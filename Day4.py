#Password Processing (AOC Day 4)
#Keshav V.
#This one was *rough*

with open("Day_4_input.txt","r") as f:
    data = f.readlines()
    data.append("\n") #I need to add a newline character to the end of the data
    #Makes sure the for loop does its job, as the checking process only occurs with a newline delimiting batches
    
info = [] #This array is what all the code depends on. I'll explain further.
required = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
count = 0 #You should know what this is for at this point, lol.

#Part 1
for i in data:
    if i == "\n": #This code block is the 'testing' procedure for each batch.
        test = True #'test' serves as a flag for a passport that failed. if test is False, then the passport isn't valid.
        for j in required:
            if j not in info: #Checks if the required fields are in the batch
                test = False #Fails if it find one it doesn't have
                break
        info = [] #Resets info for a new batch/passport.
        if test == True:
            count += 1

    d = i.split(" ")
    
    for x in d:
        info.append(x[:3]) #In part 1, you need only be concerned with the fields. Thus the [:3] slice to info.
        #info is what contains each batch, and when there's a newline, the testing block above gets run.
        #After testing, the info block is reset to zero for the next passport batch of fields.
        #This is why I need to put a newline at the very end: So that the last batch can be tested.
print(count) #Should get 206.


#Part 2... oh god the horror. helpmehelpmehelpme...
count = 0
for i in data:
    if i == "\n":
        del info[0] #info[0] is always newline, as it gets added after all this code to the next iteration of info.
        test = True
        parsed_info = [i[:3] for i in info]
        for j in required:
            if j not in parsed_info:
                test = False #Identical testing to part 1, but modified to keep the values for testing.
        
        for j in info:
            f = j.split(":") #Breaking down elements to fields and values.
            field = f[0]
            value = f[1]

            #Testing of all the relevant fields
            if field == "byr":
                if int(value) <  1920 or int(value)>2002:
                    test = False
                    
            elif field == "iyr":
                if int(value)< 2010 or int(value)>2020:
                    test = False
                    
            elif field == "eyr":
                if int(value)< 2020 or int(value)>2030:
                    test = False
                    
            elif field == "hgt":
                if "cm" in value:
                    height = int(value[:-2]) #Takes just the number.
                    if height < 150 or height > 193:
                        test = False
                        
                elif "in" in value:
                    height = int(value[:-2])
                    if height < 59 or height > 76:
                        test = False
                        
                else:
                    test = False
                    
            elif field == "hcl":
                numbers = True
                for i in value:
                    if i not in '0123456789abcdef#':
                        numbers = False #numbers is another fail condition that needed its own for loop to work.
                        
                if len(value) != 7 or value[0] != "#" or numbers == False:
                    test = False
                    
            elif field == "ecl":
                if value not in ('amb blu brn gry grn hzl oth'): #Ah, the wonder of Ctrl+C Ctrl+V!
                    test = False
            elif field == "pid":
                if len(value) != 9 or not value.isdigit():
                    test = False
            
        info = []
        
        if test == True:
            count += 1
        
    d = i.split(" ")
    
    for x in d:
        info.append(x.rstrip("\n"))
        #Take notes kids: If you need to remove a \n character that only appears sporadically,
        #NEVER use x[:-1], since it will cut off your data and make a lot of false rejections
        #And sad faces :(

print(count)#Should get 123
    
