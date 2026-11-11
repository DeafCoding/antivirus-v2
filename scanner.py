import yara
import sys
import os
def load_rules(folder):
    paths = {}
    for name in os.listdir(folder):
        if name.endswith(".yar"):
            paths[name] = os.path.join(folder, name)
    return yara.compile(filepaths=paths)
def scan_file(rules, path):
    matches = rules.match(path)

    if matches:
        print(f"{path} has been reported with:")
        for match in matches:
            print(match.rule)
    else:
        print(f"{path} is clean")
    return matches

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <file>| <folder>")
        sys.exit(1)


    rules = load_rules("rules")
    if os.path.isfile(sys.argv[1]):
        scan_file(rules, sys.argv[1])
    elif os.path.isdir(sys.argv[1]):
        
        for name in os.listdir(sys.argv[1]):
            caminho = os.path.join(sys.argv[1], name)
            scan_file(rules, caminho)
    else:
        print(f"{sys.argv[1]} not found: What were you looking for?")
        sys.exit(1)
