import os
import sys
import unittest

# Add the current directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Now you can import the hello_world function from solution.py
from solution import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        test_cases = [
            {
                "input": "",
                "expected_output": "Hello World!"
            }
        ]

        for test_case in test_cases:
            input_value = test_case["input"]
            expected_output = test_case["expected_output"]
            actual_output = hello_world()
            self.assertEqual(actual_output, expected_output, f"Test case failed for input: {input_value}")

if __name__ == '__main__':
    unittest.main()
