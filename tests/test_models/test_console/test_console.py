#!/usr/bin/python3
"""Console Testing"""

import unittest

from console import HBNBCommand


class test_console(unittest.TestCase):
    """Testcase subclass"""

    def test_create(self):
        """Testing ceate"""
        self.assertTrue(hasattr(HBNBCommand, 'do_create'))
