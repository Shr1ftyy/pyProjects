import random
import math

scl = 0.5
seed = input("Type Seed Here: ")

random.seed(seed)

def generateWhiteNoise(width,height):
    noise = [[r for r in range(width)] for i in range(height)]

    for i in range(0,height):
        for j in range(0,width):
            noise[i][j] = random.randrange(0,10,1)

    return noise

noise = generateWhiteNoise(30, 30)

for i in noise:
    print()
    for o in i:
        if(o <= 4):
            print("-",end='')
        else:
            print('#',end='')
print ("""
Seed: """ + str(seed))
