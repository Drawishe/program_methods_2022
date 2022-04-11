import unittest
import numpy as np
# from Tasks import task2
from Tasks.task2 import arrZero
from Tasks.task2 import machArr
from Tasks.task2 import machArr2
from Tasks.task2 import machArr3
from Tasks.task2 import machArr4
from Tasks.task2 import machArr5


class tst(unittest.TestCase):
    # Variables with result
    arrZeroResult = np.array([[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]])
    arrZeroResult2 = np.array([[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]])
    arrZero=np.array([[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]])
    arrTest = arrZeroResult2 == arrZero
    # print("\narrZeroResult equal arrZero(machArr input) ->\n",arrTest,"\nComparison End")

    arr= np.array([[[0,0,0],[1,3,0],[2,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[2,0,0],[1,3,0],[0,0,0]],[[3,0,0],[1,0,0],[0,0,0],[0,0,0],[2,0,0]],[[0,0,0],[0,0,0],[0,0,0],[2,0,0],[1,3,0]],[[0,0,0],[0,0,0],[3,0,0],[2,0,0],[1,0,0]]])

    arr2= np.array([[[0,0,0],[1,0,0],[2,0,0],[3,0,0]],[[0,0,0],[1,2,0],[0,0,0],[3,0,0]],[[3,0,0],[0,0,0],[1,2,0],[0,0,0]],[[0,0,0],[3,0,0],[3,0,0],[1,2,0]]])

    arr3= np.array([[[0,0,0],[1,3,0],[2,0,0],[3,0,0],[0,0,0]],[[0,0,0],[1,2,0],[2,0,0],[1,3,0],[0,0,0]],[[3,0,0],[1,0,0],[1,2,0],[0,0,0],[2,0,0]],[[0,0,0],[3,0,0],[3,0,0],[2,1,0],[1,3,0]],[[0,0,0],[0,0,0],[3,0,0],[2,0,0],[1,0,0]]])

    arr4= np.array([[[0,0,0],[1,0,0],[2,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[3,0,0]],[[3,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[2,0,0]]])
    
    arr5= np.array([[[0,0,0],[1,0,0],[2,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[3,0,0]],[[3,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[2,0,0]]])

    def setUp(self) -> None:
        return super().setUp()
    print("\nStart task2 functions testing:\n")
    # Start test arrZero func
    def test_arrZero(self):
        self.assertListEqual(arrZero(5,5,3).tolist(),self.arrZeroResult.tolist())
        print(" arrZero function checked, input (5,5,3)")

    def test_arrZero2(self):
        self.assertListEqual(arrZero(4,4,3).tolist(),self.arrZeroResult2.tolist())
        print("\n arrZero function checked, input (4,4,3)")
        # End Testing arrZero func

    # Start test machArr 1-5 func
    def test_machArr(self):
        self.assertListEqual(machArr(self.arrZeroResult).tolist(),self.arr.tolist())
        print("\n machArr function checked, input (arr-zero)")

    def test_machArr2(self):
        self.assertListEqual(machArr2(self.arrZero).tolist(),self.arr2.tolist())
        print("\n machArr2 function checked, input (arr-zero)")

    def test_machArr3(self):
        self.assertListEqual(machArr3(self.arr).tolist(),self.arr3.tolist())
        print("\n machArr3 function checked, input (arr)")

    def test_machArr4(self):
        self.assertListEqual(machArr4(self.arrZeroResult2).tolist(),self.arr4.tolist())
        print("\n machArr4 function checked, input (arr-zero)")

    def test_machArr5(self):
        self.assertListEqual(machArr5(self.arrZeroResult2).tolist(),self.arr5.tolist())
        print("\n machArr5 function checked, input (arr-zero)")
    # End test machArr 1-5 func
    
if __name__ == "__main__":
       unittest.main()