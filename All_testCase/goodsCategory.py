__author__ = 'huiyi_000'
# -*- coding: utf-8 -*-

import unittest
import sys
import urllib

import requests

import Public


class GoodsCategory(unittest.TestCase):
    def setUp(self):
        self.type = sys.getfilesystemencoding()
        self.postdata=urllib.urlencode({})
        self.targetApi= Public.domain()+'/goods/category'
    def test_something(self):
        r=requests.post(self.targetApi)
        r_info=r.json()['code']
        if(r_info==0 and r.status_code==200):
            print u"商品分类接口调用成功"
        else:
            print(u'商品分类接口调用失败')
            print r_info,r.status_code
        self.assertEqual(r.status_code,200)
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
