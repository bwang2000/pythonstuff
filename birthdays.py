import random
people = 23
tries = 1000

def getbirthday(a):
    '''returns a list of birthdays with a characters'''
    b = []
    for i in range(a):
        #b.append(random.randint(1,365))
        c = random.randint(1,365)
        if (c <= 31) : b.append(f"1/{c}") #jan
        elif (c > 31 and c <= 59) : b.append(f"2/{c-31}") #feb
        elif (c > 59 and c <= 90) : b.append(f"3/{c-59}") #march
        elif (c > 90 and c <= 120) : b.append(f"4/{c-90}") #apr
        elif (c > 120 and c <= 151) : b.append(f"5/{c-120}") #may
        elif (c > 151 and c <= 181) : b.append(f"6/{c-151}") #june
        elif (c > 181 and c <= 212) : b.append(f"7/{c-181}") #july
        elif (c > 212 and c <= 243) : b.append(f"8/{c-212}") #aug
        elif (c > 243 and c <= 273) : b.append(f"9/{c-243}") #sep
        elif (c > 273 and c <= 304) : b.append(f"10/{c-273}") #oct
        elif (c > 304 and c <= 334) : b.append(f"11/{c-304}") #nov
        elif (c > 334) : b.append(f"12/{c-334}") #dec
    return b

def checklist(a):
    '''takes in a list and sees there if two elements match, returns true if yes, returns false if no'''
    seen = []
    for i in a:
        if i in seen:
            return True
        else:
            seen.append(i)
    return False

def samebirthday(a):
    '''makes a list of a birthdays, and sees if any birthdays match. Returns true if yes, returns false if no'''
    birthdays = getbirthday(a)
    print(birthdays)
    if (checklist(birthdays)):
        #print("At least two people share birthdays in this group of people.")
        return True
    else: 
        #print("There are no shared birthdays in this group of people")
        return False
    
people = 0
while (people < 1 or people > 100):
    people = int(input("How many birthdays should I generate? (Max 100) "))
    if (people < 1 or people > 100): print ("Please input a number between 1 and 100")
    else: break
    
tries = 0
while (tries < 1 or tries > 100000):
    tries = int(input("And how many times would you like to test? (Max 100) "))
    if (tries < 1 or tries > 100000): print ("Please input a number between 1 and 100000")
    else: break

counter = 0
for i in range(tries):
    if (samebirthday(people)):
        counter += 1
print (f"According to this data, there is a {counter*100/tries}% chance that at least 2 people in a group of {people} will share a birthday")

