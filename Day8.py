#Handheld Halting (AOC Day 8)
#Keshav V.

with open("Day_8_input.txt","r") as f:
    instructions = []
    for line in f:
        instructions.append(line.split()) #I'm not making the same mistake as last time.

#Part 1
ind = 0 #Current index of instruction
ind_visited = [] #keeps indexes visited -- to detect loops
accumulator = 0

while ind not in ind_visited: #Revisiting an index is the sign of a loop. Breaks out of the while.

    info = instructions[ind]
    if info[0] == 'acc':
        accumulator += int(info[1].lstrip("+")) #Removes + to avoid conversion issues to int.
        ind_visited.append(ind)
        ind += 1

    elif info[0] == "jmp":
        ind_visited.append(ind)
        ind += int(info[1].lstrip("+")) #Jumps info[1] far ahead. Contains the argument.

    else:
        ind_visited.append(ind) #Handles 'nop.' Too lazy :P
        ind += 1

print(accumulator) #Should get 2080

#Part 2
breakout = False #Flags when to breakout of the function (see first if in second while.)
edit = True #Flags when to edit the next jmp or nop the program sees.

while True: #Program will loop until last instruction completed, indicated when breakout is True

    accumulator = 0
    ind = 0
    ind_visited = [] #Reset values of each for each instruction change.

    while ind not in ind_visited:
        if ind >= len(instructions):
            breakout = True
            break

        info = instructions[ind]

        if info[0] == 'acc':
            accumulator += int(info[1].lstrip("+"))
            ind_visited.append(ind)
            ind += 1

        elif info[0] == "jmp" or info[0] == "jmpx": #See why the x is there in the for loop below
            ind_visited.append(ind)
            ind += int(info[1].lstrip("+"))
        
        else:
            ind_visited.append(ind)
            ind += 1
        #Mostly identical. Some minor changes.
        
    if breakout == True:
        break

    for i in instructions:
        if i[0] == "nop" and edit == True:
            i[0] = "jmpx" #The x marks the most recently edited jmp or nop instruction.
            edit = False
            break
        elif i[0] == "jmp" and edit == True:
            i[0] = 'nopx'
            edit = False
            break
        elif i[0] == "nopx" and edit == False:
            i[0] = 'jmp' #Changes it back, since it didn't breakout, the boot code is still in a loop
            edit = True #edit flag is True, looking for next instruction to edit.
        elif i[0] == "jmpx" and edit == False:
            i[0] = 'nop'
            edit = True


print(accumulator)
#The instruction that should be edited in my input is a jmp -250 instruction at index 345 (line 346 in input).
#Change that to nop -250 and the program exits normally.
#Should get accumulator as 2477
