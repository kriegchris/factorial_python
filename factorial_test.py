import factorial
import unittest

class factorial_test(unittest.TestCase):
    
    def test_factorial(self):
        self.assertEqual(factorial.factorial(1), 1)

if __name__ == '__main__':
    unittest.main()
