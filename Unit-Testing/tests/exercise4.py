import unittest
from sys import platform
@unittest.skip("Work in progress")
class Test_skipClass(unittest.TestCase):
    """Skipping a testmethod in unittest"""
    def test_test_case_1(self):
        self.assertEqual(1 + 1, 2)
    
    # """Use one of the method which is @unittest.skip(prompt)"""
    # @unittest.skip('Work in progress Method 1')    
    def test_test_case_2(self):
        pass
    
    # """Use one of the method which is skipTest(prompt)"""
    def test_test_case_3(self):
        # self.skipTest('Work in progress MEthod 2')
        pass
    def test_test_case_3(self):
        # raise unittest.SkipTest("Work in progress Method 3")
        pass

"""Skip a test with  a condition"""
class Test_skipif(unittest.TestCase):
    
    def test_case_1(self):
        self.assertEqual(1 + 1, 2)
    
    # @unittest.skipIf(condition, reason)
    @unittest.skipIf(False, "condition doesnt have to be true for it to skip it can be either false or true ")
    def test_case_2(self):
        self.assertIsNotNone([])
        
    @unittest.skipUnless(True, 'condition is True so skip')
    def test_case_3(self):
        self.assertNotEqual(1 + 3, 3)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)