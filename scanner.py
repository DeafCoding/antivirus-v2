import yara
import sys
import os
import hashlib



def hash_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

def load_hashes(path):
    with open(path) as f:
        return {line.strip() for line in f if line.strip()}
    
def load_rules(folder):
    paths = {}
    for name in os.listdir(folder):
        if name.endswith(".yar"):
            paths[name] = os.path.join(folder, name)
    return yara.compile(filepaths=paths)
def scan_file(rules, path, bad_hashes=None):
    hash_hit = bool(bad_hashes) and hash_file(path) in bad_hashes
    matches = rules.match(path)

    if hash_hit or matches:
        print(f"[!] INFECTED: {path}")
        if hash_hit:
            print("  - Known malware hash")
        for match in matches:
            print(f"  - Rule matched: {match.rule}")
    else:
        print(f"[OK] CLEAN: {path}")
    return matches

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <file>| <folder>")
        sys.exit(1)


    rules = load_rules("rules")
    bad_hashes = load_hashes("hashes/bad_hashes.txt")
    if os.path.isfile(sys.argv[1]):
        scan_file(rules, sys.argv[1],bad_hashes)
    elif os.path.isdir(sys.argv[1]):
        
        for name in os.listdir(sys.argv[1]):
            caminho = os.path.join(sys.argv[1], name)
            scan_file(rules, caminho, bad_hashes)
    else:
        print(f"{sys.argv[1]} not found: What were you looking for?")
        sys.exit(1)
