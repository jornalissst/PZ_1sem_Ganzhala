try:
    cost = float(input('Введите цену за 1 кг: '))
    a = 0
    while a < 0.9:
        a += 0.1
        print(f'Цена {round(a, 2)} кг - {round(cost*a,2)} рублей')
except ValueError:
    print('Введите число!!!')
