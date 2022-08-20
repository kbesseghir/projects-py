import random 
import string 
from words import words

word = random.choice(words)
print(word)
def hangman():
    word_letter = set(word.upper())
    print(word_letter)
    alphabit = set(string.ascii_uppercase)
    used_letter = set()
    while len(word_letter)> 0:
       
        user_letter = input ("guess a letter : ").upper()
        if user_letter in used_letter:
            print("this letter exist")
        if user_letter in word_letter:
         
          print("current word :", " ".join(user_letter)) 
          word_letter.remove(user_letter)
          print(word_letter)   
        if user_letter in alphabit:
            used_letter.add(user_letter)
            print( "u have already used thi letter" , " ".join(used_letter))
        else:  
            print("this is not a caracter")  
       
           
        


              
    print("yay")

hangman()