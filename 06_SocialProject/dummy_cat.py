import sys
import socket
import threading
import cmd
import readline
import queue

quе = queue.Queue()

class chat(cmd.Cmd):
    prompt = 'input>>> '

    def __init__(self, *args, socket, **kwargs):
        self.s = socket
        return super().__init__(*args, **kwargs)
    
    def do_cows(self, args):
        self.s.sendall("0 cows\n".encode())

    def do_who(self, arg):
        s.sendall("0 who\n".encode())

    def do_login(self, args):
        s.sendall(f"0 login {args}\n".encode())

    def complete_login(self, text, line, begidx, endidx):
        s.sendall(f"1 cows\n".encode())
        available = (line + ".").split()
        return [c for c in quе.get().split(", ") if c.startswith(available[-1][:-1])]

    def do_quit(self, args):
        s.sendall("0 quit\n".encode())
        return True

    def do_eof(self, *args):
        return 1
    
    def do_yield(self, args):
        s.sendall(f"0 yield {args}\n".encode())
    
    def do_say(self, args):
        s.sendall(f"0 say {args}\n".encode())

    def complete_say(self, text, line, begidx, endidx):
        s.sendall(f"1 who\n".encode())
        available = (line + ".").split()
        return [c for c in quе.get().split(", ") if c.startswith(available[-1][:-1])]


    def msg_processing(self, cmdline, s):
        while True:
            response = s.recv(1024).rstrip().decode()
            #print(f'RESPONSE = {response}')
            if response[0] == '0':
                print(f"\n{response[2:]}\n{cmdline.prompt}{readline.get_line_buffer() if readline.get_line_buffer() else ""}",
                    end="", flush=True)
            else:
                quе.put(response[2:])
    




if __name__ == '__main__':
    host = "localhost" if len(sys.argv) < 2 else sys.argv[1]
    port = 1337 if len(sys.argv) < 3 else int(sys.argv[2])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    cmdline = chat(socket=s)
    mes = threading.Thread(target=cmdline.msg_processing, args = (cmdline, s))
    mes.start()
    cmdline.cmdloop()
    s.shutdown(socket.SHUT_RDWR)