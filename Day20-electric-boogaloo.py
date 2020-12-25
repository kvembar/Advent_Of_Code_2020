#Jurassic Jigsaw Part 2 (AOC Day 20)
#Keshav V.
#Day 25 forced my hand to solve Part 2. I stayed up until 4 AM on Christmas Day to do it. But, it's ok.
#I have never felt more powerful in my LIFE!
#And with that, let's take a deep dive into the longest bit of code I've ever made in a while. 217 lines. Let's go.

with open("Day_20_input.txt","r") as f:
    pieces = {}
    name = 0
    data = []
    for line in f:
        if line[0] == "T":
            name = int(line[5:-2])

        elif line[0] == "." or line[0] == "#":
            data.append(line.rstrip("\n"))

        elif line == "\n": #I had to add two newlines to the Day 20 input so that it could catch the last puzzle piece. Caused issues later down the line.
            pieces[name] = data
            name = 0
            data = []

def get_8_sides(block): #This function's name is self-explanatory. Gets all 4 sides and their reverses.
    transpose = [["" for j in range(len(block[0]))] for i in range(len(block))]
    for r in range(len(block)):
        for c in range(len(block[r])):
            transpose[c][r] += block[r][c]
    transpose = ["".join(i) for i in transpose]
    sides = [block[0],block[-1],transpose[0],transpose[-1],block[0][::-1],block[-1][::-1],transpose[0][::-1],transpose[-1][::-1]]
    return sides

orient = ['T','B','L','R','TR','BR','LR','RR'] #This tells you the order of the 8 sides of the get_8_sides array. Top, bottom, left, right, and their reverses indicated by an R after the letter.

def displaymatrix(mat): #This function was for debugging purposes so that I could display the matrix in its true 2D form.
    for i in mat:
        print(i)
    return None

def flip(mat, axis): #Flips the matrix according to the x/y axis.
    new_mat = []
    if axis == "x":
        new_mat = [mat[i] for i in range(len(mat)-1,-1,-1)] #Inverts matrix so that top becomes bottom and vice versa, like flipping it relative to the x-axis.
        return new_mat #The line above had an OBOE that accidentally trimmed off the first row. Ended up with weird errors that were fixed with a simple change from a 0 to a -1.
    elif axis == "y":
        for i in mat:
            line = ""
            for j in i:
                line = j + line #Inverts each of the rows. Same as flipping the matrix on y-axis.
            new_mat.append(line)
        return new_mat
    else:
        return None #Just in case I decided to be a dumdum and type something wrong for flip's axis.

def rotate_90_right(mat): #Self explanatory name.
    new_mat = ["" for i in range(len(mat))]
    for r in range(len(mat)):
        for c in range(len(mat[r])):
            new_mat[c] += mat[r][c] #First column becomes first row, second column to second row in new_mat, etc.
    return flip(new_mat,"y") #Flipping it across y-axis then makes the first column of new_mat be the last row in mat and so forth, equivalent to a rotation right.

#Now with all of the relevant functions defined, we are ready to create the map.

seed = 2311 #Place an ID in your input here. I used 2311 for mine (as a carryover from the test case), but theoretically, any number from the input should work.
locations = {int(f"{seed}"):[0,0]} #Stores where the other IDs are relative to this seed ID.
just_added = [seed] #Will be added onto until all IDs have been analyzed. Not unlike Day 7 Part 1's 'better' solution for tracking the bags!

for piece in just_added:
    image = pieces[piece]
    edges = get_8_sides(image)

    coordinates = locations[piece]
    x = coordinates[0]
    y = coordinates[1] #Gets the location of the piece we are analyzing. (again, the coordinates are relative to the seed we provide it.)

    for match in pieces.keys():
        if match in just_added:
            continue #If the key we are looking at is in just_added, it means we already analyzed it and found it's neighbours. No need to analyze it twice.

        edges_of_match = get_8_sides(pieces[match])

        for i in edges:
            if i in edges_of_match: #This conditional is the meat of the coordinate system. It only executes if we find out that two of the edges can line up. This is that 'lining up' process.
                side = edges.index(i) #This is the side that the match's tile going to be lined up to.

                while edges_of_match[side] != edges[side]:
                    pieces[match] = rotate_90_right(pieces[match])

                    edges_of_match = get_8_sides(pieces[match])

                    if edges_of_match[side] == edges[side][::-1]:
                        if orient[side] in ['T','B']:
                            pieces[match] = flip(pieces[match],"y")
                        elif orient[side] in ['R','L']:
                            pieces[match] = flip(pieces[match],"x")
                    #This while loop rotates and flips the piece until the sides match up. As in, L of the piece is the same as the L of the match, etc.
                    #Mainly a set up for the next block below. If I know that the edges that are supposed to line up are on the same side and same orientation, I can rotate it twice and flip it.
                    #bada bing, bada boom.

                pieces[match] = rotate_90_right(pieces[match])
                pieces[match] = rotate_90_right(pieces[match])
                if orient[side] in ['T','B']:
                    pieces[match] = flip(pieces[match],"y")
                elif orient[side] in ['R','L']:
                    pieces[match] = flip(pieces[match],"x")
                #This block of code orients the piece so that they line up properly. i.e. the L of the piece becomes the R of the match. Opposite sides line up now.
                #Now the pieces are oriented properly, but they will not match up in their own 2D matrix until a bit later.

                if orient[side] == "L":
                    locations[match] = [x-1,y]
                elif orient[side] == "R":
                    locations[match] = [x+1,y]
                elif orient[side] == "B":
                    locations[match] = [x,y-1]
                elif orient[side] == "T":
                    locations[match] = [x,y+1]
                #coordinates of match have been added to locations.
                just_added.append(match) #That piece you added is the next thing to analyze. Add it to just_added (thus the name).
                break

