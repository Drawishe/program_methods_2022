import matplotlib.pyplot as plt
import numpy as np
arr=np.zeros(75, int).reshape(5,5,3)
# arr
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
# arr




# Создание массива под автомат А"
arr2=np.zeros(48, int).reshape(4,4,3)
# arr2



# Добавление весов и направлений в автомат А", направления указаны от строки к столбцам, 
# q1"=0 элементу массива, q4"=3 элементу массива
# К каждому весу прибавлена +1
arr2[0][1][0]=1
arr2[0][2][0]=2
arr2[0][3][0]=3
arr2[1][1][0]=1
arr2[1][1][1]=2
arr2[1][3][0]=3
arr2[2][0][0]=3
arr2[2][2][0]=1
arr2[2][2][1]=2
arr2[3][1][0]=3
arr2[3][2][0]=3
arr2[3][3][0]=1
arr2[3][3][1]=2
# arr2



# Объединение автоматов
# Объединение автоматов - добавление новых дорог к уже имеющемуся
arr3=arr
# arr3
arr3[0][3][0]=3
arr3[1][1][0]=1
arr3[1][1][1]=2
arr3[2][2][0]=1
arr3[2][2][1]=2
arr3[3][1][0]=3
arr3[3][2][0]=3
arr3[3][3][1]=1
# arr3



# Пересечение языков двух автоматов (дороги и веса)
arr4=np.zeros(75, int).reshape(5,5,3)

arr4[0][1][0]=1
arr4[0][2][0]=2
arr4[1][3][0]=3
arr4[2][0][0]=3
arr4[3][3][0]=2

# arr4




# Пересечение языков двух автоматов (дороги)
arr5=np.zeros(75, int).reshape(5,5,3)

arr5[0][1][0]=1
arr5[0][2][0]=2
arr5[1][3][0]=3
arr5[2][0][0]=3
arr5[3][3][0]=2

# arr5



# Отрисовка автомата А'
from graphviz import Digraph
graph1= Digraph(comment="Автомат А'")
# Создание вершин q1-q5
colors=['red']
graph1.node('0','q1')
graph1.node('1','q2')
graph1.node('2','q3',fillcolor="red",style="filled")
graph1.node('3','q4')
graph1.node('4','q5',fillcolor="red",style="filled")

# Цикл заполнения переходов

for i in range(0,5):
    for j in range(0,5):
        for z in range(0,3):
            if arr[i][j][z] != 0:
                temp = arr[i][j][z]
                temp = temp-1
                graph1.edge('%s'%(i),'%s'%(j),'%s'%(temp))
                
# print(graph1.source) 
import pydot
graph1.render('graph1.gv', view=True)
# graph1
# arr

# Отрисовка автомата А"
from graphviz import Digraph
graph2= Digraph(comment="Автомат А''")
# Создание вершин q1-q4
graph2.node('0','q1')
graph2.node('1','q2')
graph2.node('2','q3',fillcolor="red",style="filled")
graph2.node('3','q4')

# Цикл заполнения переходов

for i in range(0,4):
    for j in range(0,4):
        for z in range(0,3):
            if arr[i][j][z] != 0:
                temp = arr2[i][j][z]
                temp = temp-1
                graph2.edge('%s'%(i),'%s'%(j),'%s'%(temp))
                
import pydot
graph2.render('graph2.gv', view=True)
# graph2

# Отрисовка графа объединения автоматов
from graphviz import Digraph
graph3= Digraph(comment="Объединенные автоматы")
# Создание вершин q1-q5
graph3.node('0','q1')
graph3.node('1','q2')
graph3.node('2','q3')
graph3.node('3','q4')
graph3.node('4','q5')

# Цикл заполнения переходов

for i in range(0,5):
    for j in range(0,5):
        for z in range(0,3):
            if arr3[i][j][z] != 0:
                temp = arr[i][j][z]
                temp = temp-1
                graph3.edge('%s'%(i),'%s'%(j),'%s'%(temp))
                
    

import pydot
graph3.render('graph3.gv', view=True)
# graph3

# Отрисовка автомата пересечения дорог и весов
from graphviz import Digraph
graph4= Digraph(comment="Автомат пересечения дорог и весов")
# Создание вершин q1-q5
graph4.node('0','q1')
graph4.node('1','q2')
graph4.node('2','q3')
graph4.node('3','q4')
# graph4.node('4','q5')

# Цикл заполнения переходов

for i in range(0,5):
    for j in range(0,5):
        for z in range(0,3):
            if arr4[i][j][z] != 0:
                temp = arr[i][j][z]
                temp = temp-1
                graph4.edge('%s'%(i),'%s'%(j),'%s'%(temp))
                
    

import pydot
graph4.render('graph4.gv', view=True)
# graph4


# Отрисовка автомата пересечения дорог
from graphviz import Digraph
graph5= Digraph(comment="Автомат пересечения дорог")
# Создание вершин q1-q5
graph5.node('0','q1')
graph5.node('1','q2')
graph5.node('2','q3')
graph5.node('3','q4')
# graph5.node('4','q5')

# Цикл заполнения переходов

for i in range(0,5):
    for j in range(0,5):
        for z in range(0,3):
            if arr5[i][j][z] != 0:
                temp = arr[i][j][z]
                temp = temp-1
                graph5.edge('%s'%(i),'%s'%(j),'%s'%(temp))
                
    

import pydot
graph5.render('graph5.gv', view=True)
# graph5



