import random


words = ["apple", "banana", "grape", "orange", "mango"]

letter_priority = list("etaoinshrdlucmfwypvbgkjqxz")

word = random.choice(words)
guessed_word = ["_"] * len(word)

guessed_letters = []
attempts = 6

print("Welcome to AI Hangman!")

while attempts > 0 and "_" in guessed_word:
    # AI selects next letter based on priority
    guess = None
    for letter in letter_priority:
        if letter not in guessed_letters:
            guess = letter
            break

    guessed_letters.append(guess)
    print(f"\nAI guesses: {guess}")

    if guess in word:
        print("Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

    print("Word:", " ".join(guessed_word))
    print("Attempts left:", attempts)


if "_" not in guessed_word:
    print("\nAI WON! The word is:", word)
else:
    print("\nAI LOST! The word was:", word)