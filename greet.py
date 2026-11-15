import argparse


def positive_integer(value):
    try:
        number = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError("must be a positive integer") from None
    if number < 1:
        raise argparse.ArgumentTypeError("must be a positive integer")
    return number


parser = argparse.ArgumentParser(description="Print a friendly greeting.")
parser.add_argument("name", nargs="?", default="World")
parser.add_argument("--uppercase", action="store_true", help="Uppercase the entire greeting.")
parser.add_argument("--goodbye", action="store_true", help="Say Goodbye instead of Hello.")
parser.add_argument("--repeat", type=positive_integer, default=1,
                    help="Print the greeting this many times (positive integer; default: 1).")
args = parser.parse_args()

salutation = "Goodbye" if args.goodbye else "Hello"
greeting = f"{salutation}, {args.name}!"
if args.uppercase:
    greeting = greeting.upper()
for _ in range(args.repeat):
    print(greeting)
