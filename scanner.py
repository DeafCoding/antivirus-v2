import yara
import sys
import os
if len(sys.argv) < 2:
    print("Usage: python scanner.py <file>")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print(f"Error: {sys.argv[1]} does not exist")
    sys.exit(1)
rules = yara.compile(filepath="rules/test.yar")
matches = rules.match(sys.argv[1])
if matches:
    print(f"{sys.argv[1]} has been reported with:")
    for match in matches:
        print(match.rule)
else:
    print(f"{sys.argv[1]} is clean")
