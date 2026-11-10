import yara

rules = yara.compile(filepath="rules/test.yar")

matches = rules.match("samples/infectado.txt")

print(matches)
