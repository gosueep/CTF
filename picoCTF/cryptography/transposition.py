message = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"
result = ""

for i in range(0, len(message)-2, 3):
    result += message[i+2] + message[i:i+2]
    print(result)

print(result)

# The flag is picoCTF{7R4N5P051N6_15_3XP3N51V3_109AB02E}