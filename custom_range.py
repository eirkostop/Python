def custom_range(start, end, step):
    L = []
    next = start
    while next < end:
        L.append(next)
        next = next + step
    return L

for i in custom_range(1, 10, 2):
    print(i)
    
#the function does what the built in function "range(start, end, step)" does. We could have written directly
#for i in range(1, 10, 2):
#    print(i)
