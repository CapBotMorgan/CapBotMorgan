#высота = (ускорение*время^2)/2
h = float(input('Задайте высоту в метрах '))
g = 9.81
s = float(input('Задайте время в секундах '))
y = (g*s**2)/2
print("Мяч пролетел %.2f " % y)


input('Press ENTER to exit')