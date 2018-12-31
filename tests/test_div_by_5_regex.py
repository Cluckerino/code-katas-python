"""Tests for the fold_an_array kata"""

import re
import unittest

from solutions.div_by_5_regex import PATTERN


class DivBy5RegexTest(unittest.TestCase):

    def setUp(self):
        """Build the regex used for testing."""
        self.matcher = re.compile(PATTERN)

    def run_test(self, binStr, expected):
        """Run the given test"""
        actual = bool(self.matcher.match(binStr))
        self.assertEqual(actual, expected,
                         "Invalid result for {}".format(binStr))

    def test_examples_from_kata(self):
        """Run the tests given from the kata."""
        kataCases = [(False, ""),
                     (False, "abc"),
                     (True,  "000"),
                     (True,  "101"),
                     (True,  "1010"),
                     (True,  "10100"),
                     (True,  "{:b}".format(65020)),
                     (True,  "{:b}".format(6039865)),

                     (False, "10110101"),
                     (False, "1110001"),

                     (False,  "{:b}".format(21)),
                     (False,  "{:b}".format(15392)),
                     (False,  "{:b}".format(23573)),
                     (False,  "{:b}".format(19344)),

                     (False,  "{:b}".format(43936)),
                     (False,  "{:b}".format(32977)),
                     (False,  "{:b}".format(328)),
                     (False,  "{:b}".format(5729)),
                     ]
        for expected, testStr in kataCases:
            with self.subTest(binStr=testStr):
                self.run_test(testStr, expected)
