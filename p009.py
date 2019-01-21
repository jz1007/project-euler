# find the triplet(s) that adds up to a number (indicated by variable 'n')

def p_triplet(n):  
    for a in range(1,n+1,1):
        for b in range (a+1,n+1,1):
            c = (a**2 + b**2)**(1/2)
            if (a + b + c) == n:
                print(a, b, c) #triplet
                print('Product is: ' + str(int(a*b*c))) #this is the answer

p_triplet(1000)
