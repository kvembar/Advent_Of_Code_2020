# Ticket Translation (AOC Day 16)
# Keshav V.
# Note: This one was pretty fun! It took me a while to solve it, but this was actually interesting!

import re #RETURN OF THE REGEX

#Part 1
with open("Day_16_input.txt","r") as f: #This with function is the first one in a while to have the parsing be done in it.
    valid = [] #Keeps the ranges of numbers that make tickets valid
    to_test = [] #List of all tickets to test, thus the name.
    tickets = [] #List of valid tickets for Part 2
    fields = [] #List of the various fields that each ticket column could be.
    first = True #Flag for my ticket that I will put in its own variable.
    for line in f:
        l = re.split(r" |or|\n|-|,|:", line) #Parses the data conveniently. And it also accidentally cuts off 'platform,' but it has little impact on the code.
        if len(fields) != 20:
            if l[0] == "departure" or l[0] == "arrival":
                fields.append(l[0]+" "+l[1]) #Since each field with these words are two words.
            else:
                fields.append(l[0])
        if l[0].isalpha(): #This tells you that the data belongs to the number fields in 'valid.'
            for i in l:
                if i.isdigit():
                    valid.append(int(i)) #Appends the raw, unseparated number. Will be parsed in part 2
        elif l[0].isdigit: #Tells you that this line belongs to a ticket.
            if first == True:
                my_ticket = [int(i) for i in l if i.isdigit()]
                first = False
                continue
            to_test.append([int(i) for i in l if i.isdigit()]) #List of just numbers for each one to test.
            tickets.append([int(i) for i in l if i.isdigit()]) #Setup for part 2

ranges = [] #Keeps the valid numbers. If the tested ticket's number is not in here, then it isn't valid.
for i in range(0, len(valid), 2):
    lower = valid[i]
    upper = valid[i+1]
    for j in range(lower, upper + 1):
        if j not in ranges:
            ranges.append(j)
tser = 0 #Ticket Scanning Error Rate
for i in to_test:
    for j in i:
        if j not in ranges:
            tser += j #Adds the error to the TSER.
            tickets.remove(i) #Since this ticket is invalid, it will be removed from the list of valid tickets called 'tickets.'
print(tser) #Should get 26026 with my input. How coincidental.

#Part 2. I felt like a genius when I solved this.
dep_ranges = [valid[i:i+4] for i in range(0, len(valid),4)] 
#Each field in my input had 4 numbers describing which numbers are valid. Ex: 33,430,456,967 described departure location values.

temp = [(fields[i],dep_ranges[i]) for i in range(0,20)]
reference = {key:value for key,value in temp} #Matches the 4 numbers in dep_ranges to their respective fields.

columns = list(map(list, zip(*tickets))) #A little magic trick to transpose the list (rows become columns and vice versa)
#The zip(*tickets) takes the arrays in tickets (rows) as iterables, and matches each of lists' elements 1-to-1 with each other.
#The rest of it is just tomfuckery to get it back into a list of lists, because Python 3 can be small-brain with generators sometimes. 

values = [] #Will contain the elements of my_ticket with the relevant field names

#VVVVV This is where the magic happens VVVVV

while len(values) < 20: #Repeat this loop until values is 20 long, which is the number of fields.
    for col,i in enumerate(columns):
        possible_areas = [b for b in dep_ranges] #A copy of dep_ranges that will narrow down which column is associated with what field.

        for j in dep_ranges:
            for k in i:
                if not(j[0]<=k<=j[1] or j[2]<=k<=j[3]): #If the columns value lies outside the dep_range of the field we are analyzing...
                    possible_areas.remove(j) #Remove it from the list of possible field-ranges that that column falls in
                    break #And move on to the next.
        
        if len(possible_areas) == 1: #After all is said and done, if we have only one left, we add it to values

            for key, value in reference.items():
                if value == possible_areas[0]:
                    badabing = key #Matches the dep_range with the field it is associated with.
                    break

            values.append([my_ticket[col], badabing])
            dep_ranges.remove(possible_areas[0]) #Since we identified which column has that field/associated ranges, we remove it from search. No need to look for it again.
            continue

prod = 1
for i in values:
    print(i) 
    #If you look at each of the arrays presented to you, the 6 arrays that have the word 'departure' in them have the numbers 173,139,163,61,103,and 53
    #Their product is 1305243193339, which is the answer to Part 2 with my input.
    #As a neat side effect, all of the other categories are also labeled. At least I won't be confused while on my train!
    #And if you're too lazy to do that...
    if 'departure' in i[1]:
        prod *= i[0]

print(prod) #Here's the product for you.