
import random

# Load words from file
with open("words.txt", "r") as file:
    words = [
        word.strip().lower()
        for word in file
        if word.strip().isalpha()
    ]

# Hangman drawings
stages = [
    """
       -----
       |   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
    =========
    """
]

# Game variables
word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("\n================================")
print("        HANGMAN GAME")
print("================================")
print("Guess the hidden word!")
print("You have 6 attempts.")

# Main game loop
while wrong_guesses < max_attempts:

    print(stages[wrong_guesses])

    # Display hidden word
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("Word:", display)
    print("Guessed letters:", guessed_letters)
    print("Attempts left:", max_attempts - wrong_guesses)

    # Check win condition
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You won!")
        print("The word was:", word)
        break

    # Take user input
    guess = input("\nEnter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Enter one letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print(stages[wrong_guesses])
    print("\nGame Over!")
    print("The correct word was:", word)

print("\nThank you for playing!")
