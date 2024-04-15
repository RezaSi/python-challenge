import os
import sys
import unittest

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now you can import the reverse_string function from solution.py
from solution import reverse_string

class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        test_cases = [
            {
                "expected_output": "olleh",
                "input": "hello"
            },
            {
                "expected_output": "looc si nohtyP",
                "input": "Python is cool"
            },
            {
                "expected_output": "",
                "input": ""
            }
        ]

        for test_case in test_cases:
            input_str = test_case["input"]
            expected_output = test_case["expected_output"]
            actual_output = reverse_string(input_str)
            self.assertEqual(actual_output, expected_output, f"Test case failed for input: {input_str}")

if __name__ == '__main__':
    unittest.main()
    