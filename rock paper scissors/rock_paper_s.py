import random
import time

x = input("Do u want to play the game? enter 'y' for yes and 'n' for no : ")
print("")
time.sleep(1.5)

if x == 'y':
    print("Its a game of rock, paper and scissors\nSome general instructions:\n'r' for rock, 'p' for paper, 's' for scissors")
    print("Get ready !\n")
    

    def game():
            score_pc = 0
            score_user = 0
           
            while (score_pc + score_user) <= 3:
                user = input("Your turn (enter r or s or p):  ")
                computer = random.choice(['r', 's', 'p'])
                
                if win_checker(user, computer):    
                    score_user+=1
                    print(f"your score : {score_user}. pc score is {score_pc}.")
                
                    
                elif user == computer:
                    print("Its a tie")
                    
                else:
                    score_pc+=1
                    print(f"your score : {score_user}", f"pc score : {score_pc}")
                
                print(f"pc choice is {computer}")    
            
            
            print(f"user score is {score_user} and pc score is {score_pc}")
            time.sleep(1)
            print("Game Over")
            time.sleep(1)
            
    def win_checker(player1, player2):
        if (player1 == 'r' and player2 == 's') or (player1=='s' and player2=='p') or (player1=='p' and player2=='r'):
            return True
        
    game()
    
elif x == 'n':
    print('Your wish! Thank You')
    time.sleep(1)


    


    
    


