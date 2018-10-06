def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)


def grow(n):
    if n >= 10:
        grow(n // 10) # Imgagine (12345) has grown to 1 12 123
        print(n // 10)
        
def shrink(n):
    if n >= 10:
        print(n // 10)
        shrink(n // 10)

inverse_cascade(12345)
