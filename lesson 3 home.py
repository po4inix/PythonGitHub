# ## WHILE
#
# 1. По данному целому числу N распечатайте все квадраты натуральных
# чисел, не превосходящие N, в порядке возрастания.
#
# Например:
# 50      1 4 9 16 25 36 49
# 10      1 4 9
# 9       1 4 9
# 4       1 4
# 1       1
# 100     1 4 9 16 25 36 49 64 81 100
# 99      1 4 9 16 25 36 49 64 81

print('Приступим к программе!')
num = int(input('Введите целое число больше нуля! :'))
perem = 1
while perem ** 2 <= num:
    print(perem ** 2)
    perem = perem + 1
print('Программа выполнила работу, Мой Господин!')



# По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N.
# Выведите показатель степени и саму степень. Операцией возведения в степень, а так же функцией
# возведения в степень пользоваться НЕЛЬЗЯ!

# Например:
# 50          5 32            2 ** 5 = 32
# 10          3 8             2 ** 3 = 8
# 8           3 8             2 ** 3 = 8
# 7           2 4             2 ** 2 = 4
# 1           0 1             2 ** 0 = 1
# 2           1 2             2 ** 1 = 2
# 3           1 2             2 ** 1 = 2
# 4           2 4             2 ** 2 = 4
# 5           2 4             2 ** 2 = 4
# 100         6 64            2 ** 6 = 64
# 1025        10 1024         2 ** 10 = 1024
# 15431543    23 8388608      2 ** 23 = 8388608


print('Приступим к программе!')
num = int(input('Введите натуральное число  : '))
dvoika_v_stepeni = 2
stepen = 1
while dvoika_v_stepeni <= num:
    dvoika_v_stepeni *= 2
    stepen += 1
print(str(num),'     ', stepen - 1, '   ', dvoika_v_stepeni // 2, str('   2 **'), stepen - 1, ' = ', dvoika_v_stepeni // 2 )
print('Программа выполнила работу, Мой Господин!')



# 5. Программа запрашивает ввод последовательности целых чисел, пока не будет введён 0. Как только
# будет введён 0 (ноль), программа должна посчитать и вывести на экран:
# - количество введённых чисел (завершающий 0 не считается)
# - их сумму
# - среднее арифметическое (не считая завершающего числа 0)
# - определить максимальное и минимальное значение
# - определить количество чётных и не чётных элементов в последовательности