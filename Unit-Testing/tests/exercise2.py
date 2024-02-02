import unittest
from function2 import BankAccount

class Test_fuction(unittest.TestCase):
    """to avoid WET we use the setUp"""
    def setUp(self):
        """Set up the bank_account instance so it can be used through out the test"""
        self.bank_account = BankAccount(100)
        
    def test_deposit(self):
        # self.bank_account = BankAccount(100)
        self.bank_account.deposit(100)
        self.assertEqual(self.bank_account.balance, 200)
    def test_withdraw(self):
        # self.bank_account = BankAccount(100)
        self.bank_account.withdraw(50)
        self.assertEqual(self.bank_account.balance, 50)
    
    def test_balance(self):
        self.assertEqual(self.bank_account.balance, self.bank_account.balance)
        
    def tearDown(self) -> None:
        self.bank_account = None




if __name__ == "__main__":
    unittest.main(verbosity=2)