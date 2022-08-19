import random
def  computer_guess(x):
     low =  1
     heigh = x
     feedback = ""
     guess :int
     while  feedback !=  "c":
        guess= random.randint(low, heigh)
        feedback = input(f"if the number{guess} is low ..write L  or heigh write H or correct write C:  ")
        if feedback ==  "l":
           low= guess  + 1
        if feedback == "h":
          heigh = guess-1
     print("correctly !!!")

computer_guess(10)

