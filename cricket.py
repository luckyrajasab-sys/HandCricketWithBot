import random
def getcomputermove():
    return random.randint(1,6)
def playhandcricket():
    totalscore = 0
    out = False
    
    print("Welcome to Hand Cricket")
    print("Choose a number between 1 and 6 to score runs.")

    while not out:
        Player = int(input("Your move (1-6): "))
        
        if Player < 0 or Player > 6:
            print("Invalid Choose a number between 1 and 6.")
            continue
            
        Bot = getcomputermove()
        print("Computer chose:", Bot)
        
        if Player == Bot:
            print("OUT The Bot matched your number.")
            out = True
            break
        else:
            totalscore = totalscore + Player
            print("Current Score:", totalscore)
    print("FINAL SCORE:", totalscore, "runs")
playhandcricket()
