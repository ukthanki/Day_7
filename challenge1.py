import random

word_list = ["ardvark", "baboon", "camel", "lion","jaguar"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []

for letter in chosen_word:
    display.append("_")
print(chosen_word)
print(display)

lives = 6

while lives > 0:
    # Guessed Letter input
    guessed_letter = input("Guess a letter: ").lower()
    letter_mismatch = 0
    # Checking if the letter is in the word
    for i in range(0, word_length):
        if chosen_word[i] == guessed_letter:
            display[i] = guessed_letter
        else:
            letter_mismatch += 1
            if letter_mismatch == word_length:
                lives -= 1
               
    print(f"Lives left: {lives}")

    if lives == 0:
        print("YOU LOST")
        print(f"The word was: {chosen_word}")
    if chosen_word == "".join(display):
        lives = 0
        print("YOU WON")

    print(display)
    
    # print("".join(display))


