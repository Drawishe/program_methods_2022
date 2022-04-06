"""
# **Документация к "Конечные автоматы", Задание №2**

## **Алгоритм реализует:**
- *функции объединения и пересечения двух заранее определенных автоматов Мура*
- *генерацию файлов с выводом начальных состояний двух автоматов
и результат работы алгоритма в виде графов*

## **Содержание алгоритма:**
"""
# from re import A
import pydot
from graphviz import Digraph
import matplotlib.pyplot as plt
import numpy as np
from os import remove

# Генерация 3-х мерной матрицы, заполненной 0
def arrZero(i,j,z):
    """
    **Создает пустой массив по заданному размеру матрицы**
    """
    arr = np.zeros(((i*j*z)), int).reshape(i, j, z)
    return arr


def machArr(arr):
    """
    **Заполняет автомат 1 A'**   
    """
    # arr
    # Добавление весов и направлений в автомат А', направления указаны от строки к столбцам,
    # q1'=0 элементу массива, q5'=4 элементу массива
    # К каждому весу прибавлена +1

    arr[0][1][0] = 1
    arr[0][1][1] = 3
    arr[0][2][0] = 2
    arr[1][2][0] = 2
    arr[1][3][0] = 1
    arr[1][3][1] = 3
    arr[2][0][0] = 3
    arr[2][1][0] = 1
    arr[2][4][0] = 2
    arr[3][3][0] = 2
    arr[3][4][0] = 1
    arr[3][4][1] = 3
    arr[4][2][0] = 3
    arr[4][3][0] = 2
    arr[4][4][0] = 1
    return arr

def machArr2(arr2):
    """
    **Заполняет автомат 2 A''**   
    """
    # arr2
    # Добавление весов и направлений в автомат А", направления указаны от строки к столбцам,
    # q1"=0 элементу массива, q4"=3 элементу массива
    # К каждому весу прибавлена +1
    arr2[0][1][0] = 1
    arr2[0][2][0] = 2
    arr2[0][3][0] = 3
    arr2[1][1][0] = 1
    arr2[1][1][1] = 2
    arr2[1][3][0] = 3
    arr2[2][0][0] = 3
    arr2[2][2][0] = 1
    arr2[2][2][1] = 2
    arr2[3][1][0] = 3
    arr2[3][2][0] = 3
    arr2[3][3][0] = 1
    arr2[3][3][1] = 2
    return arr2

def machArr3(arr3):
    """
    **Заполняет автомат 3 "Объединение двух автоматов"**   
    """
    # Объединение автоматов
    # Объединение автоматов - добавление новых дорог к уже имеющемуся A'
    
    
    # arr3
    arr3[0][3][0] = 3
    arr3[1][1][0] = 1
    arr3[1][1][1] = 2
    arr3[2][2][0] = 1
    arr3[2][2][1] = 2
    arr3[3][1][0] = 3
    arr3[3][2][0] = 3
    arr3[3][3][1] = 1
    return arr3

"""
Пересечение двух автоматов
"""
def machArr4(arr4):
    """
    **Заполняет автомат 4 "Пересечение двух автоматов"**   
    """
    # arr4
    arr4[0][1][0] = 1
    arr4[0][2][0] = 2
    arr4[1][3][0] = 3
    arr4[2][0][0] = 3
    arr4[3][3][0] = 2
    return arr4


def machArr5(arr5):
    """
    **Заполняет автомат 5 "Пересечение двух автоматов (2 способ)"**
    """
    # arr5
    arr5[0][1][0] = 1
    arr5[0][2][0] = 2
    arr5[1][3][0] = 3
    arr5[2][0][0] = 3
    arr5[3][3][0] = 2
    return arr5


# Удаление лишних файлов
def remove_cash(file_name):
    """
    **Удаляет лишние файлы, которые были созданы в ходе работы алгоритмов**
    """
    remove(f'{file_name}.dot')


# Блок отрисовки Графов
 ## Вывод графа в файл
def graphRender(graph,graph_name):
    """
    **Отрисовывает построенный граф в png файл**
    """
    # Вывод в файл graph5
    # graph5.render('graph5.gv', view=True)
    graph.save(f'{graph_name}.dot', None)
    (graph,) = pydot.graph_from_dot_file(f'{graph_name}.dot')
    graph.write_png(f'task2_{graph_name}.png')
    remove_cash(graph_name);


