i = 0
numbers = []

while i < 6:
    print(f'At the top i is {i}')
    numbers.append(i)

    i += 1
    print(f'Numbers are now: {numbers}')
    print(f'At the bottome i is {i} \n')


print('The numbers: ')

for num in numbers:
    print(num)
