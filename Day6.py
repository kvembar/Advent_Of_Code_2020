#Custom Customs (AOC Day 6)
#Keshav V.

with open("Day_6_input.txt","r") as f:
    questions = []
    for line in f:
        questions.append(line.rstrip("\n"))
    questions.append("") #See Day 4 for why this is here.

#Part 1:
sums = [] #This array contains the number of unique answers per batch. (E.g. First batch has 3 unique answers, 2nd has 1, so it would be 3,1,...)
unique_answers = []#Temporary array to contain the answers

for i in questions:
    if i == "": #Once again using the newline as a bumper between batches
        sums.append(len(unique_answers)) #Takes unique answers in the batch and adds them to sums
        unique_answers = [] #Reinitialize for next batch
        continue
    
    for j in i:
        if j not in unique_answers:
            unique_answers.append(j) #Simple sift of unique characters

print(sum(sums))#Should get 7027

#Part 2
sums = []
shared_answers = [] #Now contains the number of shared answers per batch
traceFlag = True #This flag tracks when a new batch has arrived

for i in questions:
    if i == "":
        sums.append(len(shared_answers))
        shared_answers = []
        traceFlag = True
        continue
    
    if traceFlag == True:
        for j in i:
            shared_answers.append(j) #Puts all characters in shared_answers
            #Since for answer to be shared by all, it must be shared by the first.
        traceFlag = False #Possible shared answers recorded, then moves onto else statement for rest of batch

    else:
        shitlist = [] #Tracks letters to be removed from shared_answers
        #This is to circumvent the removal of characters from a list i'm iterating through
        for j in shared_answers:
            if j not in i:
                shitlist.append(j) #If the shared character is not in the answers for a person, it is to be removed as it isn't shared by everyone.
        for j in shitlist:
            shared_answers.remove(j)
    

print(sum(sums))#Should get 3579

        
