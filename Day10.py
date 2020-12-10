#Adapter Array (AOC Day 10)
#Keshav V.
#This one was an emotional rollercoaster: Alright to bad, to Good, and then Brain Aneurysms, then amazing!

with open("Day_10_input.txt","r") as f:
    jolts = []
    for line in f:
        jolts.append(int(line.rstrip("\n")))

#Part 1 (Different and MUCH less complicated than the one I used to solve Day 10)
#The original code did not rely on sorted(jolts). You can probably see why I improved it.

ordered = [0] + sorted(jolts) #Added zero to account for starting jump
gaps = [] #The gaps between each consecutive adapter were kept here. Prevents the need for two counters.
for i in range(len(ordered)-1):
    g = ordered[i+1]-ordered[i]
    gaps.append(g)

print(gaps.count(1) * (gaps.count(3)+1))
#The plus one is there to handle the joltage jump of 3 at the very end. Should get 1755.


#Part 2
#Note: If your input has even a single jump of 2, this solution is null and void. Mine had only jumps of 1 and 3.

runs = [] #A 'run' is defined as a chain of adapters with 1-jolt differences. 3-jolt differences delimited each run. This is a list of lists of runs
to_add = [0] #to_add is the array of runs that will be added. Starts at zero for the same reason as adding zero above.

for i in ordered:
    if i-to_add[-1] == 1:
        to_add.append(i)
    elif i-to_add[-1] == 3:
        runs.append(to_add)
        to_add = [i] #Add the run to the list and start a new run with i, as it begins the next.

runs.append(to_add)
#This section of the code had several bugs, and it gave me an anuerysm every single time one happened.
#But to be fair, if it wasn't for the bugs here, I wouldn't have figured out the bugs in the loop below and got a lot of incorrect guesses.

poss = [] #The possible configurations of each run.
#Since one run doesn't affect any of the others' combinations, we can multiply the combos of each run together and we get the total number of ways to arrange the adapters.
for i in runs:
    n = len(i)
    combo = 2**(n-2)-(n-4)*(2**(n-5))+(n-5)*(2**(n-6))
    poss.append(round(combo))
    #Oh boy, this one has a long explanation. See Note_10.pdf in this repo. Warning: Involves some pure/applied combination math.
    #This section of the code is why the 'no jump 2' rule exists.
    #This is the only cool thing I'll do in this competition. Then again, maybe this isn't cool.

prod = 1
for i in poss:
    prod *= i #Multiplying the possibilities with each other.

print(prod) #You should get a whopping 4,049,565,169,664 combinations from my input. At least you have options with your adapters!

        
