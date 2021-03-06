import unittest
import numpy as np
# from Tasks import task1
from Tasks.task1 import miliArr
from Tasks.task1 import muraArr



class tst(unittest.TestCase):
    # Содержимое на входе и выходе функции
    muraInput = np.array([[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']],[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']],[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']],[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']],[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']],[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']],[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']],[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']],[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']],[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']],[[''],[''],[''],[''],[''],[''],[''],[''],[''],[''],['']]])
    muraOut = np.array([[[''],['0'],['2'],['1'],[''],[''],[''],[''],[''],[''],['']],[[''],[''],[''],['1'],[''],['0'],[''],['2'],[''],[''],['']],[[''],[''],[''],['1'],[''],['0'],[''],['2'],[''],[''],['']],[['2'],['0'],[''],[''],[''],[''],[''],[''],[''],['1'],['']],[['2'],['0'],[''],[''],[''],[''],[''],[''],[''],['1'],['']],[[''],[''],[''],[''],[''],['1'],[''],[''],['0'],[''],['2']],[[''],[''],[''],[''],[''],['1'],[''],[''],['0'],[''],['2']],[[''],[''],[''],[''],[''],['1'],[''],[''],['0'],[''],['2']],[[''],[''],[''],[''],['2'],[''],['1'],[''],[''],[''],['0']],[[''],[''],[''],[''],['2'],[''],['1'],[''],[''],[''],['0']],[[''],[''],[''],[''],['2'],[''],['1'],[''],[''],[''],['0']]])

    miliInput = np.array([[['','',''],['','',''],['','',''],['','',''],['','','']],[['','',''],['','',''],['','',''],['','',''],['','','']],[['','',''],['','',''],['','',''],['','',''],['','','']],[['','',''],['','',''],['','',''],['','',''],['','','']],[['','',''],['','',''],['','',''],['','',''],['','','']]], dtype='object')
    miliOut = np.array([[['','',''],['0a','2c',''],['1b','',''],['','',''],['','','']],[['','',''],['','',''],['1b','',''],['0a','2c',''],['','','']],[['2c','',''],['0a','',''],['','',''],['','',''],['1b','','']],[['','',''],['','',''],['','',''],['1a','',''],['0a','2c','']],[['','',''],['','',''],['2c','',''],['1b','',''],['0c','','']]], dtype='object')

    def setUp(self) -> None:
        return super().setUp()
    print("\nНачало тестирования функций:\n")
    # Тестирование функций
    def test_miliArr(self):
        self.assertListEqual(miliArr(self.miliInput).tolist(),self.miliOut.tolist())
        print("\nMILI-функция проверена")

    def test_muraArr(self):
        self.assertListEqual(muraArr(self.muraInput).tolist(),self.muraOut.tolist())
        print("\nMURA-функция проверена")

if __name__ == "__main__":
       unittest.main()