""" 
# **Документация к заданию №3 из темы "Конечные автоматы"**
# **Выполнил студент уч.гр. 181-331 Фурман Кирилл**
## **Данный алгоритм реализует:**
-*функцию дополнения языка для заданного автомата*


## **Содержание алгоритма:**
"""



# Импорты: 
import matplotlib.pyplot as plt
import numpy as np
import pydot
import os
from graphviz import Digraph


def matrix_change(arr):
    """

    **Функция заполнения матрицы дорог и весов для нужного нам конечного автомата**

    """
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
    return(arr)

def make_peaks(peak):
    """
    **Функция заполнения конечных состояний стоковыми значениями**
    """
    peak=[0,0,1,0,1]
    return(peak)

def peak_reverse(peak):
    """
    **Функция изменения конечных состояний в заданном автомате**
    """
    for i in range(0,5):
        if peak[i] == 1:
            peak[i]=0
        else:
            peak[i]=1
    return(peak)

def make_graph(num,arr,graph1,colors,peak):
    """
    **Функция отрисовки графа**
    """
    for i in range(0,5):
        if peak[i] == 1:
            graph1.node(f'{i}',f'q{i+1}',fillcolor="red",style="filled")
        else:
            graph1.node(f'{i}',f'q{i+1}')
    # Цикл заполнения переходов

    for i in range(0,5):
        for j in range(0,5):
            for z in range(0,3):
                if arr[i][j][z] != 0:
                    temp = arr[i][j][z]
                    temp = temp-1
                    graph1.edge(f'{i}',f'{j}',f'{temp}')
    
    graph1.save(f'graph{num}.dot', None)
    (graph1,) = pydot.graph_from_dot_file(f'graph{num}.dot')
    graph1.write_png(f'graph{num}.png')
    # display(Image(filename='graph1.png'))
    os.remove(f'graph{num}.dot')



def main():
    """
    **Основная функция работы программы: **
    """
    # Создание массива под автомат А'
    arr=np.zeros(75, int).reshape(5,5,3)
    print('Вывод нулевого массива: ')
    print(arr)
    print('Старт программы')


    # Добавление весов и направлений в автомат А', направления указаны от строки к столбцам, 
    # q1'=0 элементу массива, q5'=4 элементу массива
    # К каждому весу прибавлена +1
    matrix_change(arr)

    print('Вывод заполненного массива: ')
    print(arr)

    # Отрисовка автомата А', выбор финальных состояний

    graph1= Digraph(comment="Автомат А'")
    # Создание вершин q1-q5
    colors=['red']
    peak=np.zeros(5,int)
    peak=make_peaks(peak)
    num=int(1)
    make_graph(num,arr,graph1,colors,peak)



    # a=int(input('q1 конечное состояние? 1 - да, 0 - нет: '))
    # b=int(input('q2 конечное состояние? 1 - да, 0 - нет: '))
    # c=int(input('q3 конечное состояние? 1 - да, 0 - нет: '))
    # d=int(input('q4 конечное состояние? 1 - да, 0 - нет: '))
    # e=int(input('q5 конечное состояние? 1 - да, 0 - нет: '))

    # Заполнение стоковыми значениями
    # Отрисовка автомата А' с дополнененным языком
    graph1= Digraph(comment="Автомат А'")
    # Создание вершин q1-q5
    # colors=['red']
    peak_reverse(peak)
    num=int(2)
    make_graph(num,arr,graph1,colors,peak)

    print('Завершение программы')