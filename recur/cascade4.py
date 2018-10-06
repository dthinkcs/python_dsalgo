def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)


def grow(n):
    if n >= 10:
        grow(n // 10) # IHOP
        print(n // 10)
        
def shrink(n):
    if n >= 10:
        print(n // 10) # IHOP
        shrink(n // 10)

inverse_cascade(12345)
