import unittest

from find_base_converter import base_a_to_base_b
from find_GCD import calculate_gcd
from find_prime_factorization import prime_factorization
from find_smallest_divisor import smallest_divisor
from find_square_root import calculate_square_root
from find_random_number import generate_random_number


class TestMathematicalProblemSolver(unittest.TestCase):

    def test_base_conversion(self):
        self.assertEqual(base_a_to_base_b("1010", 2, 10), "10")

    def test_gcd(self):
        self.assertEqual(calculate_gcd(48, 18), 6)

    def test_prime_factorization(self):
        self.assertEqual(
            prime_factorization(60),
            [2, 2, 3, 5]
        )

    def test_smallest_divisor(self):
        self.assertEqual(smallest_divisor(91), 7)
        self.assertEqual(smallest_divisor(17), 17)

    def test_square_root(self):
        self.assertEqual(calculate_square_root(25), 5.0)
        self.assertIsNone(calculate_square_root(-25))

    def test_random_number(self):
        result = generate_random_number(1, 100)

        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 100)

    def test_invalid_random_range(self):
        self.assertIsNone(generate_random_number(100, 1))


if __name__ == "__main__":
    unittest.main()