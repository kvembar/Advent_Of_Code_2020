#(AOC Day 22)

with open("Day_22_input.txt","r") as f:
     player1 = []
     player2 = []
     mode = "1"
     first = True
     for line in f:
         if first == True:
             first = False
             continue
        
         if line == "\n":
             mode = "2"
             first = True
             continue

         if mode == "1":
             player1.append(int(line.rstrip("\n")))

         if mode == "2":
             player2.append(int(line.rstrip("\n")))

def war(my_deck, crabs):
    decks_plaid = set()
    while True:
        #print(f"current hand: {my_deck}, {crabs}\n")
        if my_deck == []:
            #print("player 1 ran out of cards\n")
            winner = "player2"
            break

        elif crabs == []:
            #print("player2 ran out of cards\n")
            winner = "player1"
            break
        
        if (tuple(my_deck), tuple(crabs)) in decks_plaid:
            #print(f"current hand: {my_deck}, {crabs}\n")
            #print(f"current deck has appeared before in {decks_plaid}")
            winner = "player1"
            break
        else:
            decks_plaid.add((tuple(my_deck), tuple(crabs)))
        
        my_card = my_deck.pop(0)
        crab_card = crabs.pop(0)

        if ((len(my_deck)>=my_card) and (len(crabs)>=crab_card)):
            #print(f"Recursion entered: {my_card}, {crab_card}\n")
            player_1_wins = ("player1" == war([i for i in my_deck], [i for i in crabs]))
        else:
            player_1_wins = my_card>crab_card
            #print(f"Did player 1 win: {player_1_wins}\n")
        
        if player_1_wins:
            my_deck += [my_card, crab_card]
            winner = "player1"
        else:
            crabs += [crab_card, my_card]
            winner = "player2"

    return winner

winner = war(player1, player2)
total = 0
if winner == "player1":
    for ind, i in enumerate(player1):
        mult = len(player1) - ind
        total += mult*i
else:
    for ind, i in enumerate(player2):
        mult = len(player2) - ind
        total += mult*i
print(total)
    
