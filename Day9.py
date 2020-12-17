#Encoding Error (AOC Day 9)
#Keshav V.

with open("Day_9_input.txt","r") as f:
    numbers = []
    for line in f:
        numbers.append(int(line.rstrip("\n"))) #Introducing the int() to the parsing!

#Part 1
found_match = False #This is mainly to prevent multiple matches by identifying a proper sum
for i in range(25,len(numbers)):
    search = numbers[i-25:i] #Previous 25 numbers to search through
    for j in search:
        if ((numbers[i]-j) in search):
            found_match = True #Identifies that there is a valid sum, breaks out and goes to next loop
            break
        
    if found_match == True:
        found_match = False
        continue
    else:
        print(numbers[i]) #If no sum was found, then that is our weak number.
        #Should get 15690279 from this input.
        break

#Part 2
starting_index = -1 #Determines the place to start the summing.
while True:
    starting_index += 1 #If the previous loop failed, then the next starting num in the continguous stretch is the one after the previous number attempted.
    total = 0 #Keeps track of sum of continuous numbers in this sequence.
    nums = [] #Keeps numbers in sum tracked.
    
    for i in range(starting_index, len(numbers)):
        total += numbers[i]
        nums.append(numbers[i])
        if total >= 15690279:
            #If our number exceeds or meets the required total, 15690279 (might be different for you), we exit.
            #No need to add any further. We've either met or exceeded 15690279.
            break

    if total == 15690279: #If our sum is found, we are done and exit. If not...
        break #We start back at the beginning with a new starting point after the one we tested, total reset to zero, and nums empty.

print(min(nums)+max(nums))#The max and min numbers in the range for me were 769435 and 1404797 for a total answer of 2174232
