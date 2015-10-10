__author__ = 'huiyi_000'
# -*- coding: utf-8 -*-

import unittest

import requests

import Public


class shopGoods(unittest.TestCase):
    def setUp(self):
        self.targetApi= Public.domain()+'/shop/goods'

    def test_shopGoods(self):
        print u'开始测试店铺主页商品信息接口'
        par={'shop_id':'631'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==0 and r.status_code==200):
            print u"店铺主页商品信息调用成功"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'店铺主页商品信息调用失败')
            print r_info,r.status_code
        self.assertEqual(r.status_code,200)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
