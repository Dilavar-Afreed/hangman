import random

import tempfile
import os


def get_random_word(wordfile="/usr/share/dict/words"):
    candidate_words = []
    with open(wordfile) as f:
        for word in f:
            word = word.strip()
            if len(word) >= 6 and word.islower() and word.isalpha():
                candidate_words.append(word)
    word = random.choice(candidate_words)
    return word


def mask_word(a, b):
    z = []
    for i in a:
        if i in b:
            z.append(i)
        else:
            z.append("-")

    return "".join(z)

def n_turns(word, guess, guesses):
    max_turns = 7
    if guess not in word and guess not in guesses:
        turns_left = max_turns - 1
    else:
        turns_left = max_turns
    
    return turns_left

def guess_list(guess,guesses):
    if guess not in guesses:
        guesses.append(guess)

def play_hangman():
    word = get_random_word()
    guesses = []
    turns_left = 7
    print("Welcome to Hangman!")
    
    while turns_left > 0:
        masked_word = mask_word(word, guesses)
        print("Word:", masked_word)
        print("Turns left:", turns_left)
        print("Guesses:", guesses)

        guess = input("Enter your guess: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Please enter a single letter.")
            continue

        if guess in guesses:
            print("You've already guessed that letter. Try again.")
            continue

        guess_list(guess, guesses)

        if guess in word:
            print("Correct guess!")
            if set(word) == set(guesses):
                print("Congratulations! You've guessed the word correctly: " + word)
                break
        else:
            turns_left -= 1
            print("Wrong guess!")
            if turns_left == 0:
                print("Game over! You've run out of turns. The word was:", word)

    print("Thank you for playing Hangman!")

# Run the game
play_hangman()
    


    


