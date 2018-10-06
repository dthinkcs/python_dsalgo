#1
#12
#123
#1234
#123
#12
#1

def fun(n):
    l = len(str(n))
    for i in range(1, 2*l):
        print(n // (10 **(l-1))) 
        if i < len(str(n)):
            l -= 1
        else:
            l += 1
            
        
                
fun(12345)
