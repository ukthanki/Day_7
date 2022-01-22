import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
display = []

for letter in chosen_word:
    display.append("_")

print(hangman_art.logo)

print(" ".join(display))

lives = 6

while lives > 0:
    # Guessed Letter input
    guessed_letter = input("\nGuess a letter: ").lower()
    letter_mismatch = 0
    # Checking if the letter is in the word
    for i in range(0, word_length):
        if chosen_word[i] == guessed_letter:
            if display[i] == guessed_letter:
                print(f"You have already guessed '{guessed_letter}.'")
            display[i] = guessed_letter
        else:
            letter_mismatch += 1
            if letter_mismatch == word_length:
                print(f"You guessed '{guessed_letter}', but it is not in the word. You lose a life.")
                lives -= 1
               
    print(hangman_art.stages[lives])

    if lives == 0:
        print("YOU LOST")
        print(f"The word was: {chosen_word}")
    if chosen_word == "".join(display):
        lives = 0
        print("YOU WON")

    print(" ".join(display))


