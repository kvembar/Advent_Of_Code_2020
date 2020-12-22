#Crab Combat (AOC Day 22)
#Keshav V.
#This program is the product of sweat, quite a lot of tears, and a Pacific Ocean of blood. You'll see why.

#Important Note: You'll see some triple quotes in the code below. With them, you have Part 1.
#Take out the triple quotes and indent the line immediately after for Part 2's code.

with open("Day_22_input.txt","r") as f:
     player1 = []
     player2 = []
     mode = "1" #The power of the mode variable. Idk if this method actually has a name, but it works.
     first = True
     for line in f:
         if first == True: #Skips line with "Player 1/2" on it.
             first = False
             continue
        
         if line == "\n": #Separator between the P1 and P2 decks
             mode = "2"
             first = True
             continue

         if mode == "1":
             player1.append(int(line.rstrip("\n"))) #Add to player 1s deck.

         if mode == "2":
             player2.append(int(line.rstrip("\n"))) #Add to player 2s deck.

def war(player_1, player_2): #Let's be honest, this is just war.
    decks_plaid = set() #First appearance of the set data type! Learned it from Sumner(thank you btw)!
    while True: #Repeat until either player1, player2 or an infinite loop is achieved.
        if player_1 == []:
            winner = "player2"
            break

        elif player_2 == []:
            winner = "player1"
            break

        '''
        if (tuple(player_1), tuple(player_2)) in decks_plaid:
            winner = "player1" #If the config appears in the decks already plaid, declares winner as player 1.
            break
        else:
            decks_plaid.add((tuple(player_1), tuple(player_2)))
            #This tracks the decks that have already occured. Adds the current config to the set.
            #The fact that it is a set is a small time improvement from O(n) to O(1)
        '''
        
        player_1_card = player_1.pop(0)
        player_2_card = player_2.pop(0)
        '''
        if ((len(player_1)>=player_1_card) and (len(player_2)>=player_2_card)):
            copy_1 = [player_1[i] for i in range(player_1_card)]
            copy_2 = [player_2[i] for i in range(player_2_card)]
            player_1_wins = ("player1" == war(copy_1, copy_2)) #Recurses the code with a second game and a boolean with the parsed copies. 
            
            #This part of the code makes my blood boil. Initially, I thought the problem meant add the
            #ENTIRE rest of the list to the recursive game, not the amount specified by the card.
            #I lost an hour because of that. The test cases didn't indicate anything wrong initially either.

            #Whoever made that rule... I want to talk to you with this bat to your kneecaps and your weak collarbones.
        else:
        '''
        player_1_wins = player_1_card>player_2_card #Boolean true if greater, false if less. Executes in Part 2 if not recursed.
        
        if player_1_wins:
            player_1 += [player_1_card, player_2_card] #Adds it back to player_1's deck in the order specified.
            winner = "player1"
        else:
            player_2 += [player_2_card, player_1_card] #Adds it back to player_2's deck in the order specified.
            winner = "player2"

    return winner

winner = war(player1, player2)
total = 0
if winner == "player1":
    for ind, i in enumerate(player1):
        mult = len(player1) - ind #This reverses the multiplier accordingly, since the increment starts at the end of the list
        total += mult*i
else:
    for ind, i in enumerate(player2):
        mult = len(player2) - ind
        total += mult*i
print(total) #Part 1 should be 31754 with my data, Part 2 should be 35436
    
