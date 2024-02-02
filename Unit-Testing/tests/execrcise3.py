import unittest

class Test_skipMethod(unittest.TestCase):
    """Skipping a testmethod in unittest"""
    def test_test_case_1(self):
        self.assertEqual(1 + 1, 2)
    
    # """Use one of the method which is @unittest.skip(prompt)"""
    @unittest.skip('Work in progress Method 1')    
    def test_test_case_2(self):
        pass
    
    # """Use one of the method which is skipTest(prompt)"""
    def test_test_case_3(self):
        self.skipTest('Work in progress MEthod 2')
    
    def test_test_case_3(self):
        raise unittest.SkipTest('work in progress method 3')


if __name__ == "__main__":
    unittest.main(verbosity=2)