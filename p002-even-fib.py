import numpy as np

first = 1
fib = [1,2]
fib_even = []
for num in range(4000000):
    if max(fib) < 4000000:
        fib.append(fib[-1]+fib[-2])
print(fib)

for num in fib:
    if num%2 == 0:
        fib_even.append(num)
print(fib_even)

print(sum(fib_even))