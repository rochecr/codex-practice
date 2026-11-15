import argparse

parser = argparse.ArgumentParser(description="Print a friendly greeting.")
parser.add_argument("name", nargs="?", default="World")
parser.add_argument("--uppercase", action="store_true", help="Uppercase the entire greeting.")
parser.add_argument("--goodbye", action="store_true", help="Say Goodbye instead of Hello.")
args = parser.parse_args()

salutation = "Goodbye" if args.goodbye else "Hello"
greeting = f"{salutation}, {args.name}!"
print(greeting.upper() if args.uppercase else greeting)
