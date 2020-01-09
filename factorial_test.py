import factorial
import unittest

class factorial_test(unittest.TestCase):
    
    def test_factorial(self):
        self.assertEqual(factorial.factorial(1), 1)
        self.assertEqual(factorial.factorial(2), 2)
        self.assertEqual(factorial.factorial(3), 6)
        self.assertEqual(factorial.factorial(4), 24)
        self.assertEqual(factorial.factorial(5), 120)
        self.assertEqual(factorial.factorial(6), 720)
        self.assertEqual(factorial.factorial(7), 5040)

if __name__ == '__main__':
    unittest.main()
