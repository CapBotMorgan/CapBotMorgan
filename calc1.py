operation = input('''Выберите знак 
- минус
+ плюс
* умножение
/ деление
''')
num_1 = int(input('Введите число 1: '))
num_2 = int(input('Введите число 2: '))
if operation == '+':
    print('{} + {} ='.format(num_1, num_2)) 
    print(num_1 + num_2)
elif operation == '-':
    print('{} - {} ='.format(num_1, num_2))
    print(num_1 - num_2)
elif operation == '*':
    print('{} * {} ='.format(num_1, num_2))
    print(num_1 * num_2)
elif operation == '/':
    print('{} / {} ='.format(num_1, num_2))
    print(num_1 / num_2)
else:
    print('такой функции нет')

input('Press ENTER to exit')


