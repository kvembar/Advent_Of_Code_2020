#Combo Breaker (AOC Day 25)
#Keshav V.
#Fun fact: This code is almost exactly as long as my Day 1 solution! We came full circle!
#This is literally just symmetric key exchange. I remember this from CS101.

card = 11404017 
door = 13768789 #My inputs, this time not in another doc.

def reverse_loop(n):
    loop = 0
    start = 1
    while start != n:
        start = (7*start)%20201227
        loop += 1
    return loop #A very cheesed function tbh. It literally runs through the encryption algorithm starting with 1 until we get the card/door's number and returns the loop number.

loop_size_card = reverse_loop(card)
loop_size_door = reverse_loop(door)

answer = card #answer will store.... well, take a guess.

for i in range(loop_size_door-1):
    answer = (answer*card)%20201227 #Runs through algorithm with door's loop size (-1 due to OBOE) and the card's encrypted subject number.

print(answer) #Should get 18862163

'''
Part 2 was to press a button to complete AOC 2020. But I needed to complete Day 20 Part 2 before I could.

I had an awesome time doing AOC, and while, yes, I struggled a lot, and I may not have performed as well
as I thought I have, I came away from it smarter, and with a better appreciation for coding! Every time
I solved a difficult puzzle, I felt like I could split the earth in two with my bare hands. And I learned a lot
about thinking like a programmer here as my skills have been taxed and tested.

I will come back next year to complete AOC 2021 in Python/C++. Thank you for being on this journey with me,
whether you were in the mines AOC chat or you're looking through my annotated code.

May your typing be ever swift, and may your code not suffer from OBOEs and missing newlines.
Thank you,
Keshav V.
'''