# how to WRITE recursive functions and prove them
def sum_of_digits(n):
    # how can i break it into smaller parts of the same problem
    # sum_of_digits(n) same as sum_of_digit(n // 10 ) + n%10
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
    
    # base case is correct
    # assuming (T-1) th step is correct
    # I can prove T th step is correct
    
print(sum_of_digits(123456789))
