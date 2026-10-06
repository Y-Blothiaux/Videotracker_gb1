import unittest
import sys
import os.path
sys.path.append("../")
from VideoTracker.src.models.fileRepo import FileRepo


class Test_liste(unittest.TestCase):
    def setUp(self):
        self.__fileContent = '1;2;3;4;5\n1;2;3;4;5'
        self.__filename = 'CSVtest.csv'
        self.path = "./VideoTracker/tests/CSVtest.csv"

    def tearDown(self):
        pass

    def test_saveFile(self):
        FileRepo.saveFile(self.__filename,self.__fileContent)
        self.assertTrue(os.path.exists(self.path))
    
    def  test_Content(self):
        with open('./VideoTracker/tests/CSVtest.csv','r') as f:
            self.assertTrue(f.read() == self.__fileContent)   

if __name__ == '__main__':
    unittest.main(verbosity=2)