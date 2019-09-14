def FizzBuzz(n):
    for i in range(1,n+1):
        if i / 3 == int(i / 3) and i / 5 == int(i / 5):
            print('FizzBuzz')
        elif i / 5 == int(i / 5):
            print('Buzz')
        elif i / 3 == int(i / 3):
            print('Fizz')
        else:
            print(i)

# Alternatively
def FizzBuzz2(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%3==0:
            print('Fizz')
        elif i%5==0:
            print ('Buzz')
        else: print(i)

# Example
n = input('Give me a number: ')
n = int(n)
FizzBuzz(n)