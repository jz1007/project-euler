num = 600851475143

def find_prime_factor(n):
    i = 2
    while i ** 2 < n:
        while n % i == 0:
            n = n / i
        i = i + 1
    print(int(n))

find_prime_factor(num)