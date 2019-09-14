def is_palindrome(L):
    for i in range(int(len(L) / 2)):
        if L[i] != L[len(L)-1-i]:
            return False
    return True

# Using recursion
def is_palindrome_rec(L):
    if len(L) <= 1:
        return True
    return L[0] == L[len(L)-1] and is_palindrome_rec(L[1:len(L)-1])
        
# Example
L1=[100,3,4]
L2=[100,3,100]
print(is_palindrome(L1))
print(is_palindrome(L2))
