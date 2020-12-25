#Crab Cups (AOC Day 23)
#Keshav V.
#This was ROUGH. This code takes around 10 hours to execute. Yes. Really.

#Part 1
cups = "475328061" #All the digits have been shifted down by 1 manually so that the code works.
parsed = [int(i) for i in cups]

for move in range(100):
    moved_off = parsed[1:4] 
    del parsed[1:4] #Effectively moves off the cups. Yes, I could've used a linked list, but I'm deadly dedicated to stupid shit, so this is what you're working with.
    x = parsed.pop(0) #Acts as the starting cup.

    current_cup = (x-1)%9
    while current_cup in moved_off:
        if current_cup == 0:
            current_cup = (current_cup-1)%9
        else:
            current_cup -= 1
    
    destination = parsed.index(current_cup) #Find where the destination of the cup is.
    for i in range(1,4):
        parsed.insert(destination+i,moved_off[i-1]) #Optimization of moving the moved_off cups back in at the destination cup.
    parsed.append(x) #Moves starting cup to the end of the list.

while parsed[0] != 0:
    parsed = parsed[1:] + [parsed[0]] #Shifts the list until the cup labeled '0' (really '1') is at the front. Yes, a linked list would've been better. 
    #Shut up, I don't know how classes, __init__, __next__, data structures, or any of that stuff works. Please send help.
    
print("".join([str(i+1) for i in parsed[1:]])) #Should get 28946753 for the answer.

#Part 2
cups = "475328061"
parsed = [int(i) for i in cups]
parsed += [i for i in range(9,1000000)]

place = 0
for move in range(10000000):
    moved_off = parsed[1:4]
    del parsed[1:4]
    x = parsed.pop(0)
    
    current_cup = (x-1)%1000000
    while current_cup in moved_off:
        if current_cup == 0:
            current_cup = (current_cup-1)%1000000
        else:
            current_cup -= 1
    
    destination = parsed.index(current_cup)
    for i in range(1,4):
        parsed.insert(destination+i,moved_off[i-1])
    parsed.append(x)

    if move % 100 == 0:
        print(f"move reached {move}") #Tracks the progress of execution. Feel free to remove this if it is too annoying. I just used it to time the execution.

while parsed[0] != 0:
    parsed = parsed[1:] + [parsed[0]]

print(parsed[1]*parsed[2]) #Same explanation as Part 1. I used Part 1 to test my optimizations, which is why the code for both are nigh-identical.
#Should get 519044017360 as the answer. Well, if you have the patience and the ice packs that is.