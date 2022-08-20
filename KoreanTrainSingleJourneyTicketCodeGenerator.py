import random
from random import randint
import time
gentype = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'
print("Hello To My Ticket Generator")
print("This Script only Education")
total = input("Generate Number")
#Number To Generate
number = int(total)
file = (total + " Generated.txt")
file2 = 'GiftCardsCodes.txt'
mode = input("Code\nKorailsinglejourneyticket\n")
#Korailsinglejourneyticket
if(mode == "Korailsinglejourneyticket"):
    for x in range(number):
        generate1 = random.choice(gentype)
        generate2 = random.choice(gentype)
        generate3 = random.choice(gentype)
        generate4 = random.choice(gentype)
        space1 = "-"
        generate5 = random.choice(gentype)
        generate6 = random.choice(gentype)
        generate7 = random.choice(gentype)
        generate8 = random.choice(gentype)
        space2 = "-"
        generate9 = random.choice(gentype)
        generate10 = random.choice(gentype)
        generate11 = random.choice(gentype)
        generate12 = random.choice(gentype)
        space3 = "-"
        generate13 = random.choice(gentype)
        generate14 = random.choice(gentype)
        generate15 = random.choice(gentype)
        generate16 = random.choice(gentype)
        space4 = "/"
        generate17 = random.choice(gentype)
        generate18 = random.choice(gentype)
        generate19 = random.choice(gentype)
        generate20 = random.choice(gentype)
        newline = "\n"
        with open(file, 'a') as out:
            out.write(generate1+generate2+generate3+generate4+space1+generate5+generate6+generate7+generate8+space2+generate9+generate10+generate11+generate12+space3+generate13+generate14+generate15+generate16+space4+generate17+generate18+generate19+generate20+newline)
print("Thanks For Using This Script")
time.sleep(5)
