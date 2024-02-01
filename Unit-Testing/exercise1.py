import unittest
from fucntion1 import addFunction, Square
""" Note the setUpModule() runs at the beginnig of the Test its is a module Function and tearDownModule() runs at the end of the  Test
"""
def setUpModule():
    print("starting module")

def tearDownModule():
    print("Runing TearDown")

class TestAddFunction(unittest.TestCase):
    """
       setUpClass(cls) runs Before the Class Test
       tearDownClass(cls) Runs at the End of the class
    """
    """
        The setUp(): runs Executes before Each test and After each test
        The tearDown(): runs Executes before Each test and After each test
    """
    @classmethod
    def setUpClass(cls):
        print("\n", '#' * 10, "Class Test is starting",'#' * 10, "\n")
    
    @classmethod
    def tearDownClass(cls):
        print("\n", '#' * 10, "Tear down running in class", '#' * 10, "\n")
        
    def setUp(self) -> None:
        print(".........Runing........")
    
    def tearDown(self) -> None:
        print('.........Ending........')
    
    def test_posive_num(self):
        
        self.assertEqual(addFunction(2, 2), 4)

    def test_not_equal(self):
        self.assertNotEqual(addFunction(2,2), 5)
        
    def test_negative_num(self):
        self.assertEqual(addFunction(-1, -1), -2)
        
    def test_floats_num(self):
        self.assertEqual(addFunction(1.0, 1), 2.0)
        
    def test_type(self):
        with self.assertRaises(TypeError):
            addFunction('6', 9)
    def test_para_true(self):
        self.assertTrue((5, 8),(int, float))
    def test_is(self):
        a = 5
        b = a
        self.assertIs(a,b)
            
        
class TestSquare(unittest.TestCase):
    def test_area(self):
        area = Square(2).area()
        self.assertEqual(area, 4)
        

if __name__ == "__main__":
    unittest.main(verbosity=2)
    

