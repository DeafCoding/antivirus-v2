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


rules = yara.compile(filepath="rules/test.yar")
if os.path.isfile(sys.argv[1]):
    scan_file(rules, sys.argv[1])
elif os.path.isdir(sys.argv[1]):
    
    for name in os.listdir(sys.argv[1]):
        caminho = os.path.join(sys.argv[1], name)
        scan_file(rules, caminho)
else:
    print("File not found: What were you looking for?")
    sys.exit(1)

