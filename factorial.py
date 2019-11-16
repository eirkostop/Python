def athroisma(n):
    result = 0
    for i in range(1, n+1):
        result = result + i
    return result

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

n = input('Give me a number: ')
n = int(n)
print('To athroisma einai ' + str(athroisma(n)))
print('To paragontiko einai ' + str(factorial(n)))
