import msvcrt
import random
import string

print("ROBOT MISSILE")
print("")
print("TYPE THE CORRECT CODE")
print("LETTER (A-Z) TO")
print("DEFUSE THE MISSILE.")
print("YOU HAVE 4 CHANCES")
print("")


code = random.choice(string.ascii_uppercase)
defused = False
attempt = 1
while attempt <= 4:
    guess = str(msvcrt.getwch()).capitalize()
    if guess == code:
        defused = True
        break
    elif ascii(guess) < ascii(code):
        print("LATER")
    else:
        print("EARLIER")
    print(" THAN " + guess)
    attempt += 1

if defused == True:
    print("TICK...FZZZZ...CLICK")
    print("YOU DID IT")
else:
    print("BOOOOOOOOMMM...")
    print("YOU BLEW IT")
    print("THE CORRECT CODE WAS " + code)


        

