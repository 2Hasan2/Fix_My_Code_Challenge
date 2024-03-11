#!/usr/bin/python3
""" test FizzBuzz
"""
import unittest
import subprocess


class TestFizzBuzz(unittest.TestCase):
    """ Test FizzBuzz
    """
    def test_fizzbuzz_50(self):
        """ test fizzbuzz 50"""
        expected_output = "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz Fizz 37 38 Fizz Buzz 41 Fizz 43 44 FizzBuzz 46 47 Fizz 49 Buzz"
        process = subprocess.Popen(['./0-fizzbuzz.py', '50'], stdout=subprocess.PIPE)
        actual_output = process.communicate()[0].decode("utf-8").strip()
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
