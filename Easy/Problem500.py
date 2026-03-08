row1 = "qwertyuiop"
row2 = "asdfghjkl"
row3 = "zxcvbnm"


words = ["qz", "wq", "asdddafadsfa", "adfadfadfdassfawde"]


passed = []

for word in words:
    row = ""
    if len(word) == 1:
        passed.append(word)
        continue
    ok = True
    for letter in word.lower():
        if row:
            if letter in row:
                continue
            else:
                ok = False
                break
        if letter in row1:
            row = row1
            continue
        elif letter in row2:
            row = row2
            continue
        elif letter in row3:
            row = row3
            continue
    if ok:
        passed.append(word)

print(passed)
