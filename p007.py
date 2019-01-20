#solution is to append to a list of primes and divide the next int by all primes. If it isn't divisible
#then you have a new prime

def nth_prime(x):
    primes = [2,3,5,7,11,13] #starter list of primes
    i = 13
    while len(primes) < x:
        check = all(i % prime != 0 for prime in primes) #see if 'i' can be divided by anything in primes
        if check == True:  #True = 'i' is not divisible by any primes
            primes.append(i)
        i+=1
    print(primes[-1])

nth_prime(10001)
