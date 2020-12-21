#Allergen Assessment (AOC Day 21)
#Keshav V.
#Note: You are never going to see my solution to Day 20 Part 2, because I'm at the end of my wit on that one,
#and I don't think a hint can save me here. But Day 21 is just Day 16 in a shiny new coat.
#The fact that I couldn't solve Day 20 means I am lacking in something. I guess I just suck at 2D arrays and jigsaw

import re
with open("Day_21_input.txt","r") as f:
    ingred = []
    for line in f:
        p = re.split(" ",line.rstrip("\n)")) #Regex allows me to combine these two operations.
        for i in range(len(p)):
            p[i] = p[i].lstrip("(")
            p[i] = p[i].rstrip(",)") #Getting rid of any extraneous separators.
        ingred.append(p)

#Part 1
unique_ingred = []
unique_allergens = {}
for i in ingred:
    space = i.index('contains')
    for j in i:
        if j not in unique_ingred and j not in unique_allergens:
            if i.index(j)<space:
                unique_ingred.append(j) #Stores unique ingredients
            elif i.index(j)>space:
                unique_allergens[j] = [] #Will store the ingredients associated with this allergy

for allergy in unique_allergens.keys():
    for label in ingred:
        space = label.index('contains') #Separates the allergies from allergens.
        if allergy in label: #If the allergy is in the label of the food...
            if unique_allergens[allergy] == []: #And if we haven't encountered it yet...
                for k in range(space):
                    unique_allergens[allergy] += [label[k]] #Add everything before the allergies
            else: #And if we have seen it before... (analyzed it with the first time it appears)
                to_keep = []
                for ingredient in label:
                    if ingredient in unique_allergens[allergy]:
                        to_keep.append(ingredient)
                        #Search through the list of associated possible ingredients
                        #If it is there in the list, you keep. If not, ignore it.
                unique_allergens[allergy] = to_keep

determiner = len(unique_allergens) #This will tell us if we have one ingredient to each allergen.
while True:
    for allergy in unique_allergens.keys():
        arr = unique_allergens[allergy]
        if len(arr) == 1: #If we have a 1-to-1 correspondence
            cross = unique_allergens[allergy][0]
            for hunt in unique_allergens.keys():
                if hunt == allergy:
                    continue #Avoids deleting its own allergy. Learned through experience
                if cross in unique_allergens[hunt]:
                    unique_allergens[hunt].remove(cross) #Remove it from the allergy, since it's already determined.

    count = 0
    for i in unique_allergens.values():
        for j in i:
            count += 1

    if count == determiner:
        break #Only exits if a 1-to-1 correspondence between allergen and ingredient has been achieved

strike = []
for i in unique_allergens.values():
    for j in i:
        strike.append(j) #Setup for loop below.

final_count = 0
for i in ingred:
    space = i.index('contains')
    for ind,j in enumerate(i):
        if j not in strike and ind<space: #If the ingredient is not a danger ingredient and not an allergy, add 1.
            final_count += 1 #Count of ingredients that appear in the list.
print(final_count) #Should get 2282 from the list

#Part 2. Yep. This is it. 4 short lines, since i've already done the association game.
dangerous = ""
for i in sorted(unique_allergens): #sorts alphabetically and creates the string
    dangerous += unique_allergens[i][0]+","
print(dangerous[:-1]) #I got vrzkz,zjsh,hphcb,mbdksj,vzzxl,ctmzsr,rkzqs,zmhnj from my input.
