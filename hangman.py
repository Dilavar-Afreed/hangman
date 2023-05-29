import random


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
    


    


