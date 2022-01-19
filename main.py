# main.py
from numpy import loadtxt

# Open wordlist
with open("wiki-100k.txt") as f:
    word_list = f.read().split()

for i in range(5):
    incorrect_letters = input("Please enter the incorrect letters (e.g. guess): ").lower()
#     letter_position = input("""Please enter the positions of the letters.  Use \
#             dots for incorrect letters, lowercase for correct but wrong \
#             position, and uppercase for correct position (e.g. g.e..): """)
    half_correct_letters = input("Please enter the yellow letters (incorrect position) e.g. ea: ").lower()
    half_correct_position = input("Please enter the position of the yellow letters, e.g. 31: ")
    correct_letters = input("Please enter the green letters (correct position) e.g. oi: ").lower()
    correct_position = input("Please enter the position of the green letters, e.g 25: ")

    word_list = list(filter(lambda word: set(incorrect_letters).intersection(set(word)), word_list))

    count = 0
    for word in word_list:
        count += 1

    j = 0
    while j < count:
        current_word = word_list[j]
        if half_correct_letters is not None:
            for z in range(len(half_correct_letters)):
                current_letter = half_correct_letters[z]
                incorrect_position = int(half_correct_position[z]) - 1
                if (not current_letter in current_word or current_word[incorrect_position]
                        == current_letter):
                    word_list.pop(j)
                    count -= 1
                    break
        if correct_letters is not None:
            for z in range(len(correct_letters)):
                current_letter = correct_letters[z]
                current_correct_position = int(correct_position[z]) - 1
                if not current_word[current_correct_position] == current_letter:
                    word_list.pop(j)
                    count -= 1
                    break

        j += 1

    count = 0
    for word in word_list:
        count += 1

    if count > 20:
        print("---Top 20 words---")
        for i in range(19):
            print(word_list[i])

    else:
        print(f'---Top {count + 1} words---')
        for i in range(count):
            print(word_list[i])
