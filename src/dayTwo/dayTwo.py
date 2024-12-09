from itertools import count

file = open("ressource/dayTwo.txt", "r")
content = file.read()
file.close()

lines = content.strip().split("\n")
array = [[int(x) for x in line.split()] for line in lines]
result = 0

for line in array:
    is_increasing = True
    is_decreasing = True
    stairCounter = 0

    for j in range(len(line) - 1):
        difference = line[j] - line[j + 1]
        if difference > 0:
            is_increasing = False
            if difference <= 3:
                stairCounter += 1
        elif difference < 0:
            is_decreasing = False
            if difference >= -3:
                stairCounter += 1
        else:
            is_increasing = False
            is_decreasing = False
    if (is_increasing or is_decreasing) and stairCounter == len(line) - 1:
        result += 1

print(result)
