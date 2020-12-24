#Lobby Layout (AOC Day 24 Part 1)
#Keshav V.
#I had a lot of fun with this one. This was awesome, especially since I got to use LINEAR ALGEBRA IN PART 2! Stay tuned to find out how ;)
with open("Day_24_input.txt","r") as f:
    unparsed = []
    for line in f:
        unparsed.append(line.rstrip("\n")) #We haven't seen this in a while! Although tbh, the parsing block below could've easily been integrated here.

parsed = []
northflag = False #To parse the instructions without delimiters, we create our own that becomes true if we encounter 'n' or 's,' as it tells us that this character alone isn't the complete direction.
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
            to_add = "" #Adds two-character direction to parsed and resets to_add for next instruction

        elif (char == "e" or char == "w") and not northflag:
            to_add += char
            inst.append(to_add)
            to_add = "" #Mainly to be consistent and to catch explicit 'e' or 'w' instructions.
    parsed.append(inst) #Parsed one line. Add it and move on to the next.

flipped = [] #Contains the coordinates of the centers of the hexagons that are black. Strange to call it 'flipped' here, but it's called 'black' in part 2, so no worries.
for inst in parsed:
    coordinates = [0,0] #x,y coordinates
    for j in inst:
        if j == "w":
            coordinates[0] -= 1 #Distance from centers of hexagons on right and left directly are defined as one.
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
            coordinates[1] -= 0.5 
            #I am aware that the y coordinate isn't *quite* accurate in the last 4 here, but you can view each tile as a squashed hexagon with a center that follows these coordinates.
            #The math is the same either way, so there is no worry.
    if coordinates in flipped:
        flipped.remove(coordinates) #If the hexagon is already flipped, we remove it, as it flips back to black *AC/DC riff starts*
    else:
        flipped.append(coordinates) #Otherwise, it flips to black and it hits the sa- I mean gets added to flipped.

print(len(flipped)) #Should get 320 from my input.
