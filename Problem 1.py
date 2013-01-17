# Problem 1

def ryanIsTheCoolest():
    x = 0
    total = 0 
    while True:
        x = x + 3
        if x < 1000:
            total = total + x
        else:
            return total

def multiplesOf5():
    x = 0
    total = 0
    while True:
        x = x + 5
        if x < 1000:
            total = total + x
        else:
            return total
            

print(ryanIsTheCoolest() + multiplesOf5())
