#Toboggan Trajectory (AOC Day 3)
#Keshav V.
'''
Note: The code has been modified from the Part 1 solution,
since Part 2 is just an extension of Part 1. Part 1 used a simple for loop,
But Part 2 needed to be more general to allow the 'Right 1 Down 2'
to be computed properly, but the code works in any case.
'''

#Part 1 and 2
with open("Day_3_input.txt","r") as f:
    trees = f.readlines() #Reading in data as per usual

column = 0
row = 0
right_shift = 3
down_shift = 1 #How much the toboggan will move right and down each iteration

tree_count = 0

while row <= len(trees)-1: #<= is used instead of != due to the down 2 case skipping the final row.
    if trees[row][column] == "#":
        tree_count += 1
    row += down_shift
    column = (column+right_shift)%(len(trees[0])-1) #The power of wraparound.


print(tree_count)
#By modifying right_shift and down_shift to specifications, you can find the number of trees
#Using 1,1 3,1 5,1 7,1 1,2 and multiplying them together
#You should get 234, 79, 72, 91, and 48 non-respectively as answers.
