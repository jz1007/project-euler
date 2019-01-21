#pythagorean triplet that equals 1000

import numpy as np

z = 250 ##use 'z' for 'c' in a**2 + b**2 = c**2

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