import random

word_list = ["ardvark", "baboon", "camel", "lion","jaguar"]

# Choosing a Random Word
# word_num = random.randint(0, len(word_list)-1)
# chosen_word = word_list[word_num]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []

for letter in chosen_word:
    display.append("_")
print(chosen_word)
print(display)

# Guessed Letter input
guessed_letter = input("Guess a letter: ").lower()
letter_is_in_word = False

occurrence = 0
index_list=[]

# Checking if the letter is in the word
for i in range(0, word_length):
    if chosen_word[i] == guessed_letter:
        occurrence += 1
        display[i] = guessed_letter
        index_list.append(1)
    else:
        index_list.append(0)

if occurrence > 0:
    letter_is_in_word = True

# for item in index_list:
#     if item == 0:
#         print("Wrong")
#     else:
#         print("Right")

print(display)

# if guessed_letter in chosen_word:
#     print(True)