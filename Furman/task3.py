# Импорты: 
import matplotlib.pyplot as plt
import numpy as np
import pydot
import os
from graphviz import Digraph

# Создание массива под автомат А'
arr=np.zeros(75, int).reshape(5,5,3)
print('Вывод нулевого массива: ')
print(arr)
print('Старт программы')


# Добавление весов и направлений в автомат А', направления указаны от строки к столбцам, 
# q1'=0 элементу массива, q5'=4 элементу массива
# К каждому весу прибавлена +1
arr[0][1][0]=1
arr[0][1][1]=3
arr[0][2][0]=2
arr[1][2][0]=2
arr[1][3][0]=1
arr[1][3][1]=3
arr[2][0][0]=3
arr[2][1][0]=1
arr[2][4][0]=2
arr[3][3][0]=2
arr[3][4][0]=1
arr[3][4][1]=3
arr[4][2][0]=3
arr[4][3][0]=2
arr[4][4][0]=1
print('Вывод заполненного массива: ')
print(arr)

# Отрисовка автомата А', выбор финальных состояний

graph1= Digraph(comment="Автомат А'")
# Создание вершин q1-q5
colors=['red']

# a=int(input('q1 конечное состояние? 1 - да, 0 - нет: '))
# b=int(input('q2 конечное состояние? 1 - да, 0 - нет: '))
# c=int(input('q3 конечное состояние? 1 - да, 0 - нет: '))
# d=int(input('q4 конечное состояние? 1 - да, 0 - нет: '))
# e=int(input('q5 конечное состояние? 1 - да, 0 - нет: '))

# Заполнение стоковыми значениями
a=0
b=0
c=1
d=0
e=1


if a==1:
    graph1.node('0','q1',fillcolor="red",style="filled")
else:
    graph1.node('0','q1')
if b==1:
    graph1.node('1','q2',fillcolor="red",style="filled")
else:
    graph1.node('1','q2')
if c==1:
    graph1.node('2','q3',fillcolor="red",style="filled")
else:
    graph1.node('2','q3')
if d==1:
    graph1.node('3','q4',fillcolor="red",style="filled")
else:
    graph1.node('3','q4')
if e==1:
    graph1.node('4','q5',fillcolor="red",style="filled")
else:
    graph1.node('4','q5')
    

# Цикл заполнения переходов

for i in range(0,5):
    for j in range(0,5):
        for z in range(0,3):
            if arr[i][j][z] != 0:
                temp = arr[i][j][z]
                temp = temp-1
                graph1.edge(f'{i}',f'{j}',f'{temp}')
                
# print(graph1.source) 

graph1.save('graph1.dot', None)
(graph1,) = pydot.graph_from_dot_file('graph1.dot')
graph1.write_png('graph1.png')
# display(Image(filename='graph1.png'))
os.remove('graph1.dot')

# print('Вывод массива: ')
# print(arr)


# Отрисовка автомата А' с дополнененным языком
graph1= Digraph(comment="Автомат А'")
# Создание вершин q1-q5
colors=['red']

if a==0:
    graph1.node('0','q1',fillcolor="red",style="filled")
else:
    graph1.node('0','q1')
if b==0:
    graph1.node('1','q2',fillcolor="red",style="filled")
else:
    graph1.node('1','q2')
if c==0:
    graph1.node('2','q3',fillcolor="red",style="filled")
else:
    graph1.node('2','q3')
if d==0:
    graph1.node('3','q4',fillcolor="red",style="filled")
else:
    graph1.node('3','q4')
if e==0:
    graph1.node('4','q5',fillcolor="red",style="filled")
else:
    graph1.node('4','q5')
    
# Цикл заполнения переходов

for i in range(0,5):
    for j in range(0,5):
        for z in range(0,3):
            if arr[i][j][z] != 0:
                temp = arr[i][j][z]
                temp = temp-1
                graph1.edge(f'{i}',f'{j}',f'{temp}')
                


# print(graph1.source) 
graph1.save('graph2.dot', None)
(graph1,) = pydot.graph_from_dot_file('graph2.dot')
graph1.write_png('graph2.png')
os.remove('graph2.dot')
# print('Вывод массива: ')
# print(arr)



print('Завершение программы')