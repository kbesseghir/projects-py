import string
from words import words
import random
def get_valid(words):
    word = random.choice(words)
    while '' in word:
        word = random.choice(words)
        return word.upper()
def hangman():
    global user_letter
    word = random.choice(words)
    word_letter = set(word)
    print(word_letter)
    alphabite = set(string.ascii_uppercase)
    used_letter = set("k" )
    while len(word_letter) > 0:
        user_letter = input("guess a letter").upper()
        if user_letter in alphabite:
            used_letter.add(user_letter)
            print(used_letter)
        if user_letter in used_letter:
            print("this letter is exist")
        if user_letter in word_letter:
            word_letter.remove(user_letter)
            print(word_letter)
        if  user_letter  not in alphabite:
            print("this is not a  carcter")
    if user_letter in word_letter:
        word_letter.remove(user_letter)
        print(word_letter)



hangman()


