#Password Philosophy (AOC Day 2)
#Keshav V.
#Note: all input files and programs are assumed to be in the same CWD

#Part 1
count = 0
with open("Day_2_input.txt","r") as file:
    for line in file:
        info = line.split(" ")
        info[1] = info[1][0] #Some parsing to make coding easier, removing the colon and making it into a list

        char_count = 0
        for i in info[2]:
            if i == info[1]:
                char_count += 1 #Simple loop to find/count instances of a character. Can use .count() here.

        limits = info[0].split("-")

        if int(limits[0]) <= char_count <= int(limits[1]): #Testing to see if the password is within bounds
            count += 1
print(count) #Should give 418

#Part 2
count = 0 #Reset count to 0 for purposes of this demonstration.
with open("Day_2_input.txt","r") as file:
    for line in file:
        info = line.split(" ")
        info[1] = info[1][0]

        limits = info[0].split("-")
        
        index_1 = int(limits[0])-1 #Zero index correction
        index_2 = int(limits[1])-1
        
        A = (info[2][index_1] == info[1]) #A and B are either true or false
        B = (info[2][index_2] == info[1]) #Sees if characters match

        if ((not A) and B) or (A and (not B)): #XOR gate, as only 1 match is allowed
            count += 1

print(count) #Should get 616

        
