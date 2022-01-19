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

    # Removes all words containing incorrect letters from the list
    word_list = list(filter(lambda word: not set(incorrect_letters).intersection(set(word)), word_list))

    # Calculates the amount of words in the list so it doesn't try pop
    # an element outside the list
    def count(word_list):
        counter = 0
        for word in word_list:
            counter += 1
        return counter

    j = 0
    while j < count(word_list):
        removed = False
        # Selects a word from the word list
        current_word = word_list[j]
        if half_correct_letters is not None:
            for z in range(len(half_correct_letters)):
                # Selects one of the half correct letters and its position
                current_letter = half_correct_letters[z]
                incorrect_position = int(half_correct_position[z]) - 1

                # Remove words that either don't have the letter or have it in
                # an incorrect position
                if (not current_letter in current_word or current_word[incorrect_position]
                        == current_letter):
                    word_list.pop(j)
#                     count -= 1
                    removed = True
                    break

        if correct_letters is not None and not removed:
            for z in range(len(correct_letters)):
                #Selects one of the correct letters and its position
                current_letter = correct_letters[z]
                current_correct_position = int(correct_position[z]) - 1

                # Removes words that don't have a correct letter in the right
                # position
                if not current_word[current_correct_position] == current_letter:
                    word_list.pop(j)
#                     count -= 1
                    removed = True
                    break

        # If nothing was removed increase j by one.  This check ensures
        # no words are skipped
        if not removed:
            j += 1

    count = 0
    for word in word_list:
        count += 1

    # If there's more than 10 elements print the top 10
    if count > 10:
        print("---Top 10 words---")
        for i in range(19):
            print(word_list[i])

    # Otherwise just print all the words
    else:
        print(f'---Top {count} words---')
        for i in range(count):
            print(word_list[i])
