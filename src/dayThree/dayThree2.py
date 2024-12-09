import re

with open("ressource/dayThree.txt", "r") as file: content = file.read()

pattern_mul = r"mul\((\d{1,3}),(\d{1,3})\)"
pattern_do = r"do\(\)"
pattern_dont = r"don't\(\)"

endResult = 0
mul_enabled = True

matches_mul = re.findall(pattern_mul, content)
matches_do = re.findall(pattern_do, content)
matches_dont = re.findall(pattern_dont, content)

position_mul = [m.start() for m in re.finditer(pattern_mul, content)]
position_do = [m.start() for m in re.finditer(pattern_do, content)]
position_dont = [m.start() for m in re.finditer(pattern_dont, content)]

all_positions = sorted(position_mul + position_do + position_dont)

i = 0
while i < len(all_positions):
    current_pos = all_positions[i]
    print(current_pos)
    if current_pos in position_do:
        mul_enabled = True
    elif current_pos in position_dont:
        mul_enabled = False
    elif current_pos in position_mul and mul_enabled:
        match = re.findall(pattern_mul, content[current_pos:])[0]
        mul1 = int(match[0])
        mul2 = int(match[1])
        result = mul1 * mul2
        endResult += result
    i += 1

print(endResult)
