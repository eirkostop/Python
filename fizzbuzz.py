n = input('Give me a number: ')
n = int(n)

for i in range(n+1):
    if i / 3 == int(i / 3) and i / 5 == int(i / 5):
        print('FizzBuzz')
    elif i / 5 == int(i / 5):
        print('Buzz')
    elif i / 3 == int(i / 3):
        print('Fizz')
    else:
        print(i)

