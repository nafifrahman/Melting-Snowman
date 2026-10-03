# game_logic.py

import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

MAX_MISTAKES = len(STAGES) - 1  # e.g. 5 if there are 6 stages (0..5)


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display current snowman stage and the word with underscores."""
    print(STAGES[mistakes])

    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

    print("Word:  ", display_word)
    print(f"Mistakes: {mistakes} / {MAX_MISTAKES}")
    print()


def is_word_guessed(secret_word, guessed_letters):
    """Return True if all letters in secret_word are in guessed_letters."""
    return all(letter in guessed_letters for letter in secret_word)


def get_valid_guess(guessed_letters):
    """Prompt until a valid, unused single letter is entered."""
    while True:
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character (a–z).")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        return guess


def play_one_game():
    """Play a single round of Snowman Meltdown."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("\nWelcome to Snowman Meltdown!\n")

    while True:
        display_game_state(mistakes, secret_word, guessed_letters)

        if is_word_guessed(secret_word, guessed_letters):
            print("Congratulations! You saved the snowman!")
            print(f"The word was: {secret_word}")
            return True  # win

        if mistakes >= MAX_MISTAKES:
            print("Oh no! The snowman has completely melted.")
            print(f"The word was: {secret_word}")
            return False  # lose

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess not in secret_word:
            mistakes += 1


def ask_play_again():
    """Ask the user if they want to play again."""
    while True:
        answer = input("Do you want to play again? (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please type 'y' for yes or 'n' for no.")


def play_game():
    """Main entry: play rounds until the user chooses to stop."""
    while True:
        play_one_game()
        if not ask_play_again():
            print("\nThanks for playing Snowman Meltdown! Goodbye!")
            break