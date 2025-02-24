import cowsay
import argparse

'''
import cowsay as _cowsay, cowthink as _cowthink, Option, list_cows, \
    read_dot_cow
'''

parser = argparse.ArgumentParser()
parser.add_argument(
    "-e",
    type=str,
    help="An eye string. first cow",
    dest="eyes_1",
    default="oo",
    metavar="eye_string",
)

parser.add_argument(
    "-f", type=str, metavar="cowfile",
    help="Either the name of a cow specified in the COWPATH, "
         "or a path to a cowfile (if provided as a path, the path must "
         "contain at least one path separator)",
)

parser.add_argument(
    "-n", action="store_false",
    default=' ',
    help="If given, text in the speech bubble will not be wrapped"
)



parser.add_argument(
    "-E",
    type=str,
    help="An eye string. second cow",
    dest="eyes_2",
    default="oo",
    metavar="eye_string",
)

parser.add_argument(
    "-F", type=str, metavar="cowfile",
    help="Either the name of a cow specified in the COWPATH, "
         "or a path to a cowfile (if provided as a path, the path must "
         "contain at least one path separator)",
)

parser.add_argument(
    "-N", action="store_false",
    default=' ',
    help="If given, text in the speech bubble will not be wrapped"
)

parser.add_argument(
    "message_1", default=None, nargs='?',
    help="The message to include in the speech bubble. "
         "If not given, stdin is used instead."
)

parser.add_argument(
    "message_2", default=None, nargs='?',
    help="The message to include in the speech bubble. "
         "If not given, stdin is used instead."
)


args = parser.parse_args()

cow1 = cowsay.cowsay(message=args.message_1, eyes=args.eyes_1, wrap_text=args.n, cow=args.f)
cow2 = cowsay.cowsay(message=args.message_2, eyes=args.eyes_2, wrap_text=args.N, cow=args.F)

cow1_lines = cow1.split("\n")
cow2_lines = cow2.split("\n")
    
max_height = max(len(cow1_lines), len(cow2_lines))

cow1_lines = [""] * (max_height - len(cow1_lines)) + cow1_lines
cow2_lines = [""] * (max_height - len(cow2_lines)) + cow2_lines

maxx_line = max(len(el) for el in cow1_lines)
print(maxx_line)

print("\n".join(a.ljust(maxx_line) + b for a, b in zip(cow1_lines, cow2_lines)))