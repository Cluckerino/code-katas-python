"""Example unit test module"""

import unittest
import solutions.hello_world


class HelloWorldTest(unittest.TestCase):
    """Example test suite"""

    def test_hello_world(self):
        """Example unit test"""
        self.assertEqual("Hello World!", solutions.hello_world.hello_world())
