import random as r

def create_list(num):
    mylist=[]
    for i in range(0,num):
        mylist.append(i)
    return mylist

def player_guess():
    guess=''
    while guess not in mylist:
        guess=int(input("Enter your guess: "))
    return int(guess)

def answer(num,guess):
    while num != guess:
        print("Wrong guess try again")

num=int(input("Enter how long the list should be(including 0 in the start): "))

mylist = create_list(num)
num=r.choice(mylist)
print (mylist)4

print (num)
guess=player_guess()
answer(num,guess)
