import argparse

parser = argparse.ArgumentParser(description="Print a friendly greeting.")
parser.add_argument("name", nargs="?", default="World")
parser.add_argument("--uppercase", action="store_true", help="Uppercase the entire greeting.")
args = parser.parse_args()

greeting = f"Hello, {args.name}!"
print(greeting.upper() if args.uppercase else greeting)
