#Docking Data (AOC Day 14)
#Keshav V.

with open("Day_14_input.txt","r") as f:
    memos = []
    for line in f:
        memos.append(line.rstrip("\n"))

#Part 1
memories = {} #I'm really salty about this particular variable. See the notes after line 34 for why I'm salty.

for line in memos: #Yes, I could've incorporated this into the with() function from earlier, but I still have PTSD from one of the problems I tried to do this on at first.
    data = line.split(" = ")
    
    if "mask" in line:
        mask = list(data[1])
        continue #Sets the current mask as the new mask

    if "mem" in line:
        address = int(data[0].strip("mem[]")) #Leaves just the address as an integer
        value = list(str(bin(int(data[1])))[2:]) #Turns the value into an int, converts to binary, back to a string, cuts off that fricking '0b' in the front and makes each digit into an array.

    while len(value) != 36:
        value = ['0'] + value #Normalizes the length of the array to the length of the mask, 36.

    for index in range(len(value)):
        if mask[index] == '0':
            value[index] = '0'

        elif mask[index] == '1':
            value[index] = '1'
        #Applies mask rules
        
    memories[address] = int("".join(value),2)
    #Before the 'memories' dictionary was included, I had two separate lists, one storing the index, one storing the value
    #This single line of code replaces a 7-liner with O(n^2) xomplexity that made the program's execution slow to a crawl of around a second or two.
    #Part 2 was even worse... see line 81.

print(sum(memories.values())) #Got 5,055,782,549,997 from my data.

#Part 2
memories = {}
for line in memos:
    data = line.split(" = ")
    
    if "mask" in line:
        mask = list(data[1])
        continue

    if "mem" in line:
        address = list(str(bin(int(data[0].strip("mem[]"))))[2:]) #The process for the value in Part 1 of conversion to binary digit list is repeated for the address here.
        value = int(data[1])


    while len(address) != 36:
        address = ['0'] + address

    for index in range(len(address)):
        if mask[index] == '1':
            address[index] = '1'

        elif mask[index] == "X":
            address[index] = "X" #Same mask rules as before
        
    poss_ads = [] #List of possible addresses for the X's.
    combos = [list(str(bin(i))[2:]) for i in range(2**address.count("X"))] #Lists out the possible combinations of 1s and 0s to replace the X's.
    
    for i in range(len(combos)):
        while len(combos[i]) != address.count("X"):
            combos[i] = ["0"]+combos[i] #This code block makes sure that the length of each combo is the same as the number of Xs, so that the replace function can get to all Xs.

    for i in combos:
        temp = "".join(address) #Stores the address, X temporarily to enter in the combinations.
        count = 0
        while "X" in temp:
            temp = temp.replace("X",i[count],1)
            count += 1 #Next number in combo to replace
        poss_ads.append(int(temp,2)) #The resulting 'temp' variable is a possible address to add it too.

    for i in poss_ads:
        memories[i] = value #Remember that 7-liner thing from earlier? A similar thing was implemented here that made the program take THIRTY SIX SECONDS TO EXECUTE!
        #With this fix and improvement, it takes less than half a second. I am so salty that the solution was literally to change two lists to a dictionary and make use of the third parameter in .replace()
        #I'm mad about it. But it improves the code, so the salt is diluted a bit.

print(sum(memories.values()))  #Should get 4,795,970,362,286 from my input. Surprisingly smaller than expected.          
