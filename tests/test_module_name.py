#! python3.8
# -*- coding: utf-8 -*-

# File name:    test_module_name.py
# Author:       Tobias Rosskopf
# Email:        tobirosskopf@gmail.com
# Created:      ??.??.2019
# Modified:     ??.??.2019

"""
Unittest for module <module_name.py>.
"""

# Standard imports
import unittest

# Package imports
import package_name.module_name


class TestClassName(unittest.TestCase):
    """Testclass's docstring"""

    def test_main(self):
        """Test's docstring"""
        self.assertEqual(package_name.module_name.main("Test"), "Test")


if __name__ == '__main__':
    unittest.main()
