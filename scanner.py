import yara
import sys
rules = yara.compile(filepath="rules/test.yar")
if len(sys.argv) < 2:
    print("Uso: python scanner.py <archivo>")
    sys.exit(1)
matches = rules.match(sys.argv[1])
print(matches)
