floors = input('Give me a number: ')
floors = int(floors)

for i in range(floors):
    print(' ' * (floors - 1 - i) + '*' * (2 * i + 1))

