__author__ = 'huiyi_000'
# -*- coding: utf-8 -*-

import unittest

import requests

import Public


class goodsDetail(unittest.TestCase):
    def setUp(self):
        self.targetApi= Public.domain()+'/goods/detail'

    def test_detail(self):
        print u'开始测试正确商品详情页接口'
        par={'goods_id':'860056'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==0 and r.status_code==200):
            print u"商品详情接口调用成功"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'商品详情接口调用失败')
            print r_info,r.status_code
        self.assertEqual(r.status_code,200)


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
