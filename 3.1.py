num1 = int(input('Введите число: '))
num2 = 0

while num1 > 0:
    d = num1 % 10; #Последняя цифра нашего числа
    num1 = num1 // 10; #Убираем из числа последнюю цифру
    num2 = num2 * 10 #Увеличиваем разрядность второго числа
    num2 = num2 + d #Добавляем цифру
print('Обратное число: ', num2)    
input('Press ENTER to exit')