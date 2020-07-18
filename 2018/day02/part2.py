import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "input.txt")
words = []

with open(filename) as file:
    for line in file:
        element = line.rstrip()
        words.append(element)

for word in words:
    x = 0
    y = x

    while x < len(words):
        y += 1
        if y < len(words):
            word_1 = words[x]
            word_2 = words[y]
            equals = 0
            differents = 0
            c = 0

            while c < len(word_1):
                if word_1[c] == word_2[c]:
                    equals += 1
                elif word_1[c] != word_2[c]:
                    differents += 1
                    position = c
                if differents > 1:
                    break
                c += 1
            if equals == (len(word_1)-1) and differents == 1:
                final_word_1 = word_1
                final_word_2 = word_2
                answer = word_1[:position] + word_1[position+1:]
                print(answer)
                break
        if y == len(words):
            x += 1
            y = x
    if equals == (len(word_1)-1) and differents == 1:
        break
