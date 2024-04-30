import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "algorithm", "developer", "coding"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word has", len(word), "letters.")

    while True:
        print("\nAttempts left:", attempts)
        print("Guessed letters:", guessed_letters)
        print("Current word:", display_word(word, guessed_letters))

        if "_" not in display_word(word, guessed_letters):
            print("\nCongratulations! You've guessed the word:", word)
            break

        if attempts == 0:
            print("\nSorry, you ran out of attempts! The word was:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess!")

hangman()