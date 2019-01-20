##allows you to start at a c**2 value and find possible a / b combos. Will generate a 2d array

import numpy as np

z = 1000 ##represents your c**2 value ##this is the variable you change

def pythag_finder(c2): 
    c = int(c2**(1/2))
    pythag_tuples = []  #list of a's and b's that work with "c" variable
    for a in range(1,c,1):
        for b in range(a,c,1):
            pythag = a**2 + b**2
            if pythag == c2:
                pythag_tuples.append([a,b,c])  #append to list
            else:
                continue
    print(np.array(pythag_tuples))  #output a multi-dimentional array for easy reading / analysis later
    
pythag_finder(z)
