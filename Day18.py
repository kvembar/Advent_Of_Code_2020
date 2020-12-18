#Operation Order(AOC Day 18)
#Keshav V.
#Note: The ghost of Day 7 has returned, but I was able to destroy it!
#Recursion's my bitch now. This solution takes less than 100ms to execute for both parts.

#Part 1
def parse(problem): #Self-explanatory title

    index = 0 #Current index that we are parsing. 
    parsed = []
    
    while index < len(problem): #A for loop can't work, as index has to be changed on the fly
        if problem[index] == "(":
            x = parse(problem[index+1:])#Looks at just the parts inside the parentheses and puts them into their own array.
            index += int(x[1]) + 1 #Jumps the index to after the ")" it is associated with. index+1 is necessary so that ")" isn't read twice. OBOE.
            parsed.append(x[0])
        elif problem[index] == ")":
            return (parsed,index) #We reached the end of a parentheses. Return the parse as its own array to add to the one in the higher level.
        elif problem[index] == " ":
            pass
        else:
            parsed.append(problem[index]) #Otherwise, just add to the list as normal.

        index += 1
            

    return parsed #With this, an equation like 3+(5*8)+7 becomes [3,+,[5,*,8],+,7]. This is KEY for Part 1 and 2's solve() functions.

with open("Day_18_input.txt","r") as f:
    problems = []
    for line in f:
        problems.append(line.rstrip("\n"))

def solve(problem):
    solution = 0
    operand = None
    for ind, i in enumerate(problem):
        if type(i) == list: #If the 'thing' we're looking at is a list, we've just hit a parentheses list. 
            i = str(solve(i)) #Evaluate that on it's own, and set it to the value. They are equivalent, after all.

        if ind == 0:
            solution = int(i) #The only purpose of ind here. Avoids having a 'first' flag. I'm so tired of typing those.
            continue

        if not(i.isdigit()):
            operand = i #If i is not a digit or a list, it's an operator.
        else:
            i = int(i)
            if operand == "+":
                solution += i
            elif operand == "*":
                solution *= i #Adds where it adds and multiplies when it multiplies. Simple enough, from left to right as the problem states.

    return solution 
            
total = 0
for i in problems:
    j = parse(i)
    total += solve(j)

print(total) #I got a wonderful 21,347,713,555,555 as my solution. Look at those 5s! They make me feel powerful and happy!

#Part 2
def solve_2(problem): #The problem entered is parsed the same, and since the solution method is different, we need a new function for it.
    solution = 1 #See line 86 for why solution is 1 instead of 0.
    index = 0

    while index<len(problem):
        m = problem[index]
        if type(m) == list:
            problem[index] = solve_2(problem[index]) 
            #Again handling the lists. In part 1, we handle them, replace them with their proper value in the list, and move on.
            #This is slightly different, as it literally spams solve_2 until we get a list that DOESN'T have a list in it (some expression in parentheses)
            #This is necessary, since we aren't going left-to-right with the operations in Part 2.
        index += 1

    while "+" in problem: #Evaluate all +'s first before anything else.
        magic = problem.index("+") #Finds where a + is.
        s = int(problem[magic-1]) + int(problem[magic+1])
        problem[magic] = s
        del problem[magic-1]
        del problem[magic] #We remove magic instead of magic+1, since the number in that spot has shifted over due to line 81's deletion.
        #This loop takes an addition (free of any lists, mind you), performs it, replaces the + with the answer and deletes the two numbers besides em'

    for j in problem:
        if (type(j) == int) or (j.isdigit()):
            solution *= int(j) #This is why solution is 1. After all +'s are gone, we only have multiplications. Letting solution = 1 let's us do this.
    return solution

total = 0
for i in problems:
    j = parse(i)
    total += solve_2(j)
print(total) #Should get 275,011,754,427,339 from my input data in under 100ms!
