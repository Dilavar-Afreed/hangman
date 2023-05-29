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
        if i == b:
            z.append(b)
        else:
            z.append("-")

    return "".join(z)


a = mask_word("elephant", "l")
print(a)
