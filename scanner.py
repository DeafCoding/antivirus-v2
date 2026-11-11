import yara
import sys
import os

def scan_file(rules, path):
    matches = rules.match(path)

    if matches:
        print(f"{path} has been reported with:")
        for match in matches:
            print(match.rule)
    else:
        print(f"{path} is clean")
if len(sys.argv) < 2:
    print("Usage: python scanner.py <file>")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print(f"Error: {sys.argv[1]} does not exist")
    sys.exit(1)

rules = yara.compile(filepath="rules/test.yar")

scan_file(rules, sys.argv[1])
