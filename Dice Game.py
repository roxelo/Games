import random

def draw(a): # Function for the drawing of the dice
    if a ==1:
        a = " _______\n|       |\n|   *   |\n|_______|"
    elif a == 2:
        a = " _______\n| *     |\n|       |\n|     * |\n|_______|"
    elif a ==3:
        a = " _______\n| *     |\n|   *   |\n|     * |\n|_______|"
    elif a == 4:
        a = " _______\n|       |\n| *   * |\n|       |\n| *   * |\n|_______|"
    elif a == 5:
        a = " _______\n|       |\n| *   * |\n|   *   |\n| *   * |\n|_______|"
    else:
        a = " _______\n|       |\n| *   * |\n| *   * |\n| *   * |\n|_______|"
    print(a)

        
score_play = 0 #Score of the player
score_comp = 0 #Score of the computer
print ("Hi, my name is Casper.")
ans = input("Do you want to play dice with me? Y/N ")
ans = ans.lower()
if ans == "y":
   run = 0
   print ("Press enter when you are ready to roll your dice.")
while run == 0:
    roll = input("")


    #Roll the dice
    comp_dice_1 = random.randint(1,6)
    comp_dice_2 = random.randint(1,6)
    play_dice_1 = random.randint(1,6)
    play_dice_2 = random.randint(1,6)
    


    #Add the dice together
    big_comp_dice = comp_dice_1 + comp_dice_2
    big_play_dice = play_dice_1 + play_dice_2

    #Print the result    
    print ("Your dice: ")
    draw(play_dice_1) #Draw the dice
    draw(play_dice_2)
    print ("Total ", big_play_dice)
    print ("Casper's dice: ")
    draw(comp_dice_1) #Draw the dice
    draw(comp_dice_2)
    print ("Total ", big_comp_dice)

    #Tells who won or if it is a tie
    if big_comp_dice > big_play_dice:
        score_comp +=1
        print ("Casper won!\n")
    elif big_play_dice > big_comp_dice:
        score_play +=1
        print ("You won!\n")
    elif big_play_dice == big_comp_dice:
        print ("Tie\n")

    #Tell who wins the game and their final score
    if score_play == 5 or score_comp ==5:
        print ("And the CHAMPION is...")
        if score_play > score_comp:
            print ("You!!!")
            print ("Your score: ", score_play, "\n", "Casper's score: ", score_comp)
        else:
            print ("Casper!!!")
            print ("Your score: ", score_play, "\n", "Casper score: ", score_comp)

        #Restart
        ans = input("Do you want to play again? Y/N ")
        ans = ans.lower()
        if ans == "n":
            run = 1 #Stop the Game/Loop
        else: #Reset the score
            score_play = 0 
            score_comp = 0
    
