import yara
import sys
import os
rules = yara.compile(filepath="rules/test.yar")
if len(sys.argv) < 2:
    print("Uso: python scanner.py <archivo>")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print(f"Error: el archivo no existe: {sys.argv[1]}")
    sys.exit(1)
matches = rules.match(sys.argv[1])
print(matches)
