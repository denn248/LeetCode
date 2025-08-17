# Problem 387

s = "leetcode"

dict = {}

for letter in s:
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 1

indexes = []
for key, value in dict.items():
    if value == 1:
        indexes.append(s.index(key))

if indexes:
    print(min(indexes))
else:
    print(-1)