# !/usr/bin/env python
# -*- coding:utf-8 -*-
import unittest
from nameFunction import name_function


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确处理像Janis Joplin这样的姓名吗？"""
        formatted_name = name_function('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
        # self.assertEqual(formatted_name, 'Janis  Joplin')


if __name__ == '__main__':
    unittest