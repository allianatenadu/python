import random

# Secret word stored in the program
secret_word = "mosiah"
secret_word = secret_word.lower()

print("Welcome to the word guessing game!")
print("Your hint is: " + "_ " * len(secret_word))

guesses = 0

while True:
    guess = input("What is your guess? ").strip().lower()
    guesses += 1

    if len(guess) != len(secret_word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        continue

    if guess == secret_word:
        print(f"Congratulations! You guessed it! It took you {guesses} guesses.")
        break
    else:
        hint = ""
        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                hint += guess[i].upper()  # Correct letter and correct position
            elif guess[i] in secret_word:
                hint += guess[i].lower()  # Correct letter but wrong position
            else:
                hint += "_"  # Letter not in the word

        print(f"Your hint is: {hint.replace('', ' ').strip()}")
