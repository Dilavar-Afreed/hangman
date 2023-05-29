import os
import tempfile

import hangman

def test_select_random_word_min_length():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["cat\n","elephant\n","mouse\n","dog\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "elephant"

    os.unlink(name)

def test_select_random_word_no_non_alpha_chars():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["pine's\n","Dr.\n","Ångström\n","policeman\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "policeman"

    os.unlink(name)

def test_select_random_word_no_capitals():
    # create temporary file
    name = tempfile.mktemp()
    f = open(name, "w")
    f.writelines(["Alexander\n","AMD\n","California\n","pelican\n"])
    f.close()

    for _ in range(20):
        secret_word = hangman.get_random_word(name)
        assert secret_word == "pelican"

    os.unlink(name)


def test_select_random_word_no_repetitions():
    secret_words = set()
    for _ in range(10):
        secret_words.add(hangman.get_random_word())
    assert len(secret_words) == 10



# masked words

def test_masked_word_no_guess():
    assert hangman.mask_word("elephant",[]) == "--------"

def test_masked_word_1_guess():
    assert hangman.mask_word("elephant","l") == "-l------"

def test_masked_word_wrong_guess():
    assert hangman.mask_word("elephant","x") == "--------"


def test_masked_word_guess_multi():
     assert hangman.mask_word("elephant","e") == "e-e-----"


def test_masked_word_guess_cmplt():
     assert hangman.mask_word("elephant",["e","l","p","h","a","n","t"]) == "elephant"


# no of turns

def test_no_of_turns_no_guess():
    assert hangman.n_turns("elephant","") == 7


def test_no_of_turns_wrong_guess():
    assert hangman.n_turns("elephant","x") == 6

def test_no_of_turns_wright_guess():
    assert hangman.n_turns("elephant","e") ==7


