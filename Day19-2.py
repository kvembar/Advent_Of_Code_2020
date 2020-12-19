#Monster Messages Part 2 (AOC Day 19)
#Keshav V.
#This is Version 3 of the code, specific to Day 19 Part 2. See Day19-1.py for Part 1
#The christmas miracle here is that while 19-1.py takes around 4-5s to execute, this takes less than 90ms. Yeah, you try figuring that one out!
#Tbh, this solution is a stroke of smartness in the sea of stupidity that is my brain.
#Most of this code is the same, with minor alterations and a major difference near the end.

with open("Day_19_input.txt","r") as f:
    rules = {}
    messages = []
    mode = "rules"
    for line in f:
        if line == "\n":
            mode = "messages"
            continue
        
        if mode == "rules":
            parse = line.split(": ")
            rule_no = parse[0]
            d = parse[1].split()
            if "a" in parse[1] or "b" in parse[1]:
                rules[rule_no] = [parse[1][1]]
            else:
                rules[rule_no] = parse[1].rstrip("\n").split(" ")

        elif mode == "messages":
            messages.append(line.strip("\n"))

rule_trace = []
for key in rules:
    if rules[key][0] == 'a' or rules[key][0] == 'b':
        rule_trace.append(str(key))

stage1 = False
while not stage1:

    to_analyze = []

    for key in rules:
        skip = False
        for rule in rules[key]:
            if rule not in rule_trace and rule != "|":
                skip = True
                break

        
        if (skip == False) and (key not in rule_trace):
            to_analyze.append(key)

    rule_trace += to_analyze

    if ('42' in rule_trace) and ('31' in rule_trace): #Instead of 0 being the marker to stop, we stop when we reach rules 42 and 31 in the list. Critical rules!
        stage1 = True

def cartesian(arr1,arr2): #arr1 x arr2
    products = []
    for i in arr1:
        for j in arr2:
            products.append(i+j)
    return products

combo_path = {}
for key in rule_trace:
    if rules[key][0] in ['a','b']:
        combo_path[key] = rules[key]
        continue

    combos = []
    arr1 = 0
    for i in rules[key]:
        if arr1 == 0:
            arr1 = combo_path[i]
            continue
        elif i == "|":
            combos += arr1
            arr1 = 0
        else:
            arr1 = cartesian(arr1,combo_path[i])
    combos += arr1
    combo_path[key] = combos

count = 0 #This is where things get different

for i in messages:
    matches = []
    if len(i)%8 != 0:
        continue

    breakdown = [i[j:j+8] for j in range(0,len(i),8)] #Break the message down into 8-character chunks. See comment below.
    for i in breakdown:
        if i in combo_path['31']:
            matches.append("31")
            continue
        elif i in combo_path['42']:
            matches.append('42')
            continue

    #With the exception of rule 8, every rule relies upon two other rules, and cartesian producting them doubles their length.
    #Rules 31 and 42 in my code all have strings of a's and b's that are all distinct and are all 8 letters long, meaning two things:
    #1: If the message in question isn't a clean multiple of 8, there's no way to match all the letters to 42s and 31s. Invalid, moving on.
    #2: Since there are no copies of 8-character matches between 31 and 42 (since they're not identical rules), each chunk can be numbered 31 or 42. Not both.

    if len(matches) != len(breakdown): #Could not match all chunks to rules.
        continue
    
    if matches.count('31') >= matches.count('42'):
        continue
    kill_mode = False
    failed = False
    for i in matches:
        if i == '31':
            kill_mode = True
            continue
        if (i == '42') and (kill_mode):
            failed = True
            break
    if (not failed) and ('31' in matches):
        count += 1

    #In order to satisfy rules 8 and 11, the 'matches' array needs to satisfy these two rules in order:
    #There needs to be a run of 42s at the start, and it has to be followed by a run of 42s and a run of 31s of equal length.
    #These come about as a natural consequence of the recursion rules added. 
    #So we count the number of 31s to 42s. If count('31') >= count('42'), then rule 8 is not satisfied.
    #The for loop makes sure there are no 31s in between 42s, because if there are, then either not all chunks are mapped to rules 8 and 11 or rule 8 is being violated
    #And finally, the last conditional makes sure Rule 11 isn't violated and that the previous for loop hasnt indicated a failure.

print(count) #Should get 384. I feel POWERFUL AS ALL HECK THAT I GOT THIS RIGHT.
