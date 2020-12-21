#Jurassic Jigsaw Part 1 (AOC Day 20)
#Keshav V.
#Note: I couldn't solve Part 2. I suck too much at coding to do it. I'm sorry.
#This is a very cheesed solution that cheats a bit.

with open("Day_20_input.txt","r") as f:
    pieces = {}
    name = 0
    data = []
    for line in f:
        if line[0] == "T":
            name = int(line[5:-2])

        elif line[0] == "." or line[0] == "#":
            data.append(line.rstrip("\n"))

        elif line == "\n":
            pieces[name] = data
            name = 0
            data = []

def get_8_sides(block): #This function's name is self-explanatory. Gets all 4 sides and their reverses.
    sides = [block[0], block[-1], block[0][::-1], block[-1][::-1]] #Top and bottom and reversed top and bottom
    transpose = list(map(list, zip(*block)))
    sides += ["".join(transpose[0]), "".join(transpose[-1]), "".join(transpose[0][::-1]), "".join(transpose[-1][::-1])] #Left and right side and reversed left and right.
    return sides

prod = 1
adjacencies = {} #Also a carryover from an attempt at Part 2.
orient = ['T','B','RT','RB','L','R','RL','RR'] #A carryover from an attempt at Part 2 that wasn't cheesed.

for ID in pieces.keys():
    puzzle = pieces[ID] #Gets the puzzle piece associated with it.
    edges = get_8_sides(puzzle)
    shared = 0
    adjacent = [] #Carryover.
    
    for checker in pieces.keys():
        if checker == ID:
            continue
        edges_to_check = get_8_sides(pieces[checker])
        
        for i in edges:
            if (i in edges_to_check):
                shared += 1 #If the two pieces share a side, we add 1 to the number of shared sides it has.
                b = edges.index(i) 
                c = edges_to_check.index(i)
                adjacent += [orient[b], orient[c], checker] #Carryover lines.
                break
    
    if shared == 2:
        prod *= ID #If they share only 2 sides with 2 other pieces, congratulations, you found a corner piece. Multiply it right to the total
    adjacencies[ID] = adjacent
        
print(prod) #Should get 8425574315321 from my input.