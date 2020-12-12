#Rain Risk (AOC Day 12)
#Keshav V.

with open("Day_12_input.txt","r") as f:
    directions = []
    for line in f:
        directions.append(line.rstrip("\n"))

#Part 1
current = [0,0] #x,y coordinates of ship
current_direction = "E" #The direction that the ship was facing
for i in directions:
    direction = i[0]
    val = int(i[1:])

    if direction == "F":
        direction = current_direction #Saves direction as current direction the ship is facing for next conditional.

    if direction == "N":
        current[1] += val
    elif direction == "E":
        current[0] += val
    elif direction == "S":
        current[1] -= val
    elif direction == "W":
        current[0] -= val
    #This bit of code is self-explanatory. Changes direction and stuff like that.

    shift = ["N","E","S","W"] #Cardinal directions. One shift up an index is the same as turning right and one shift down an index is the same as turning left.

    if direction == "L":
        ind = shift.index(current_direction) #Find current direction in index
        current_direction = shift[(ind-(val//90))%4] #Does as many equivalent turns in 'shift' as 90 degree turns left. Saves it as new ship direction
    elif direction == "R":
        ind = shift.index(current_direction)
        current_direction = shift[(ind+(val//90))%4]

print(current) #For my input, I got my co-ordinates as [198, -121], with manhattan distance 319.

#Part 2
current = [0,0] #Coordinates of ship reset for demonstration
waypoint = [10,1] #Waypoint relative to the ship.

for i in directions:
    direction = i[0]
    val = int(i[1:])

    if direction == "F":
        current[0] += waypoint[0] * val #Changing ship location to x times number of times you go to waypoint.
        current[1] += waypoint[1] * val
    
    if direction == "N":
        waypoint[1] += val
    if direction == "E":
        waypoint[0] += val
    if direction == "S":
        waypoint[1] -= val
    if direction == "W":
        waypoint[0] -= val
    #Copy-pasted code shifting the waypoint.
    
    if direction == "L" or direction == "R":
        if direction == "R":
            val = 360 - val #Prevents coding an extra case dealing with R by giving an equivalent L.
        for i in range(val//90):
            z = waypoint[0]
            waypoint[0] = -waypoint[1]
            waypoint[1] = z
            #Swapping x and y and negating the x term. That is how you do a 90 degree rotation left. Simply repeat for every 90 degree left turn!

print(current) #For my input, I got my co-ordinates as [-10398, 39219], with manhattan distance 50157.
