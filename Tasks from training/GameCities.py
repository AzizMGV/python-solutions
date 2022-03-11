string_first = input()
string_second = input()
string_first = string_first.lower()
string_second = string_second.lower()
if string_first[-1] == string_second[0]:
    print('Good')
elif string_first[-1] == 'ь' and string_first[-2] == string_second[0]:
        print('Good')
else:
    print('Bad')


"""
При игре в "Города" игроки по очереди называют названия городов так, чтобы первая буква каждого нового слова совпадала с последней буквой предыдущего. 
При этом считают, что если последняя буква предыдущего слова — мягкий знак, то с первой буквой следующего слова надо сравнивать букву, предшествующую мягкому знаку.

Напишите программу, которая считывает подряд две строки, после чего выводит «Good», если последний символ первой строки совпадает с первым символом второй (с учётом правила про мягкий знак), и «Bad» в противном случае.

Sample Input 1:
  Лондон
  Норильск
    
Sample Output 1:
  Good
  
Sample Input 2:
  Тверь
  Роттердам
    
Sample Output 2:
  Good  
"""
