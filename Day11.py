#Seating System (AOC Day 11)
#Keshav V.
#Note: This is by far the most inefficient way to simulate CAs ever.
#This program takes 7 seconds to execute both parts. This is why I am a terrible programmer.

with open("Day_11_input.txt","r") as f:
    seats = []
    for line in f:
        seats.append(line.rstrip("\n"))

edit = True

while edit == True:
    edit = False #Again, a flag used to edit. I probably should've just created a copy and then edit that copy.
    newarray = [] #LIKE HERE. IT WAS RIGHT THERE KESHAV. JFC.
    for row, rowval in enumerate(seats):
        newrow = "" #The edited new row.
        for col, val in enumerate(rowval):
            if val == ".":
                newrow += val
                continue
            else:
                counter = 0
                if row != 0:
                    if seats[row-1][col] == "#":
                        counter += 1
                    if col != 0:
                        if seats[row-1][col-1] == "#":
                            counter += 1
                    if col != len(rowval)-1:
                        if seats[row-1][col+1] == "#":
                            counter += 1

                if row != len(seats)-1:
                    if seats[row+1][col] == "#":
                        counter += 1
                    if col != 0:
                        if seats[row+1][col-1] == "#":
                            counter += 1
                    if col != len(rowval)-1:
                        if seats[row+1][col+1] == "#":
                            counter += 1

                if col != 0:
                    if seats[row][col-1] == "#":
                        counter += 1

                if col != len(rowval)-1:
                    if seats[row][col+1] == "#":
                        counter += 1

                #Everything seen above is what edits the list. Checks left, right, forward, backward, and everything in between.
                #Counter keeps track of number of occupied seats.
                if counter == 0 and val == "L":
                    newrow += "#"
                    edit = True
                elif counter >= 4 and val == "#":
                    newrow += "L"
                    edit = True
                else:
                    newrow += val
                
        newarray.append(newrow) #Adds the new row to the new seat arragement before resetting.
        
    seats = newarray #Makes seats into the next iteration

ans1 = 0
for i in seats:
    for j in i:
        if j == "#":
            ans1 += 1 #Simple counter of #s.

print(ans1) #Should get 2166 from my data.

#Part 2. I hated this one because I had 3 OBOEs that caused repeated errors.

with open("Day_11_input.txt","r") as f:
    seats = []
    for line in f:
        seats.append(line.rstrip("\n"))
        #Resetting seats to original for purposes of demonstration.

edit = True

while edit == True:
    edit = False
    newarray = []
    for row, rowval in enumerate(seats):
        newrow = ""
        for col, val in enumerate(rowval):
            if val == ".":
                newrow += val
                continue
            else:
                counter = 0
                reach = 1 #Reach is the distance away from the seat in a particular direction.

            if row != (len(seats)-1):
                while (row+reach != len(seats)-1) and (seats[row+reach][col] == "."):
                    reach += 1
                if seats[row+reach][col] == "#":
                    counter += 1
                reach = 1

            if (row != len(seats)-1) and (col != len(rowval)-1):
                while (row+reach != len(seats)-1) and (col+reach != len(rowval)-1) and (seats[row+reach][col+reach] == "."):
                    reach += 1
                if seats[row+reach][col+reach] == "#":
                    counter += 1
                reach = 1

            if (col != len(rowval)-1):
                while (col+reach != len(rowval)-1) and (seats[row][col+reach] == "."):
                    reach += 1
                if seats[row][col+reach] == "#":
                    counter += 1
                reach = 1

            if (row != 0) and (col != 0):
                while (row-reach != 0) and (col-reach != 0) and (seats[row-reach][col-reach] == "."):
                    reach += 1
                if seats[row-reach][col-reach] == "#":
                    counter += 1
                reach = 1

            if (row != 0):
                while (row-reach != 0) and (seats[row-reach][col] == "."):
                    reach += 1
                if seats[row-reach][col] == "#":
                    counter += 1
                reach = 1

            if col != 0:
                while (col-reach != 0) and (seats[row][col-reach] == "."):
                    reach += 1
                if seats[row][col-reach] == "#":
                    counter += 1
                reach = 1

            if (row != len(seats)-1) and (col != 0):
                while (row+reach != len(seats)-1) and (col-reach != 0) and (seats[row+reach][col-reach] == "."):
                    reach += 1
                if seats[row+reach][col-reach] == "#":
                    counter += 1
                reach = 1

            if (row != 0) and (col != len(rowval)-1):
                while (row-reach != 0) and (col+reach != len(rowval)-1) and (seats[row-reach][col+reach] == "."):
                    reach += 1
                if seats[row-reach][col+reach] == "#":
                    counter += 1
                reach = 1
            #There was probably a cleaner way to code all of this, and there is!
            #Instead of directly measuring the reach away for each point, I could just loop through NUMBERS than represent the distance rather than enumerate().
            #I'm just too lazy to do otherwise. I just needed the answer for this. Will probably improve later.
            
            if counter == 0 and val == "L":
                newrow += "#"
                edit = True
            elif counter >= 5 and val == "#":
                newrow += "L"
                edit = True
            else:
                newrow += val
        newarray.append(newrow)
    seats = newarray

ans1 = 0
for i in seats:
    for j in i:
        if j == "#":
            ans1 += 1

print(ans1) #Should get 1955 from my input.
