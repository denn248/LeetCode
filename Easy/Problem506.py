from typing import Any

score: list[Any] = [10, 3, 8, 9, 4]
pairs = []
answer = [""] * len(score)
for idx, value in enumerate(score):
    pairs.append((value, idx))

pairs.sort(reverse=True)

for place, (value, idx) in enumerate(pairs):
    if place == 0:
        answer[idx] = "Gold Medal"
    elif place == 1:
        answer[idx] = "Silver Medal"
    elif place == 2:
        answer[idx] = "Bronze Medal"
    else:
        answer[idx] = str(place + 1)


print(answer)
