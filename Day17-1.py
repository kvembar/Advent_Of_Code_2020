#Conway Cubes(AOC Day 17 Part 1)
#Keshav V.
#Note: This one was rough. So rough that I literally needed to vent to the Mines AoC chat about how I sucked at coding when I saw Part 2 and exploded.
#This file is a solution to Part 1. When I saw Part 2, I was so angry and frustrated at myself that I decided I needed to start all over from scratch;
#And write a new file for Part 2. What resulted was an improved version of the layer_it function that didn't need an intuitive understanding of 4D.
#I've included both versions here for academic purposes.

#Featuring the newest and latest appearance of FUNCTIONS!

def get_3d_neighbors(array, dep, row, col): #I learned my lesson on Day 11. A whole function just for getting the neighbors of a (3d) multidimensional matrix.
    availableneighbors = []

    D = len(array) #Max value depth, row, and col can be.
    R = len(array[0])
    C = len(array[0][0])
    #Assuming of course, the array isn't jagged. But that is a relatively easy fix.

    for d in range(dep - 1, dep + 2):
        for r in range (row - 1, row + 2):
            for c in range(col - 1, col + 2): #Checks all depths, rows, and columns around the 3d matrix one away from the point whose neighbors we are getting.
                if (d == dep) and (r == row) and (c == col):
                    continue #No need to have the point itself be a neighbor. Will mess up some stuff.
                if (0 <= r < R) and (0 <= c < C) and (0 <= d < D):
                    availableneighbors.append(array[d][r][c]) #If our point is within bounds, it'll be added. Inspired by a Stack Exchange post. Don't act like you don't use it too.

    return availableneighbors

def layer_it_on_3d_old(array): 
    #This function's purpose was to add a 'layer' of cells around the 3d matrix
    #Live cells could convert cells outside the bounds of the 3d matrix (remember that the grid is infinite technically)
    #So adding a layer is absolutely necessary for analyzing it, as the most a certain point could convert is one unit outside of the current range in any of the xyz directions.
    #This is the old version that doesn't quite carry over to Part 2 unless you live in a 4th spatial dimension.

    D = len(array)
    R = len(array[0])
    C = len(array[0][0]) #Again, the max ranges

    new_z_layers = [['.' for i in range(C+2)] for j in range(R+2)] #Caps off the new layer's top and bottom with an overhang of 2, one on the left, one on the right.

    for d in range(D):
        for r in range(-1,R+1):
            if r == -1:
                array[d] = [['.' for i in range(C+2)]] + array[d] 
                continue
            if r == 0:
                continue
            elif r == R:
                array[d] += [['.' for i in range(C+2)]]
                
            array[d][r] = ['.'] + array[d][r] + ['.'] #Lines 43, 48, and 50 serve to 'wrap' around the sides of the 3d matrix with the empty, dead cells.

    return [new_z_layers]+array+[new_z_layers] #Combines the caps and wraps to form the new layer.
    #You can probably see why it would be an issue in 4D for Part 2, because you can't easily imagine how a tesseract would structure their wraps, caps, taps, and laps
    #Imagining this function's transition to 4D what made me explode in the AoC chat. But... there is a better way.


def layer_it_on_3d(mat): #And here it is. This one is original, no reference this time.
    new = []

    D = len(mat)
    R = len(mat[0])
    C = len(mat[0][0])

    for d in range(-1,D+1): 
        add_to_vol = []
        for r in range(-1,R+1):
            add_to_layer = []
            for c in range(-1,C+1):
                if (0 <= r < R) and (0 <= c < C) and (0 <= d < D):
                    add_to_layer.append(mat[d][r][c])
                else:
                    add_to_layer.append('.')
            add_to_vol.append(add_to_layer)
        new.append(add_to_vol)
    
    #This time, we generate a copy of the 3d matrix, but with extra stuff. 
    #Specifically, we are iterating three variables: row, column, and depth such that they stay mostly in bounds, and thus output the 3d matrix at that point, with two exceptions:
    #The first and last values they go through stray outside of the matrix at -1 and D/R/C. When those values occur, we are on a side of the new layer somewhere
    #And so, the else statement kicks in and we put a dead cell in the row. 
    #Each row is collected in the add_to_layer, and then each layer is added to add_to_vol when a layer has finished iterating through.
    #This creates a new matrix that has one extra layer added to each side. And it easily generalizes to 4D with an extra loop. See Day17-2.py.
        
    return new

with open("Day_17_input.txt","r") as f:
    cubes = []
    for line in f:
        cubes.append(line.rstrip("\n"))

cubes = [[list(i) for i in cubes]] #Double brackets make it a 3d matrix, as list(i) only has each row as it's own array.
cubes = layer_it_on_3d(cubes) #Adds an extra layer so that cells *just* outside the range can be considered.

for cycle in range(6):
    next_iteration = [] #Will keep the next state of the cubes.
    for depth in range(len(cubes)):
        to_add = []
        for row in range(len(cubes[depth])):
            add_to_layer = []
            for column in range(len(cubes[depth][row])):
                add_to_layer.append(0)
            to_add.append(add_to_layer)
        next_iteration.append(to_add)
    #^^The for loop above creates an identical copy of cubes, so that recording does not interfere with future edits.^^

    for depth in range(len(cubes)):
        for row in range(len(cubes[depth])):
            for column in range(len(cubes[depth][row])):
                data = get_3d_neighbors(cubes,depth,row,column)
                live_cells = data.count("#") #Counts number of live cells in neighbors

                if (2 <= live_cells <= 3) and (cubes[depth][row][column] == "#"):
                    next_iteration[depth][row][column] = "#"
                    continue
                else:
                    next_iteration[depth][row][column] = "."
                    

                if (live_cells == 3) and (cubes[depth][row][column] == "."):
                    next_iteration[depth][row][column] = "#"
                    continue
                else:
                    next_iteration[depth][row][column] = "."
                #Conway's Game of Life rules. Self-explanatory.
                    
    cubes = layer_it_on_3d(next_iteration) #Adds another layer to 'cubes' so that all possible coordinates that can be changed will be analyzed in the next cycle.

hash_count = 0
for i in next_iteration:
    for j in i:
        for k in j:
            if k == "#":
                hash_count += 1
print(hash_count) #Simple counter of #'s. Should get 426 from my data surprisingly quickly!