coordinates = [i for i in locations.values()] #Extracts just the coordinates
to_add_x = min(coordinates, key = lambda k:k[0])[0]
to_add_y = min(coordinates, key = lambda k:k[1])[1]

for ids in locations.keys():
    locations[ids][0] -= to_add_x
    locations[ids][1] -= to_add_y
    #Gets rid of any negatives and normalizes the grid so that the bottom left corner of the grid is always 0,0.

generate_x = max(coordinates, key = lambda k:k[0])[0]
generate_y = max(coordinates, key = lambda k:k[1])[1]

grid_ids = [[0 for i in range(generate_x+1)] for j in range(generate_y+1)] #Will store the IDs of the pieces in the grid
actual_matrices = [[0 for i in range(generate_x+1)] for j in range(generate_y+1)] #Will store the actual, properly oriented matrices into the grid.

def mat_strip(mat): #Strips the outer layer of the matrix
    new_mat = []
    R = len(mat)-1
    for r in range(len(mat)):
        C = len(mat[r])-1
        line = ""
        for c in range(len(mat[r])):
            if r in [0,R] or c in [0,C]:
                continue #we ignore the entries if they're on the boundary, i.e. have index 0 or index -1.
            line += mat[r][c]
        if line != "":
            new_mat.append(line)

    return new_mat

for ids, coord in locations.items():
    grid_ids[coord[1]][coord[0]] = ids
    actual_matrices[coord[1]][coord[0]] = mat_strip(pieces[ids]) #Constructs grid_ids and actual_matrices to specification.

def combine_x(mat1,mat2): #Combines the matrices mat1 and mat2 into a super-matrix in the x direction
    new = []
    for i in range(len(mat2)):
        new.append(mat1[i]+mat2[i])
    return new

def combine_y(mat1,mat2): #Same as combine_x but in the y direction. Will serve to stitch actual_matrices into a super-grid.
    new = []
    for i in mat1:
        new.append(i)
    for i in mat2:
        new.append(i)
    return new

firstlevel = []
for rowmatrix in actual_matrices:
    to_add = ["" for i in range(10)]
    for colmatrix in rowmatrix:
        #print(to_add,colmatrix)
        to_add = combine_x(to_add,colmatrix)
    firstlevel.append(to_add) #Stitches all the matrices on the same row to each other and adds them to firstlevel


secondlevel = []
for rowmatrix in firstlevel:
    secondlevel = combine_y(rowmatrix,secondlevel) #Stitches all the mega-matrices in firstlevel to each other in the y direction.
    #The order is due to the fact that the first entry in firstlevel describes the lowest part of the map, so it needs to be reversed.

#Congratulations! We have now constructed the map! Time to look for our ol' pal the loch ness monster.

marker = []
with open("Monster20.txt","r") as f: #First and only appearance of TWO files being imported! It is just WAAAAY easier to do it this way, trust me.
    for line in f:
        a = line.split(",")
        marker.append([int(a[0]),int(a[1])])
    #In the Monster20.txt file is a comma-delimited list of numbers. These numbers describe the monster's shape relative to a 'marker' at the top left of the monster.
    #Below is the monster, and the 'X' is the marker that the list is describing it with reference to. For example, the first hash below the X is described with 1,0.
    #And the hash to its bottom right is described as 2,1, as it is two rows down and one column right from X.
    '''
        X                 # 
        #    ##    ##    ###
         #  #  #  #  #  #   
    '''

def sea_monster_count(mat): #Where the magic happens
    monsters = 0

    for r in range(len(mat)):
        for c in range(len(mat[r])):
            
            try: #The program will try to grab all of the relevant tiles needed to check for a sea monster. If it goes out of bounds, it will throw an error, thus the try-except block.
                hashes = [mat[r+i][c+j] for i,j in marker]
                if "." in hashes: #If there is a "." in the hashes, we haven't found a sea monster (needs to be all hashes) and we continue.
                    continue
                else:
                    monsters += 1 #Otherwise, we found a sea monster! Increment that counter!

            except:
                continue

    return monsters
    #tbh, I expected that finding nessie would be the hard part of the coding, but it was actually the easiest! How strange coding is sometimes.
    #The hard part was actually making the dang map!

final_count = []
final_count.append(sea_monster_count(secondlevel))
for i in range(3):
    secondlevel = rotate_90_right(secondlevel)
    final_count.append(sea_monster_count(secondlevel))
secondlevel = flip(secondlevel, "x")
final_count.append(sea_monster_count(secondlevel))
for i in range(4):
    secondlevel = rotate_90_right(secondlevel)
    final_count.append(sea_monster_count(secondlevel))
#This block runs through all 8 possible arrangements of the map, contained in secondlevel: the map itself, then rotated 3 times, flipped, then rotated 4 times. (b/c of accounting for reversal of direction.)
#Checks for Nessie in all 8 and stores the count in final_count

monster_number = max(final_count) #We want to maximize the monster_count to find the correct arrangment that has the sea monsters in it.
hash_count = 0
for i in secondlevel:
    for j in i:
        if j == "#":
            hash_count += 1

print(hash_count - 15*monster_number) #There are, in fact, 24 nessies on the map for a total of 1841 hashes that are not part of a sea monster.
#15 hashes make up the sea monster, thus the subtract by 15*monster_number.

#I feel powerful that I got this right after so much pain, so much trial and error, so many prints of matrices that got fusterclarked.
#Five distinct and LONG versions of the code led to this, people! If I could solve this problem, what's stopping you from that thing you gave up on?!