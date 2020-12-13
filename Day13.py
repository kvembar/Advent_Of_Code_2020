#Shuttle Search (AOC Day 13)
#Keshav V.
#Note: EXCITING MATH RETURNS! But this time, I won't need an excessively long pdf to explain this time.
#Today's pure math factoid is the modulus and the CRT!

with open("Day_13_input.txt","r") as f:
    buses = []
    for line in f:
        buses.append(line.rstrip("\n"))

#Part 1
time = int(buses[0])-1 #The timestamp you arrive at.
ids = buses[1].split(",")
while "x" in ids:
    ids.remove("x") #This is a 2 liner I oughta use more often for parsing strings and lists.

found = False #Flag to determine when a bus has arrived
counter = -1 #Amount of time waited.

while found == False:
    time += 1
    counter += 1
    #The immediate addition of 1 is why both counter and time are subtracted by one.
    
    for i in ids:
        if time%(int(i)) == 0: #check if any of the buses have arrived back from their time loop.
            found = True
            data = [counter, i] #the time waited and the bus id that arrived.
            break

print(data) #I got [6,17] with a product of 102. Do your own damn multiplication!
#Says the guy who at first put in that 6*17 = 112 and had to wait a minute because of it.

#Part 2. This one was fun! And I was faster than all of top 4!
ids = buses[1].split(",") #Since the x's matter here, reset ids to original data.

delays = []
for i in ids:
    if i.isdigit():
        delays.append([(int(i)-ids.index(i))%int(i),int(i)])
'''
The above looks complicated, but 'delays' is actually just a set of moduli that our time t has to satisfy.
For example in my input, 19 is listed first. That means that our time t, whatever it is, has to be 0 mod 19, so in 'delays,' its represented as [0,19]
And the number 37 is at the 13th position, so to arrive at the 13th minute, our time has to be -13 mod 37, or 24 mod 37 (since it makes rounds at 37 minute intervals). Represented as [24,37] in 'delays.'
Repeat for all the numbers in the list.
The first entry in each list in delays is calculated by finding their position in the ids (the minute they have to arrive), and subtracting it from the modulus (the number itself)
Then %int(i) is taken to normalize the number to be positive and below the modulus
The second entry in each list is just the modulus itself.
'''

delays = sorted(delays, key=lambda k:k[1])

n = -1
to_add = 1
current_modulus_index = 0

while current_modulus_index != len(delays):
    n += to_add
    if n%(delays[current_modulus_index][1]) == delays[current_modulus_index][0]:
        to_add *= delays[current_modulus_index][1]
        current_modulus_index += 1
'''
This bit of code is an implementation of the Chinese Remainder Theorem (https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
It is a sieve designed to find the first number that satisfies the moduli in delays.
Note that this method has an exponential big O. I implemented it because the number of moduli are small, and it is rather quick with small numbers of moduli.
Read about this method in the wikipedia article.
'''
print(n) #With my input, you should get a whopping 327,300,950,120,029. That is 622.3 million years into the future of timestamp 0, assuming these are minutes as the problem states.

