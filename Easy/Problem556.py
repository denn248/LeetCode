s = "Let's take LeetCode contest"

new = s.split(" ")

x = []
for word in new:
    x.append(word[::-1])

print(" ".join(x))
