import random
from collections import Counter

def load_words(filename):
    words = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            words.append(line.strip().lower())
    return words

def pick_random(words):
    return random.choice(words)

def display_state(history: list[list[str]]) -> None:
    for row in history:
        print("".join(row)) 

def checking(wordle: str, words: list[str]) -> None:
    history = []
    i = 0
    while i < 6:
        freq = Counter(wordle)
        temp = [''] * 5
        guess = input(f"Enter a guess ({i+1}/6): ").strip().lower()

        if len(guess) != 5 or not guess.isalpha() or guess not in words:
            print("Invalid Input, please put a valid English word.")
        else:
            for j in range(5):
                if guess[j] == wordle[j]:
                    temp[j] = f"\033[92m{guess[j]}\033[0m"
                    freq[guess[j]] -= 1
            for j in range(5):
                if temp[j]:
                    continue
                if freq[guess[j]] > 0:
                    temp[j] = f"\033[93m{guess[j]}\033[0m"
                    freq[guess[j]] -= 1
                else:
                    temp[j] = f"\033[90m{guess[j]}\033[0m"

            i += 1
            history.append(temp)
            display_state(history)
            if guess == wordle:
                print(f"Your guess is correct, you won in {i} guesses!")
                return

    print(f"Sorry you are out of guesses, the correct word was '{wordle}'.")

words = load_words("wordle.txt")
wordle = pick_random(words)
checking(wordle, words)
