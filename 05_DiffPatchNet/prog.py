#!/usr/bin/env python3
import asyncio
import shlex

clients = {}

async def chat(reader, writer):
    #me = "{}:{}".format(*writer.get_extra_info('peername'))
    #print(me)


    current_client = None
    que = asyncio.Queue()

    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(que.get())
    while not reader.at_eof():
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                send = asyncio.create_task(reader.readline())

                #print(f'Message send type is {q.result().decode()}')
                line = q.result().decode()
                line = shlex.split(line)


                match line:
                    case ['login', cow]:
                        #print(f'I got login command from u and the cow is {cow}')
                        current_client = cow
                        clients[current_client] = que
                    case ['who']:
                        await que.put(", ".join(clients.keys()))

            elif q is receive:
                receive = asyncio.create_task(que.get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()
    send.cancel()
    receive.cancel()
    print(current_client, "DONE")
    del clients[current_client]
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())