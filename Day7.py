#Handy Haversacks (AOC Day 7)
#Keshav V.
#This one took forever, but I DID IT. THAT'S WHAT'S IMPORTANT.

#Part 1
added_flag = True #This variable keeps track of if a new bag as been added (and thus more to analyze)
#There is a much better way to do this. Just add to possible_bags and iterate through it. It'll end when there's no more.
#I was trying to rush it and the result is spaghetti. Take notes kids.

possible_bags = ["shiny gold bag"]

with open("Day_7_input.txt","r") as f:
    for line in f:
        analyze = line.split(" contain ") #Splitting the line based on the bag and what it contains
        if "shiny gold" in analyze[1]:
            possible_bags.append(analyze[0].rstrip("s"))#Removes plural to keep data clean.


while added_flag == True:
    added_flag = False
    with open("Day_7_input.txt","r") as f:
        for line in f:
            analyze = line.split(" contain ")
            for i in possible_bags:
                if (i in analyze[1]) and (analyze[0].rstrip("s") not in possible_bags):
                    #^^If the possible bag (which we've determined to be capable of holding gold) is in the bag and not already added, then we add it.^^
                    possible_bags.append(analyze[0].rstrip("s"))
                    added_flag = True #Something has been added. More to analyze
                    break

print(len(possible_bags)-1) #Minus 1 to account for the shiny gold bag itself. Should get 213.

#Part 2
import re
#My philosophy is to code as vanilla as possible; this one was unavoidable, sadly.
rules = []
with open("Day_7_input.txt","r") as f:
    for line in f:
        l = re.split(r"s contain |s, |, |s.\n|.\n",line)
        #All of these delimiters allow for the plurals, periods, commas, and newlines to be removed while parsing the data cleanly.
        rules.append(l[:-1])#The \n delimiter leaves an empty string as the last element. This removes it.

total = 0
def curserecursion(bag, multiplier): #I hate recursion so goddamn much when its this complicated
    global total #I also hate that I have to declare this to edit total.
    for i in rules:
        if bag == i[0]:
            first = True
            if i[1] == "no other bag":
                return 0 #Exits the recursion loop and undoes multiplication
            for j in i:
                if first == True: #This allows us to skip the first loop, as it only determines the bag to search for
                    first = False
                    continue
                total += int(j[0]) * multiplier
                #The multiplier variable keeps track of the number of bags above variable 'bag' in the tree to keep track of, andscales it appropriately.
                curserecursion(j[2:],multiplier*int(j[0])) #Runs it again with each of the bags that the variable 'bag' contains.

curserecursion('shiny gold bag',1) #1 shiny gold bag. How did this happen?
print(total)#38426 bags. I can't imagine the carry-on fees this would incur

#What did we learn today?
#Occasionally, you might see a path that might lead to the answer, but that you choose
#not to take because it seems too difficult. You try cracking at an easier method, but
#each and every one of them fail, causing you more trouble than the path would have given you. And it turns out that that original path wasn't so
#difficult after all. The moral of the story is to try every route of solving available to you. You never know where it might lead.
            
