# Problem 374


n = 3

pick = 3

low = 1
high = n


while True:
    g = (low+high) // 2
    print(f'Current guess: {g}')
    if g > pick:
        print(f'New high: {g}')
        high = g
    elif g < pick:
        print(f'New low: {g}')
        low = g
    else:
        print(f'Correct guess {g}')
        break


