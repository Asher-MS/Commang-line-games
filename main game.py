import pyfiglet
import time
import random


def intro():
    print("Welcome To")
    w=pyfiglet.figlet_format("Rock\n  Paper\n    &scissors")
    print(w)
    print("             BY The Silicon Guy")
    
    
intro()


print("Please Enter Your Name")
player_name=input()


print("Welcome To The Game")
print(pyfiglet.figlet_format(player_name))


gameloop=0
player_score=0
computer_score=0

player_choice="null"
computer_coice="null"
def pwin():
    print("You win")
    player_score+=1
def cwin():
    print("computer wins")
    computer_score+=1
def tie():
    print("its a TIE")





while gameloop<5:                                                                                   # 1=Scissor 2=paper 3=rock
    print("Your score is")
    print(player_score)
    print("Computer score is ")
    print(computer_score)



    player_choice=int(input("Enter Your Choice \n1.Scissor \n2.PAPER \n3.ROCK"))

    computer_choice=int(random.randint(1,3))

    if computer_choice==player_choice:
        tie()
    elif(computer_choice==1 and player_choice)==2:
            print("computer choose Scissor")
            cwin()
    elif computer_choice==1 and player_choice==3:
                print("computer choose Scissor")
                pwin()
    elif computer_choice==2 and player_choice==1:
                        print("computer choose paper")
                        pwin()
    elif computer_choice==2 and player_choice==3:
                            print("computer choose paper")
                            cwin()
    elif computer_choice==3 and player_choice==1:
                                print("computer choose Rock")
                                cwin()
    elif computer_choice==3 and player_choice==2:
                                    print("computer choose Rock")
                                    pwin()




    gameloop=gameloop+1



    




     
    

    
    
print("your score is "+player_score)
print("computer score is"+computer_score)




time.sleep(3)
                            
    
