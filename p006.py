nums = list(range(1,101,1))

def sum_squares():
    sum_sq = 0
    sq_sum = sum(nums)**2
    for num in nums:
        sum_sq = sum_sq + num**2 #sum of squares of ints in range
    print(sq_sum - sum_sq)

sum_squares()