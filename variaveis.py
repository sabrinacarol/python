name = 'Maria'

age = 28
print(f'My name is {name} and I am {age} years old.')

number_1 = int(input('Write a number: '))
number_2 = int(input('Write a other number: '))
if number_1 >= number_2:
    sum_number = number_1 + number_2
    multiplication_number = number_1 * number_2
    division_number = number_1 // number_2
    print(f'The operations the numbers is sum {sum_number}, multiplication\
    {multiplication_number} and division {division_number}.')
elif number_1 or number_2 == 0:
    print('Impossible')
else:
    print('Nothen')