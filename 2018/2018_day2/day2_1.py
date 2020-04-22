import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")

occurrence_2 = 0
occurrence_3 = 0

with open(filename) as letters:

    for word in letters:
        amount_2 = 0
        amount_3 = 0
        unique_chars = set(word)

        for c in unique_chars:
            amount = word.count(c)
            if amount == 2:
                amount_2 += 1
            elif amount == 3:
                amount_3 += 1

        if amount_2 != 0:
            occurrence_2 += 1
        if amount_3 != 0:
            occurrence_3 += 1

total = occurrence_2 * occurrence_3
print(total)
