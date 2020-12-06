#Binary Boarding (AOC Day 5)
#Keshav V.

'''
Note: This one was a fun one! Mostly because this is a roundabout creative solution
They definitely intended for this to be the way to solve it.
It's just too perfect.

Basically, since the seats are numbered from 0-127 ascending and 0-7 ascending for the seats,
You can treat them as binary numbers, since taking the upper half/lower half is like adding
a binary 1 versus a binary 0 to decimal. It is equivalent, and ill let you do the mental gymnastics

Ex: FBFBBFFRLR --> 0101100 101 --> Row 44 Col 5
And so, with this idea:
'''

#Part 1
ids = [] #Holds the ids of the chairs
with open("Day_5_input.txt","r") as f:
    for line in f:
        row = ""
        col = ""
        for i in line:
            if i == "F":
                row += "0" #A seat in the fronter end is smaller
            elif i == "B":
                row += "1" #A seat in the back end is bigger, and is bigger than half the search size

            elif i == "R":
                col += "1"
            elif i == "L":
                col += "0" #Same principle

        dec_row = int(row, 2)
        dec_col = int(col, 2)#Conversion from binary to decimal

        seat_id =8*dec_row + dec_col
        ids.append(seat_id)

print(max(ids)) #Should be 935 with my input

#Part 2
seats = [i for i in range(min(ids),max(ids)+1)]
for i in seats:
    if i not in ids: #Looks for the missing number in seats, your seat id.
        print(i)
        break
#You should get 743 printed

#Fun Fact: This part 2 code was not necessary for me.
#I solved it by visual inspection of sorted(ids) and finding the missing number.
#Bad, Keshav, bad!
#for the edge. The code above shows how I should've done it.
