#Rambunctious Recitation (AOC Day 15)
#Keshav V.

order = [0,5,4,1,10,14,7] #My input, for the first time NOT IN A SEPARATE FILE!
index = 6 #Current number to analyze

first_occurences = {} #The latest occurance of a number and where it is.

for ind, i in enumerate(order):
    first_occurences[i] = ind #Takes in occurences of numbers in input already

while len(order) != 2020: #Put in 2020 for Part 1, replace with 30,000,000 for Part 2.
    num = order[index] #Takes in current number

    if num in first_occurences:
        order.append(index - first_occurences[num])
        first_occurences[num] = index
        index += 1
        continue
        #If the num has occured before, finds it and puts in proper next number.

    order.append(0)
    first_occurences[num] = index
    index += 1
    #If number hasn't occured before, outputs 0, sets 0 to new index, and goes to next number


print(order[-1])
#Should get 203 for Part 1, 9007186 for Part 2.

    
    
