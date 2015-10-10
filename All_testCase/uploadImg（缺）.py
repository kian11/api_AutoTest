__author__ = 'huiyi_000'
# -*- coding: utf-8 -*-

import unittest

import Public


class uploadImg(unittest.TestCase):
    def setUp(self):
        self.targetApi = Public.domain() + '/upload/img'

    def test_something(self):
        self.assertEqual(True, False)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
