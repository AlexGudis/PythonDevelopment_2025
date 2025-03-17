#!/usr/bin/env python3
import asyncio
import shlex
import cowsay

class User:
    def __init__(self):
        self.name = None
        self.que = asyncio.Queue()

clients = {}

async def chat(reader, writer):
    test_connect = "{}:{}".format(*writer.get_extra_info('peername'))
    print(test_connect)


    user = User()

    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(user.que.get())
    while not reader.at_eof():
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())

                line = q.result().decode()
                line = shlex.split(line)


                match line:
                    case ['login', cow]:
                        if cow not in cowsay.list_cows():
                            await user.que.put("You cannot choose this login. Please check cows command")
                        elif cow not in clients.keys():
                            user.name = cow
                            clients[user.name] = user.que
                        else:
                            await user.que.put("This login is already assigned. Please chose another one from cows command")

                    case ['who']:
                        await user.que.put(", ".join(clients.keys()))

                    case ['quit']:
                            send.cancel()
                            receive.cancel()
                            print(user.name, "DONE")
                            del clients[user.name]
                            writer.close()
                            await writer.wait_closed()
                    case ['cows']:
                        already = set(clients.keys()) 
                        free = set(cowsay.list_cows()) - already
                        await user.que.put(", ".join(list(free)))

                    case ['yield', *msg]:
                        if user.name not in clients.keys():
                            await user.que.put("You are not signed in yet. Please login.")
                        else:
                            for out in clients.values():
                                if out is not clients[user.name]:
                                    await out.put(f"{user.name} {' '.join(msg)}")
                            

                    case ['say', to, *msg]:
                        if user.name not in clients.keys():
                            await user.que.put("You are not signed in yet. Please login.")
                        elif to not in clients.keys():
                            await user.que.put("This user is not signed in yet")
                        else:
                            await clients[to].put(f"{user.name} {' '.join(msg)}")
                    
                    case [_]:
                        await user.que.put("This isn't a valid command!")



            elif q is receive:
                receive = asyncio.create_task(user.que.get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()

async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())