import random
def  guess(x):
    random_nmbr  =  random.randint(1, x)
    guess = 0

    while guess !=  random_nmbr:
        guess  =  int(input(f"Hi..guess a number between 1 and {x}:  "))
        if  guess <  random_nmbr :
            print("sorry ,too low  try again ")
        elif   guess  >  random_nmbr:
                print("sorry ,too height try again")
    print("yay .. congrats , u  guessed  the number ")


guess(10)