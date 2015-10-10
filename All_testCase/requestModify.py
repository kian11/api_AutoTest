__author__ = 'huiyi_000'
# -*- coding: utf-8 -*-

import unittest

import requests

import Public


class goodsList(unittest.TestCase):
    def setUp(self):
        self.targetApi= Public.domain()+'/user/publish'
        self.rid=Public.getRequestID('0')
        print self.rid

    def test_classify(self):
        print u'开始测试首页的分类导航功能'
        print self.rid
        # par={'category_parent':'6','category_son':'16','order':'0'}
        # r=requests.post(self.targetApi,data=par)
        # r_info=r.json()['code']
        # if(r_info==0 and r.status_code==200):
        #     print u"商品列表页接口调用成功"
        #     print u'接口返回消息：'+ r.json()['msg']
        # else:
        #     print(u'商品列表页接口调用失败')
        #     print r_info,r.status_code
        # self.assertEqual(r.status_code,200)

    # def test_search(self):
    #     print u'开始测试首页的搜索接口'
    #     for i in range(1,4):
    #         par={'keyword':'多色','goods_type':i,'order':'0'}
    #         # goods_type:商品类别1、面料，2、辅料,3、店铺
    #         #order：排序，0最新，1人气，2销量，3样布价由低到高，4样布价由高到低，5大货价由低到高，6大货价由高到低；
    #         r=requests.post(self.targetApi,data=par)
    #         r_info=r.json()['code']
    #         if(r_info==0 and r.status_code==200):
    #             print u"搜索成功"
    #             print u'接口返回消息：'+ r.json()['msg']
    #         else:
    #             print(u'商品列表页接口调用失败')
    #             print r_info,r.status_code
    #         self.assertEqual(r.status_code,200)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
