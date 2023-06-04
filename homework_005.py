# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def func (x,y):
#     if y==1:
#         return x
    
#     return x*func(x,y-1)


# a =  int(input("Input number A"))
# b =  int(input("Input number B"))

# print(func(a,b))


# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*

# 2 2
#     4 


# def sum(a, b):
#     if b==0:
#         return 1
   
#     return a+sum(1,b-1)
    
    
    
# a =  int(input("Input number A"))
# b =  int(input("Input number B"))

# print(sum(a,b))
    
