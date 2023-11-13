import random as a


def create_list():
    mylist=[]
    num=int(input("How many numbers do you want the game to contain ? :"))
    for i in range(0,num+1): mylist.append(i)
    return mylist


def guess():
    player_guess = int(input("Type in your guess: "))
    while player_guess not in mylist:
        print("The charecter entererd is not valid")
        player_guess = int(input("Type in your guess again: "))
    return player_guess


def answer_check(player_guess,Shuffled_num):
    while player_guess != Shuffled_num:
        print("Try again")
        player_guess=int(input("Type your guess again:"))
    print("Right answer")


mylist = create_list()
Shuffled_num=a.choice(mylist)
print(Shuffled_num)
player_guess= guess()
answer_check(player_guess,Shuffled_num)