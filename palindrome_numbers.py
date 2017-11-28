"""
    Cameron Johnson
    November 2017
"""

import math

class PalindromeNumbers():

    @staticmethod
    def convert_num_to_base(i, b):
        """
        i = number to convert
        b = base

        Returns an array of integers, representing the characters
        of the number converted to the base
        """
        if i < 0:
            raise Exception("Error: Negative numbers not supported")
        if b < 2:
            raise Exception("Error: Bases less than 2 not supported")
        r = []
        power = int(math.floor(math.log(i, b)))
        processing = i
        while power >= 0:
            digit = 0
            while processing - pow(b, power) >= 0:
                processing -= pow(b, power)
                digit += 1
            r.append(digit)
            power -= 1
        return r

    @staticmethod
    def is_palindrome(s):
        """
            s = string to test

            Returns whether the given string is a palindrome
        """
        le = len(s)
        if le <= 1:
            return True
        for i, v in enumerate(s):
            if i >= (le/2):
                return True
            if v != s[-i-1]:
                break 
        return False

    @staticmethod
    def find_palindromes(n):
        """
            n = numbers to check

            Find the lowest base in which a range of numbers
            is a palindrome.
        """
        results = [None] * n
        for b in range(2, n):       # loop through all bases
            pending = [i + 1 for i, v in enumerate(results) if v == None]
            found = [p for p in pending if PalindromeNumbers.is_palindrome(PalindromeNumbers.convert_num_to_base(p, b))]
            for i, f in enumerate(found):
                results[f - 1] = b
            if len([r for r in results if r is not None]) == 0:
                break
        return results

if __name__ == "__main__":
    for i, n in enumerate(PalindromeNumbers.find_palindromes(1000)):
        print("{0}, {1}: {2}".format(i + 1, n, PalindromeNumbers.convert_num_to_base(i+1, n)))


import unittest

class TestPalindrome(unittest.TestCase):
 
    def test_convert_num_to_base(self):
        f = PalindromeNumbers.convert_num_to_base

        # i, b = r
        # Test negative base
        self.assertRaises(Exception, f, (2, -1))

        # Test negative number
        self.assertRaises(Exception, f, (-1, 2))

        # Test 0 base
        self.assertRaises(Exception, f, (2, 0))

        # Test float
        self.assertRaises(Exception, f, (2.2, 0))

        # Test string
        self.assertRaises(Exception, f, ("2", 0))

        # Test general accuracy
        self.assertEqual(f(2, 2), [1, 0])
        self.assertEqual(f(2, 3), [2])
        self.assertEqual(f(24, 2), [1, 1, 0, 0, 0])
        self.assertEqual(f(1036, 13), [6, 1, 9])
        self.assertEqual(f(18974, 755), [25, 99])
 
    def test_is_palindrome(self):
        f = PalindromeNumbers.is_palindrome

        # Test empty string
        self.assertEqual(f(""), True)

        # Test duplicates
        self.assertEqual(f("001"), False)
        self.assertEqual(f("AABBCCC"), False)
        self.assertEqual(f("ZZZZZZZZZ"), True)
        self.assertEqual(f("ZZZZZZZZ"), True)

        # Test case
        self.assertEqual(f("AABBaa"), False)
        self.assertEqual(f("AABBAA"), True)

    def test_find_palindromes(self):
        f = PalindromeNumbers.find_palindromes

        # Test subset
        self.assertEqual(f(10), [2, 3, 2, 3, 2, 5, 2, 3, 2, 3])
 
if __name__ == '__main__':
    unittest.main()
