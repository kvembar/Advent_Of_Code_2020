#Lobby Layout (AOC Day 24 Part 2)
#Keshav V.
#This is my part 2 solution to Day 24 featuring linear algebra! Go to my part 1 solution for more.

with open("Day_24_input.txt","r") as f:
    unparsed = []
    for line in f:
        unparsed.append(line.rstrip("\n"))

parsed = []
northflag = False
for i in unparsed:
    to_add = ""
    inst = []
    for char in i:

        if (char == "n" or char == "s"):
            northflag = True
            to_add += char

        elif (char == "e" or char == "w") and northflag:
            to_add += char
            northflag = False
            inst.append(to_add)
            to_add = ""

        elif (char == "e" or char == "w") and not northflag:
            to_add += char
            inst.append(to_add)
            to_add = ""
    parsed.append(inst)

def linalg(inst): #I was rather excited to use LA here.
    coordinates = [0,0]
    for j in inst:
        if j == "w":
            coordinates[0] -= 1
        elif j == "e":
            coordinates[0] += 1
        elif j == "nw":
            coordinates[0] -= 0.5
            coordinates[1] += 0.5
        elif j == "ne":
            coordinates[0] += 0.5
            coordinates[1] += 0.5
        elif j == "sw":
            coordinates[0] -= 0.5
            coordinates[1] -= 0.5
        elif j == "se":
            coordinates[0] += 0.5
            coordinates[1] -= 0.5 #Same coordinates from part 1, but this time...

    lin_combo = [0,0] 
    #We will name our hexagon's location based entirely on the linear combination of u1 and u2. The array above contains the scalar multipliers in the linear combination.
    #u1 is [1,0] and u2 is [0.5,0.5].These linearly independent vectors guarantee a unique name for each hexagon. u1 is like going 'ne' and u2 is like going 'e.'
    #All other directions and thus the neighbors can be expressed as a linear combination of these two vectors.

    lin_combo[0] = int(coordinates[0] - coordinates[1])
    lin_combo[1] = int(coordinates[1]*2)

    #The formulae above for the scalar multiples are derived via row reduction
    #The proof is left as an exercise to the reader. (Yeah, I just went there. Do your own dang row reductions. It's not even a hard one.)

    return lin_combo

black = [] #Replacement name for 'flipped' from Part 1. Same purpose. Stores which tiles are flipped and black

for i in parsed:
    basis = linalg(i)
    if basis in black:
        black.remove(basis)
    else:
        black.append(basis)

for day in range(100): #Execute this 100 times. Takes a while, but thankfully not as long as Day 23.
    neighbors = [i for i in black] #This will store all of the tiles and their neighbors for analysis on flippage.
    for i in black:
        u1 = i[0]
        u2 = i[1]
        poss = [[u1+1,u2],[u1-1,u2],[u1,u2+1],[u1,u2-1],[u1-1,u2+1],[u1+1,u2-1]] #These are the 6 neighbors of the hexagon expressed as their linear combos from earlier. 
        #See Example.pdf for visual example. I know I don't quite use a hashmap here, but it's even better: just analyzing the neighbors instead of the whole field.
        for j in poss:
            if j not in neighbors:
                neighbors.append(j) #Add to neighbors if not in there. Could use a dict in place of this, but arrays are easier to work with.

    iteration = [] #Contains the neighbors that stay black after applying the rules and is therefore the next 'iteration' of 'black'
    for i in neighbors:
        u1 = i[0]
        u2 = i[1]
        black_side_up = (i in black) #Is the tile black side up?
        poss = [[u1+1,u2],[u1-1,u2],[u1,u2+1],[u1,u2-1],[u1-1,u2+1],[u1+1,u2-1]] #Same neighbors as before.
        live = 0
        for j in poss:
            if j in black:
                live += 1
        
        if (live == 0 or live>2) and (black_side_up):
            continue
        elif (live != 2) and (not black_side_up):
            continue #If it does not flip to black, do not add it to iteration and just go to the next neighbor
        iteration.append(i) #Otherwise, add it.
    print(f"day {day+1}:{len(iteration)}") #When the program finishes executing, take day 100s answer. Should get a nice and lucky 3777. It's a slow program, true, but it gives the answer reliably!
    black = iteration #Sets black to the iteration for next cycle.