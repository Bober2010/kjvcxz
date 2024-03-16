f = open ("zvvvs.txt", "r", encoding="utf-8")

for line in f:
    z = int(line)
    print(z / 10 * 2)