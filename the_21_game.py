import random as r

play_again = "yes"
while play_again[0] =="y":
    total =0
    player =["human","computer"]
    current_player =r.randint(0,1)
    print("the fist player is : "+player[current_player])
    while total <=21 :
        if current_player == 0:
            player_choice = int(input("input your choise 1-3 : "))
            
            while player_choice > 3:
                print("your choise is error! please try again :")
                player_choice = int(input("input your choise 1-3 : "))
                
        else :
            player_choice = r.randint(1,3)
            
        total +=player_choice
        
        
        if total >21 :
            break
        
        current_player +=1
        if current_player ==2:
            current_player =0
            
    print("the loser is :"+player[current_player])
    
    play_again = str(input("play again ?: "))
    
    if play_again[0] =="y" or play_again[0]=="Y":
        continue
    else:
        break
        
    