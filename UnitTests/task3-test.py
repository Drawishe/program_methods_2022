from asyncio import Task, tasks
import unittest
import numpy as np
from Tasks.task3 import matrix_change
from Tasks.task3 import make_peaks
from Tasks.task3 import peak_reverse

array=np.zeros(75,int).reshape(5,5,3)
array_check=np.array([[[0,0,0],[1,3,0],[2,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[2,0,0],[1,3,0],[0,0,0]],[[3,0,0],[1,0,0],[0,0,0],[0,0,0],[2,0,0]],[[0,0,0],[0,0,0],[0,0,0],[2,0,0],[1,3,0]],[[0,0,0],[0,0,0],[3,0,0],[2,0,0],[1,0,0]]])
peak=[0,0,0,0,0]
peak_check=[0,0,1,0,1]
peak_checkr=[0,0,1,0,1]
reverse_peak=[1,1,0,1,0]
array.tolist()

class tst(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
 
    def test_matrix_change(self):
        self.assertListEqual(matrix_change(array).tolist(),array_check.tolist())
        print('Matrix check done')

    def test_peaks_change(self):
        self.assertListEqual(make_peaks(peak), peak_check)
        print('Natural peaks check done')
    
    def test_peak_reverse(self):
        self.assertListEqual(peak_reverse(peak_checkr),reverse_peak)
        print('Revers peaks check done')

        
if __name__ == "__main__":
  unittest.main()