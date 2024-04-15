import os
import sys
import unittest

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now you can import the is_palindrome function from solution.py
from solution import is_palindrome

class TestPalindromeChecker(unittest.TestCase):
    def test_is_palindrome(self):
        test_cases = [
            {
                "expected_output": True,
                "input": "racecar"
            },
            {
                "expected_output": False,
                "input": "hello"
            },
            {
                "expected_output": True,
                "input": "rotator"
            }
        ]

        for test_case in test_cases:
            input_str = test_case["input"]
            expected_output = test_case["expected_output"]
            actual_output = is_palindrome(input_str)
            self.assertEqual(actual_output, expected_output, f"Test case failed for input: {input_str}")

if __name__ == '__main__':
    unittest.main()