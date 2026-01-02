import unittest
from solution import is_prime

class TestIsPrime(unittest.TestCase):
    def test_negative_numbers(self):
        self.assertFalse(is_prime(-10))
        self.assertFalse(is_prime(-1))

    def test_zero_and_one(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_small_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_small_composite_numbers(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(15))

    def test_large_prime(self):
        self.assertTrue(is_prime(104729))

    def test_large_composite(self):
        self.assertFalse(is_prime(104728))

if __name__ == "__main__":
    unittest.main()

