import re

with open("ressource/dayThree.txt", "r") as file:
    content = file.read()
endResult = 0
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do = r"mul\((\d{1,3}),(\d{1,3})\)"
dont = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.findall(pattern, content)

for match in matches:
    print(match)
    mul1 = int(match[0])
    mul2 = int(match[1])
    result = mul1 * mul2
    print(result)
    endResult += result

print(endResult)








