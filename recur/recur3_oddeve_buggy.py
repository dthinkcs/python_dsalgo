def is_even(n):
    if n == -2:
        return True
    return not is_odd(n - 2)
        
def is_odd(n):    
    if n == -1:
        return True
    return not is_even(n - 2)
    
print(is_odd(10))
