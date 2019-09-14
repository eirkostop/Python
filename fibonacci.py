def fibonacci(n):
    if n<0: 
        print("Incorrect input") 
    elif n <= 1:
        return n
    last = 1
    current = 1
    for i in range(2, n):
        temp = current + last
        last = current
        current = temp
    return temp

# Alternatively, with recursion
def fibonacci_rec(n):
    if n<0: 
        print("Incorrect input") 
    elif n <= 1:
        return n
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)
    
# Example for n=9, Fn=34
print(fibonacci(9))