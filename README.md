# word_game_python
Basics level python porgram to find a random words to play with  random words

1. Importing the random Module

import random
The random module is imported to randomly select a word from the list of possible answers.

2. Loading the Word Lists

def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

How it works:
The function opens the file specified by file_path.
It reads each line, strips any whitespace (like newline characters), and stores the cleaned word in a list.
The list of words is returned.

3. Validating a Guess
   
def is_valid_guess(guess, guesses):
    return len(guess) == 5 and guess in guesses

How it works:
It ensures the guess is exactly 5 letters long.
It checks if the guess is in the list of valid guesses (from the guesses.txt file).
It returns True if both conditions are met, otherwise False.

4. Evaluating a Guess

def evaluate_guess(guess, word): 
    str = ""

    for i in range(5):
        if guess[i] == word[i]:
            str += "\033[32m" + guess[i]
        else:
            if guess[i] in word:
                str += "\033[33m" + guess[i]
            else:
                str += "\033[0m" + guess[i]
    
    return str + "\033[0m"


How it works:
A loop iterates over each letter in the guess (since the word is always 5 letters long, it runs 5 times).

For each letter in the guess:
If it matches the corresponding letter in the secret word, it is highlighted in green (\033[32m).
If it is in the secret word but in a different position, it is highlighted in yellow (\033[33m).
If it is not in the secret word, it is printed in the default color (\033[0m).
The function returns a string containing the color-coded feedback.

5. Main Game Function: wordle

def wordle(guesses, answers):
    print("Welcome to Wordle! Get 6 chances to guess a 5-letter word.")
    secret_word = random.choice(answers).lower()

    attempts = 1
    max_attempts = 6

    while attempts <= max_attempts:
        guess = input("Enter Guess #" + str(attempts) + ": ").lower()
        
        if not is_valid_guess(guess, guesses):
            print("Invalid guess. Please enter an English word with 5 letters.")
            continue

        if guess == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        attempts += 1
        feedback = evaluate_guess(guess, secret_word)
        print(feedback)
    
    if attempts > max_attempts:
        print("Game over. The secret word was:", secret_word)
