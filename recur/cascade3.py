def inverse_cascade(n, hide):
    if n < 10:
        print(n)
    else:
        print(n // (10 ** (hide)))
        inverse_cascade(n, hide - 1) # IHOP Imagine: 12345 or n you have hiddent one less and completed the process so 12 123 1234 12345 1234 12 is completed
        print(n // (10 ** (hide)))
    
inverse_cascade(12345, 4)
