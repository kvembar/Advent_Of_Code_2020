#Expense Report (AOC Day 1)
#Keshav V.

#Reading in data
with open("Day_1_input.txt","r") as f:
	expenses = f.readlines()

#Part 1
expenses = [int(i.rstrip("\n")) for i in expenses] #Removing newline

for i in expenses:
    if (2020-i) in expenses: #No nested for loops necessary
        print(f"Your numbers are {i} and {2020-i} for a total of {i*(2020-i)}")
        break

#Part 2
for i in expenses:
    for j in expenses:
        if i+j>2020: #Put in this just in case timeout occurs
            continue
        elif 2020 - (i+j) in expenses:
            print(f"Your numbers are {i},{j}, and {2020-i-j} for a total of")
            print(i*j*(2020-i-j))
            break
#Will print out answer 3 times, granted, but aiming for speed here.