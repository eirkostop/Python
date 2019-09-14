def fibonacci(n):
    if n<0: 
        print("Incorrect input") 
    elif n <= 1:
        return n
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
    if n<0: 
        print("Incorrect input") 
    elif n <= 1:
        return n
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
    
# Example for n=9, Fn=34
print(fibonacci(9))

