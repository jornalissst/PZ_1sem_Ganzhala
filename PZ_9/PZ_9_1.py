# Вариант 4
# Дан словарь с четным количеством элементов.
# Найти суммы значений элементов первой и второй половин с использованием функции. Результаты вывести на экран.
SL = {}
i = 0
for i in range(8):
    SL[i] = i + 1
print(SL)
sum1 = 0
for i in range(4):
    sum1 = sum1 + SL[i]
print("Сумма чисел первой половины :", sum1)
sum2 = 0
for i in range(4, 8):
    sum2 = sum2 + SL[i]
print("Сумма чисел второй половины :", sum2)
