#Conway Cubes, in 4 dimensions! (AOC Day 17 Part 2)
#Keshav V.
#Note: This one will be sparse of comments, because I detailed everything in excruciating detail on Day17-1.py. Read that first, then come here.

def get_4d_neighbors(mat, hyp, dep, row, col):
    available_neighbors = []

    H = len(mat) #This is max hyperlength, an extension of get_3d_neighbors from Part 1
    D = len(mat[0])
    R = len(mat[0][0])
    C = len(mat[0][0][0])

    for h in range(hyp - 1, hyp + 2):
        for d in range(dep - 1, dep + 2):
            for r in range (row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if (d == dep) and (r == row) and (c == col) and (h == hyp):
                        continue
                    if (0 <= r < R) and (0 <= c < C) and (0 <= d < D) and (0 <= h < H):
                        available_neighbors.append(mat[h][d][r][c])

    return available_neighbors

def layer_it_on_4d(mat): #Extension of new layer_it function to 4D from Part 1
    new = []

    H = len(mat)
    D = len(mat[0])
    R = len(mat[0][0])
    C = len(mat[0][0][0])
    for h in range(-1,H+1):
        to_add = []
        for d in range(-1,D+1):
            add_to_vol = []
            for r in range(-1,R+1):
                add_to_layer = []
                for c in range(-1,C+1):
                    if (0 <= r < R) and (0 <= c < C) and (0 <= d < D) and (0 <= h < H):
                        add_to_layer.append(mat[h][d][r][c])
                    else:
                        add_to_layer.append('.')
                add_to_vol.append(add_to_layer)
            to_add.append(add_to_vol)
        new.append(to_add)

    return new


with open("Day_17_input.txt","r") as f:
    hypercubes = [] #I should've called the array 'tesseracts,' but too late now.
    for line in f:
        hypercubes.append(line.rstrip("\n"))

hypercubes = [[[list(i) for i in hypercubes]]] #Triple brackets to confer that it is a 4D hypermatrix.
hypercubes = layer_it_on_4d(hypercubes)

for cycle in range(6): #Mostly generalizations and extensions using an extra for loop from Day 17-1.py. 
    next_iteration = []
    for hyp in range(len(hypercubes)):
        to_add = []
        for dep in range(len(hypercubes[hyp])):
            add_to_vol = []
            for row in range(len(hypercubes[hyp][dep])):
                add_to_layer = []
                for col in range(len(hypercubes[hyp][dep][row])):
                    add_to_layer.append(0)
                add_to_vol.append(add_to_layer)
            to_add.append(add_to_vol)
        next_iteration.append(to_add)

    for hyp in range(len(hypercubes)):
        for dep in range(len(hypercubes[hyp])):
            for row in range(len(hypercubes[hyp][dep])):
                for col in range(len(hypercubes[hyp][dep][row])):
                    data = get_4d_neighbors(hypercubes,hyp,dep,row,col)
                    live_cells = data.count("#")

                    if (2 <= live_cells <= 3) and (hypercubes[hyp][dep][row][col] == "#"):
                        next_iteration[hyp][dep][row][col] = "#"
                        continue
                    else:
                        next_iteration[hyp][dep][row][col] = "."
                    

                    if (live_cells == 3) and (hypercubes[hyp][dep][row][col] == "."):
                        next_iteration[hyp][dep][row][col] = "#"
                        continue
                    else:
                        next_iteration[hyp][dep][row][col] = "."

    hypercubes = layer_it_on_4d(next_iteration)

hash_count = 0
for i in next_iteration:
    for j in i:
        for k in j:
            for l in k:
                if l == "#":
                    hash_count += 1
print(hash_count) #Should get 1892 live cells from my data.
                    
#I now have a renewed vigor for this competition after the crisis of today.
#Let's continue solving coding problems together!