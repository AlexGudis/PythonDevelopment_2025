import cowsay
import argparse
import readline
import shlex
import cmd

# command message params cow_type reply message params
# twocows> cowsay "Hi there" moose eyes="^^" reply "Ahoy!" sheep 

class cows(cmd.Cmd):
    prompt = "twocows> "
    all_cows = cowsay.list_cows()

    def create_cow_params(self, i, line):
        cow_params = {'cow':'default', 'eyes':'oo', 'tongue':'  '}
        while i < len(line) and line[i] != 'reply':
            print(f'new_param={line[i]}')
            if line[i] in self.all_cows:
                cow_params['cow'] = line[i]
            elif '=' in line[i]:
                kv = line[i].split('=')
                cow_params[kv[0]] = kv[1]
            else:
                raise 'Something wrong with your arguments. Check help <function> to see'
            i += 1
        return cow_params, i


    def make_params(self, line):
        line = shlex.split(line)
        i = 0
        message1 = line[i]
        i += 1
        cow_params1 = {'cow':'default', 'eyes':'oo', 'tongue':'  '}
        cow_params1, i = self.create_cow_params(i, line)
        i += 1 # pass reply phrase
        message2 = line[i]
        i += 1

        cow_params2 = {'cow':'default', 'eyes':'oo', 'tongue':'  '}
        cow_params2, i = self.create_cow_params(i, line)

        return message1, cow_params1, message2, cow_params2
    

    def drow_cows(self, cow1, cow2):
        cow1_lines = cow1.split("\n")
        cow2_lines = cow2.split("\n")
            
        max_height = max(len(cow1_lines), len(cow2_lines))

        cow1_lines = [""] * (max_height - len(cow1_lines)) + cow1_lines
        cow2_lines = [""] * (max_height - len(cow2_lines)) + cow2_lines

        maxx_line = max(len(el) for el in cow1_lines)

        print("\n".join(a.ljust(maxx_line) + b for a, b in zip(cow1_lines, cow2_lines)))



    def do_cowsay(self, line):
        "This command prints a dialog between two cows with cowsay function.\nThe syntax is: message cow_type params reply message cow_type params\nparams is something like eyes='&&'"
        
        message1, cow_params1, message2, cow_params2 = self.make_params(line)

        print(message1, cow_params1, message2, cow_params2)
        
        cow1 = cowsay.cowsay(message1, cow=cow_params1['cow'], eyes=cow_params1['eyes'], tongue=cow_params1['tongue'])
        cow2 = cowsay.cowsay(message2, cow=cow_params2['cow'], eyes=cow_params2['eyes'], tongue=cow_params2['tongue'])

        self.drow_cows(cow1, cow2)
        

    def complete_cowsay(self, text, line, begidx, endidx):
        #print()
        #print(f'text={text}, line={line}, begidx={begidx}, endidx={endidx}')
        #print()
        return [c for c in self.all_cows if c.startswith(text)]
    

    def do_cowthink(self, line):
        "This command prints a dialog between two cows with cowthink function.\nThe syntax is: message cow_type params reply message cow_type params\nparams is something like eyes='&&'"
        
        message1, cow_params1, message2, cow_params2 = self.make_params(line)
        
        cow1 = cowsay.cowthink(message1, cow=cow_params1['cow'], eyes=cow_params1['eyes'], tongue=cow_params1['tongue'])
        cow2 = cowsay.cowthink(message2, cow=cow_params2['cow'], eyes=cow_params2['eyes'], tongue=cow_params2['tongue'])

        self.drow_cows(cow1, cow2)
        

    def complete_cowthink(self, text, line, begidx, endidx):
        #print()
        #print(f'text={text}, line={line}, begidx={begidx}, endidx={endidx}')
        #print()

        return [c for c in self.all_cows if c.startswith(text)]
    

    def do_list_cows(self, args):
        "Print all avalable cows to drow"
        for el in self.all_cows:
            print(el)
    

    def complete_list_cows(self, text, line, begidx, endidx):
        print()
        print(f'text={text}, line={line}, begidx={begidx}, endidx={endidx}')
        print()
        #return "tt"


if __name__ == '__main__':
    cows().cmdloop() 
















'''args = parser.parse_args()

cow1 = cowsay.cowsay(message=args.message_1, eyes=args.eyes_1, wrap_text=args.n, cow=args.f)
cow2 = cowsay.cowsay(message=args.message_2, eyes=args.eyes_2, wrap_text=args.N, cow=args.F)

cow1_lines = cow1.split("\n")
cow2_lines = cow2.split("\n")
    
max_height = max(len(cow1_lines), len(cow2_lines))

cow1_lines = [""] * (max_height - len(cow1_lines)) + cow1_lines
cow2_lines = [""] * (max_height - len(cow2_lines)) + cow2_lines

maxx_line = max(len(el) for el in cow1_lines)
print(maxx_line)

print("\n".join(a.ljust(maxx_line) + b for a, b in zip(cow1_lines, cow2_lines)))'''