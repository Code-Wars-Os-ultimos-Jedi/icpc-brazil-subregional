n = int(input())
string = input()

previous_char = None
count = 0
for i in range(n):
    current_char = string[i]
    if i != 0:
        previous_char = string[i - 1]

    if i != n - 1:
        next_char = string[i + 1]
    else:
        next_char = None
    if (current_char == "a" and next_char == "a") or (previous_char == "a" and current_char == "a"):
        count += 1

print(count)
