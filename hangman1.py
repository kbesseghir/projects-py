import string
import random
from words import words
def get_word(words):
    word = random.choice(words)
    while ''in word:
        word = random.choice(words)
    return word.upper()
def hangman():
    word =get_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_word = set()
    while len(word_letter) > 0:
        user_word = input ('guess a letter: ')
      if user_word in  used_word:
        print("letter exist")
      if user_word not in alphabet:
        print("this is not a crct")
     if     user_word in alphabet:
         used_word.add(user_word)
     if user_word in word_letter:
             word_letter.remove(user_word)



hangman()