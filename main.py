
import random

def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

def is_valid_guess(g, guesses):
    return len(g) == 5 and g in guesses

def evaluate_guess(g, word): 
    str = ""

    for i in range(5):
        if g[i] == word[i]:
            str += "\033[32m" + g[i]
        else:
            if g[i] in word:
                str += "\033[33m" + g[i]
            else:
                str += "\033[0m" + g[i]
    
    return str + "\033[0m"

def wordle(guesses, answers):
    print("Welcome to PY_World !!! You Get 6 chances to guess a 5-letter word, To Win the Game!!!")
    s_word = random.choice(answers).lower()

    attempts = 1
    max_attempts = 6

    while attempts <= max_attempts:
        g = input("Enter Guess #" + str(attempts) + ": ").lower()
        
        if not is_valid_guess(g, guesses):
            print("Invalid guess. Please enter an English word with 5 letters.")
            continue

        if g == s_word:
            print("Congratulations!!! You guessed the word:", s_word)
            break

        attempts += 1
        feedback = evaluate_guess(g, s_word)
        print(feedback)
    
    if attempts > max_attempts:
        print("Game over. The secret word was:", s_word)

guesses_dictionary = "guesses.txt"
answer_dictionary = "answer.txt"

guesses = load_dictionary(guesses_dictionary)
answer= load_dictionary(answer_dictionary)

wordle(guesses, answer)
