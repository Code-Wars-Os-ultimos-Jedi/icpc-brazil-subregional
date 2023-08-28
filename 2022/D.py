n, x, y = [int(x) for x in input().split()]
x = str(bin(x))
least_bit_position = 0

for i in range(len(x) - 1, -1, -1):
    if int(x[i]) == 1:
        least_bit_position = len(x) - i
        break
print(n - least_bit_position)
