# game_logic.py

import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

MAX_MISTAKES = len(STAGES) - 1  # e.g. 3 if there are 4 stages (0..3)


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display current snowman stage and the word with underscores."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: ", display_word)
    print()


def is_word_guessed(secret_word, guessed_letters):
    """Return True if all letters in secret_word are in guessed_letters."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while True:
        # Show current state
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check win/lose before asking for next guess
        if is_word_guessed(secret_word, guessed_letters):
            print("Congratulations! You saved the snowman!")
            print(f"The word was: {secret_word}")
            break

        if mistakes >= MAX_MISTAKES:
            print("Oh no! The snowman has completely melted.")
            print(f"The word was: {secret_word}")
            break

        # Get user guess
        guess = input("Guess a letter: ").strip().lower()

        # Basic input validation: single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            # Correct guess – no change to mistakes
            pass
        else:
            # Incorrect guess – increase mistakes
            mistakes += 1