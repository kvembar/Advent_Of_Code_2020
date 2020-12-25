#Monster Messages Part 1 (AOC Day 19)
#Keshav V.
#I nearly ragequit twice in the process of coding this POS here. But something magical happened in Part 2 that needs context from Part 1.
#It took me 2 hours to code this, with a 30 minute break to think.
#The 1st version code is in a separate file called Day19.py, and it doesn't work. Bugs galore over there.
#The most I ever got with it was a bunk parsing function and an incomplete verification function. I'll include it for anyone who's interested.

with open("Day_19_input.txt","r") as f:
    rules = {} #The dict that contains all the rules
    messages = [] #All of the messages from the satellite.
    mode = "rules" #Dictates what part of the code we're in.

    for line in f:
        if line == "\n":
            mode = "messages" #The newline empty row dictates that we are in the messages.
            continue
        
        if mode == "rules":
            parse = line.split(": ")
            rule_no = parse[0]
            d = parse[1].split()
            if "a" in parse[1] or "b" in parse[1]:
                rules[rule_no] = [parse[1][1]] #Gets rid of the extra quotation marks around the a and b.
            else:
                rules[rule_no] = parse[1].rstrip("\n").split(" ") #Breaks up the rule into its parts.

        elif mode == "messages":
            messages.append(line.strip("\n"))

#Now comes the hard part to explain right here.
rule_trace = [] #This array determines the ORDER to analyze the rules in for combo_path.
for key in rules:
    if rules[key][0] == 'a' or rules[key][0] == 'b':
        rule_trace.append(str(key))
#First, we look through the list to find the rules that match just a and b and add them to rule_trace. For me, those were rules 122 and 54 respectively.

while True:
    to_analyze = [] #Carries all the keys to add to rule_trace
    for key in rules:
        skip = False
        for rule in rules[key]:
            if rule not in rule_trace and rule != "|":
                skip = True
                break

        
        if (skip == False) and (key not in rule_trace):
            to_analyze.append(key)
    #What this massive for loop does is look for rules that have only stuff in rule_trace (or equivalently, that come about because of the rules in rule_trace)
    #So for example, if rule_trace in this iteration is 4,5, then the only things being added to the array are rules that only have 4s and 5s
    #In the next iteration, it'll look for rules with 4s,5s, and the rules added in the previous iteration. It's basically creating a 'reverse tree' of rules back to rule 0.
    #I could actually use this in a proper implementation of Day 7, actually!
    rule_trace += to_analyze

    if '0' in rule_trace:
        break #If 0 is in our rule_trace, we've gone as far back as we need. Exit the while loop

def cartesian(arr1,arr2): #Takes elements of arr1 and concatenates them to every element in arr2 in every combination a la cartesian product.
    products = []
    for i in arr1:
        for j in arr2:
            products.append(i+j)
    return products


combo_path = {}
for key in rule_trace: #This is why rule_trace was built the way it was. So that combo_path can refer to itself when building combos of combos.
    if rules[key][0] in ['a','b']:
        combo_path[key] = rules[key] #Same reason as line 33-34.
        continue

    combos = []
    arr1 = 0
    for i in rules[key]:
        if arr1 == 0: #The signal for an empty array.
            arr1 = combo_path[i]
            continue
        elif i == "|":
            combos += arr1 #The 'or' pipe lets us know that the combos before and after are separate, but equally valid. Add the current combos to list
            arr1 = 0 #And reset combos to 0
        else:
            arr1 = cartesian(arr1,combo_path[i]) #arr1 builds on itself with the cartesian product of all the rule numbers.
    combos += arr1 #Deals with the fact that the last valid string of rules isn't added to combos, as it is only added in loop when "|" appears.
    combo_path[key] = combos #The key has these valid combos, now in the form of a string of a's and b's. It effectively gives a list of possible combinations.

madlad = combo_path['0'] #I felt like one after the code executed properly.
count = 0
for i in messages: #This for loop is why the execution time is so long. Every thing before takes less than 1/4 of a sec to execute! (verified via print statements)
    if len(i) != 24: #Minor optimization due to my input's quirks. May not work for yours. As it turns out, all possible messages for rule 0 are all of length 24.
        continue
    if i in madlad:
        count += 1 #If a valid combo, add 1 to count.

print(count) #Should get 279 from my input.
