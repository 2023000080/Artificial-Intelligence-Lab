import random

# Word list
words = ["apple", "banana", "grape", "orange", "mango"]

# Choose a random word
word = random.choice(words)
guessed_word = ["_"] * len(word)

guessed_letters = []
attempts = 6

print("Welcome to Smart AI Hangman!")

# Function to filter possible words based on pattern
def filter_words(words, guessed_word, guessed_letters):
    possible = []
    for w in words:
        if len(w) != len(guessed_word):
            continue
        
        match = True
        for i in range(len(w)):
            if guessed_word[i] != "_" and guessed_word[i] != w[i]:
                match = False
            if guessed_word[i] == "_" and w[i] in guessed_letters:
                match = False
        
        if match:
            possible.append(w)
    
    return possible

while attempts > 0 and "_" in guessed_word:
    # Get possible words
    possible_words = filter_words(words, guessed_word, guessed_letters)

    # Count letter frequency in possible words
    freq = {}
    for w in possible_words:
        for letter in w:
            if letter not in guessed_letters:
                freq[letter] = freq.get(letter, 0) + 1

    # Choose best letter
    if freq:
        guess = max(freq, key=freq.get)
    else:
        guess = random.choice("abcdefghijklmnopqrstuvwxyz")

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

# Result
if "_" not in guessed_word:
    print("\nAI WON! The word is:", word)
else:
    print("\nAI LOST! The word was:", word)
