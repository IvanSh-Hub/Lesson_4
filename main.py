# import math
#
#
# d = 0.0001
#
# def showPi(d):
#     num = abs(str(d).find('.') - len(str(d)) + 1)
#     print("{:.{}f}".format(math.pi, num))
#
# showPi(d)


#---------------------------------------------------------------------------------------------------------------------------------------------

#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# n = int(input("Enter a number N: "))

# n = 270
#
# array = []
#
# for i in range(2, n):
#     if n%i == 0:
#         array.append(i)
#
# print(array)

#---------------------------------------------------------------------------------------------------------------------------------------------

#Задайте последовательность чисел.
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#
# myList = [1, 5, 4, 5, 6, 8, 7, 8, 9, 1, 1, 6, 5];
#
# mySet = set(myList)
#
# print(mySet)

#---------------------------------------------------------------------------------------------------------------------------------------------



# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#
# Пример:
#
#  k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

#
# import random
#
# indexes = {0: "\u2070", 1: "\u00B9", 2: "\u00B2", 3: "\u00B3", 4: "\u2074", 5: "\u2075", 6: "\u2076", 7: "\u2077", 8: "\u2078", 9: "\u2079"}
#
# k = int(input("Enter a degree of equation: "))
#
# if k > 9 or k < 0:
#     print("You entered wrong number: k must be between 0 and 9 incld")
# else:
#     i = k
#     while i >= 1:
#         if i > 1:
#             print("{}*x{}".format(random.randrange(0, 100),indexes[i]), end=" + ")
#         else:
#             print("{}*x".format(random.randrange(0, 100)), end=" + ")
#         i -= 1
#     print(str(random.randrange(0,100)) + " = 0")


























