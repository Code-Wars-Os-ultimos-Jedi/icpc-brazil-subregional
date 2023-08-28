n = int(input())
heights = input().split()
heights = [int(h) for h in heights]
max_height = 10**6
arrows = 0
active_arrows = {i: 0 for i in range(1, max_height + 1)}
for height in heights:
    if active_arrows[height] == 0:
        arrows += 1
        if height == 1:
            pass
        else:
            active_arrows[height - 1] += 1
    else:
        active_arrows[height] -= 1
        if height == 1:
            pass
        else:
            active_arrows[height - 1] += 1
print(arrows)
