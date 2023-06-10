# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного 
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга 
# пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите 
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывода
# Парам пам-пам

# str = "пара-ра-рам рам-пам-папам па-ра-па-дам"
# list_1 = str.split()
# list_2 = []
# list_3 = ['а', 'о', 'у', 'и', 'ю', 'я', 'э', 'ы', 'е']

# def slogi(fraza):
#     count = 0 
#     fraza = fraza.lower()
    
#     for i in range(len(fraza)):
#         for j in range(len(list_3)):
#             if fraza[i]==list_3[j]:
#                 count+=1
#     return count
  
# for i in range(len(list_1)):
#     list_2.append(slogi(list_1[i]))
    
# if len(set(list_2)) == 1:
#     print("Парам пам-пам")
# else:
#     print("Пам пара")
    


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть 
# распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как,
# например, у операции умножения.
#
# 
# Ввод: Вывод:
# 12
#          print_operation_table(lambda x, y: x * y)
#  3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24



# def print_operation_table(operation, a, b):
#     for i in range(1, a+1):
#         print()
#         for j in range(1, b+1):
#             print(operation(i,j), end = ' ')
        

# print_operation_table(lambda x, y: x * y, 6, 6)
    
    
    
    
    