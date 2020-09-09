  
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
    global player_score
    print("\nYou win")
    player_score+=1
def cwin():
    global computer_score
    print("\ncomputer wins")
    computer_score+=1
def tie():
    print("\nits a TIE")





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
            print("\n\ncomputer choose Scissor")
            cwin()
    elif computer_choice==1 and player_choice==3:
                print("\n\ncomputer choose Scissor")
                pwin()
    elif computer_choice==2 and player_choice==1:
                        print("\n\ncomputer choose paper")
                        pwin()
    elif computer_choice==2 and player_choice==3:
                            print("\n\ncomputer choose paper")
                            cwin()
    elif computer_choice==3 and player_choice==1:
                                print("\n\ncomputer choose Rock")
                                cwin()
    elif computer_choice==3 and player_choice==2:
                                    print("\n\ncomputer choose Rock")
                                    pwin()




    gameloop=gameloop+1



    
print("\n\n\n\nyour score is ")
print(player_score)

print("\n\n\ncomputer score is")
print(computer_score)

if computer_score>player_score:
    print(pyfiglet.figlet_format("Congrats  Computer  WINs"))
if player_score>computer_score:
    print(pyfiglet.figlet_format("Congrats YOU Win"))
if computer_score==player_score:
    print(pyfiglet.figlet_format("ITS a TIE"))


time.sleep(3)
                            
    