# Делаю общую функцию на создание графа
def create_graph(arr,arrNum,graphNum,graphHeader):
    """
    **Создает граф автомата по заданным параметрам**
    """
    graphName = graphNum
    graphNum = Digraph(graphHeader)
    for qNode in range(0, (arrNum.shape[0])):
        # Отрисовка автомата пересечения дорог
        # Создание вершин q1-q...
        graphNum.node(f'{qNode}',(f'q{qNode+1}'))

    # Цикл заполнения переходов
    for i in range(0, arrNum.shape[0]):
        for j in range(0, arrNum.shape[1]):
            for z in range(0, arrNum.shape[2]):
                if arrNum[i][j][z] != 0:
                    temp = arr[i][j][z]
                    temp = temp-1
                    graphNum.edge(f'{i}',f'{j}',f'{temp}')

    # Вывод графа в файл
    graphRender(graphNum,graphName)


def machine_A1(arr,arr2):
    """
    **Отрисовывает первый автомат Мура A'**
    """
    # Отрисовка автомата А'
    graph1 = Digraph(comment="Автомат А'")
    # Создание вершин q1-q5
    colors = ['red']
    graph1.node('0', 'q1')
    graph1.node('1', 'q2')
    graph1.node('2', 'q3', fillcolor="red", style="filled")
    graph1.node('3', 'q4')
    graph1.node('4', 'q5', fillcolor="red", style="filled")

    # Цикл заполнения переходов
    for i in range(0, 5):
        for j in range(0, 5):
            for z in range(0, 3):
                if arr[i][j][z] != 0:
                    temp = arr[i][j][z]
                    temp = temp-1
                    graph1.edge('%s' % (i), '%s' % (j), '%s' % (temp))

    # Вывод в файл graph1
    # print(graph1.source)
    # graph1.render('graph1.gv', view=True)
    # graph1.save('graph1.dot', None)
    # (graph1,) = pydot.graph_from_dot_file('graph1.dot')
    # graph1.write_png('graph1.png')
    graphRender(graph1,'graph1')


def machine_A2(arr,arr2):
    """
    **Отрисовывает второй автомат Мура A''**
    """

    # Отрисовка автомата А"
    graph2 = Digraph(comment="Автомат А''")
    # Создание вершин q1-q4
    graph2.node('0', 'q1')
    graph2.node('1', 'q2')
    graph2.node('2', 'q3', fillcolor="red", style="filled")
    graph2.node('3', 'q4')


    # Цикл заполнения переходов
    for i in range(0, 4):
        for j in range(0, 4):
            for z in range(0, 3):
                if arr[i][j][z] != 0:
                    temp = arr2[i][j][z]
                    temp = temp-1
                    # graph2.edge('%s' % (i), '%s' % (j), '%s' % (temp))
                    graph2.edge(f'{i}',f'{j}',f'{temp}')

    graphRender(graph2,'graph2')


def main():
    """
    **Начало работы программы**
    """
    # Создание массива под автомат А'
    arr = arrZero(5,5,3)
    arr = machArr(arr)
    # Отрисовка графа первой машины
    machine_A1(arr,arr)

    # Создание массива под автомат А"
    arr2 = arrZero(4, 4, 3)
    arr2 = machArr2(arr2)
    # Отрисовка графа второй машины
    machine_A2(arr,arr2)

    # Объединение языков двух автоматов
    arr3 = machArr3(arr)
    # Отрисовка графа объединения автоматов
    create_graph(arr,arr3,'graph3','Объединенные автоматы')

    # Пересечение языков двух автоматов (дороги и веса)
    arr4 = arrZero(4,4,3)
    arr4 = machArr4(arr4)
    # Отрисовка автомата пересечения дорог и весов
    create_graph(arr,arr4,'graph4','Автомат пересечения дорог и весов')

    # Пересечение языков двух автоматов (дороги)
    arr5 = arrZero(4,4,3)
    arr5 = machArr5(arr5)
    # Отрисовка автомат пересечения дорог
    create_graph(arr,arr5,'graph5','Автомат пересечения дорог')
    return


# print(type(arr4.shape));
# print(arr4.shape[0]);
# Pdoc: python -m pdoc --html . --output-dir html/ --force
# Pdoc single: python -m pdoc --html Eremin/Task_2.py --output-dir . --force
# Pdoc group: python -m pdoc --html . --force