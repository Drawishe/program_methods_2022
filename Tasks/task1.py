"""
# **Документация к "Конечные автоматы", Задание №1**

## **Алгоритм реализует:**
- *построение автомата Мили*
- *построение автомата Мура*
- *генерацию файлов с выводом состояний двух автоматов в виде графов*

## **Содержание программы:**
"""
from re import A
import pydot
from graphviz import Digraph
import matplotlib.pyplot as plt
import numpy as np
from os import remove


def arrEmpty(i,j,z):
    """
    **Создает пустой массив по заданному размеру матрицы**
    """
    arr = np.array(np.zeros(((i*j*z)), str).reshape(i, j, z),dtype='object')
    return arr

def miliArr(arr):
    """
    **Заполнение автомата Мили**   
    """
    # Добавление весов (вход, выход) и направлений автомату Мили,
    # направления указаны от строки к столбцам,
    # Номер вершины q = "Элемент массива"+1

    arr[0][1][0] = '0a'
    arr[0][1][1] = '2c'
    arr[0][2][0] = '1b' 
    arr[1][2][0] = '1b'
    arr[1][3][0] = '0a'
    arr[1][3][1] = '2c'
    arr[2][0][0] = '2c'
    arr[2][1][0] = '0a'
    arr[2][4][0] = '1b'
    arr[3][3][0] = '1a'
    arr[3][4][0] = '0a'
    arr[3][4][1] = '2c'
    arr[4][2][0] = '2c'
    arr[4][3][0] = '1b'
    arr[4][4][0] = '0c'
    return arr



def muraArr(arr):
    """
    **Заполнение автомата Мура**   
    """
    # Добавление весов (вход, выход) и направлений автомату Мили,
    # направления указаны от строки к столбцам,
    # Номер вершины q = "Элемент массива"+1
    # Обозначения соответствуют вершинам Автомата Мили
    # q1
    arr[0][1][0] = '0'
    arr[0][2][0] = '2'
    arr[0][3][0] = '1'

    # q2
    arr[1][3][0] = '1'
    arr[1][5][0] = '0'
    arr[1][7][0] = '2'

    arr[2][3][0] = '1'
    arr[2][5][0] = '0'
    arr[2][7][0] = '2'

    # q3
    arr[3][0][0] = '2'
    arr[3][1][0] = '0'
    arr[3][9][0] = '1'

    arr[4][0][0] = '2'
    arr[4][1][0] = '0'
    arr[4][9][0] = '1'

    # q4 
    arr[5][5][0] = '1'
    arr[5][8][0] = '0'
    arr[5][10][0] = '2'

    arr[6][5][0] = '1'
    arr[6][8][0] = '0'
    arr[6][10][0]= '2'

    arr[7][5][0] = '1'
    arr[7][8][0] = '0'
    arr[7][10][0]= '2'

    # q5
    arr[8][4][0] = '2'
    arr[8][6][0] = '1'
    arr[8][10][0]= '0'

    arr[9][4][0] = '2'
    arr[9][6][0] = '1'
    arr[9][10][0]= '0'

    arr[10][4][0] ='2'
    arr[10][6][0] ='1'
    arr[10][10][0]='0'

    return arr


# Передает значения выходов для вершин Мура
def nodeName(arr):
    """
    **Передает значения выходов для вершин автомата Мура**
    """
    # 11 выходов + 9 пустых
    arr = ['c','a','c','b','c','a','b','c','a','b','c','','','','','','','','','']
    return arr

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
    graph.write_png(f'task1_{graph_name}.png')
    remove(f'{graph_name}.dot')


# Делаю общую функцию на создание графа
def create_graph(arr,arrNum,graphNum,graphHeader):
    """
    **Создает граф автомата по заданным параметрам**
    """
    graphName = graphNum
    graphNum = Digraph(graphHeader)
    # Здесь происходит создание вершин по заданным параметрам
    if arr.shape[1]<8:
        for qNode in range(0, (arrNum.shape[0])):
            # Отрисовка вершин автомата Мили
            # Создание вершин q1-q...
            graphNum.node(f'{qNode}',(f'q{qNode+1}'))
    else:
        qName = nodeName(arr)
        for qNode in range(0, (arrNum.shape[0])):
            # Отрисовка вершин автомата Мура
            # Создание вершин q1-q...
            graphNum.node(f'{qNode}',(f'q{str(int(qNode)+1)}'+' '+f'{str(qName[qNode])}'))

    # Цикл заполнения переходов
    for i in range(0, arrNum.shape[0]):
        for j in range(0, arrNum.shape[1]):
            for z in range(0, arrNum.shape[2]):
                if arrNum[i][j][z] != '':
                    temp = arr[i][j][z]
                    graphNum.edge(f'{i}',f'{j}',f'{temp}')

    # Вывод графа в файл
    graphRender(graphNum,graphName)



def main():
    """
    **Главная функция реализации программы**
    """
    # МИЛИ
    arrMili = arrEmpty(5,5,3)
    arrMili = miliArr(arrMili)
    # Отрисовка автомата
    create_graph(arrMili,arrMili,'graphMili','Автомат Мили')

    # МУРА
    arrMura = arrEmpty(11,11,1)
    arrMura = muraArr(arrMura)
    # Отрисовка автомата
    create_graph(arrMura,arrMura,'graphMura','Автомат Мура')
#Вызов главной функции
main()