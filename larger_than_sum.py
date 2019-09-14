def larger_than_sum(L):
    for i in range(len(L)):
        s = 0
        for z in range(i+1, len(L)):
            s = s + L[z]
        if L[i] <= s:
            return False
    return True

# Alternatively
def larger_than_sum_2(L):
    for i in range(len(L)):
        if L[i] <= sum(L[i+1:len(L)]):
            return False
    return True

# Examples
L1 = [100, 50, 40, 5, 1]
L2 = [10, 50, 40, 5, 1]
print(larger_than_sum(L1))
print(larger_than_sum(L2))
