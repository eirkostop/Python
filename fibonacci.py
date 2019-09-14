def fibonacci(n):
    #make sure n is a positive integer
    if isinstance(n, int)!=True or n<0:
        raise ValueError("That is not a positive integer.")
    #F0=0 and F1=1
    elif n <= 1:
        return n
    #Fn=Fn-1 + Fn-2
    second_last = 0
    last = 1
    index=1
    while index<n:
        current = second_last + last
        second_last = last
        last=current
        index+=1
    return current

# Using recursion
def fibonacci_rec(n):
    if isinstance(n, int)!=True or n<0:
        raise ValueError("That is not a positive integer.") 
    elif n <= 1:
        return n
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
    
# Example for n=9, Fn=34

try:
    print(fibonacci(-9))
    pass
except ValueError as ve:
    print(ve)
    pass

