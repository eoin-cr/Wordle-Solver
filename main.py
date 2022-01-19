# main.py
from numpy import loadtxt

# Open wordlist
with open("wiki-100k.txt") as f:
# with open("test-list.txt") as f:
    word_list = f.read().split()

for i in range(5):
    incorrect_letters = input("Please enter the incorrect letters (e.g. ges): ").lower()
#     letter_position = input("""Please enter the positions of the letters.  Use \
#             dots for incorrect letters, lowercase for correct but wrong \
#             position, and uppercase for correct position (e.g. g.e..): """)
    half_correct_letters = input("Please enter the yellow letters (incorrect position) e.g. ea: ").lower()
    half_correct_position = input("Please enter the position of the yellow letters, e.g. 13: ")
    correct_letters = input("Please enter the green letters (correct position) e.g. i: ").lower()
    correct_position = input("Please enter the position of the green letters, e.g 5: ")

    word_list = list(filter(lambda word: not set(incorrect_letters).intersection(set(word)), word_list))

    def count(word_list):
        counter = 0
        for word in word_list:
            counter += 1
        return counter

    j = 0
    while j < count(word_list):
        removed = False
#         print(f'word list: {word_list} \n --- \n')
#         print(f'j: {j}')
#         print(f'count: {count}')
        current_word = word_list[j]
#         print(f'Cur word: {current_word}')
        if half_correct_letters is not None:
            for z in range(len(half_correct_letters)):
                current_letter = half_correct_letters[z]
                incorrect_position = int(half_correct_position[z]) - 1
#                 print(f'Word: {current_word}')
#                 print(f'Letter: {current_word[incorrect_position]} {current_letter}')
                if (not current_letter in current_word or current_word[incorrect_position]
                        == current_letter):
                    word_list.pop(j)
#                     count -= 1
                    removed = True

        if correct_letters is not None and not removed:
            for z in range(len(correct_letters)):
                current_letter = correct_letters[z]
                current_correct_position = int(correct_position[z]) - 1
                if not current_word[current_correct_position] == current_letter:
                    word_list.pop(j)
#                     count -= 1
                    removed = True

        if not removed:
            j += 1
#
    count = 0
    for word in word_list:
        count += 1

    if count > 20:
        print("---Top 20 words---")
        for i in range(19):
            print(word_list[i])

    else:
        print(f'---Top {count} words---')
        for i in range(count):
            print(word_list[i])
