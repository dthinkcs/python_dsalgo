def count_up(n):
    # Step0: how can I break this problem into smaller parts of the same problem
    # Step1: oh yeah count_up(12) is just first count_up(11) then print(12)
    # Step2: base case: in which case do I dont need to do anywork; its simple; its trivial. HERE WE HAVE RESTRICTED DOMANI n starts from 1
    if n == 1:
        print(1)
        
    count_up(n - 1)
    print(n)
        
count_up(12)
# Step whatever: verify in your mind by drawing the recursion tree diagram
