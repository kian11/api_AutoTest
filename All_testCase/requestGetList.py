__author__ = 'huiyi_000'
# -*- coding: utf-8 -*-

import unittest
import  time

import requests

import Public


class userPublishRequest(unittest.TestCase):
    def setUp(self):
        self.targetApi= Public.domain()+'/user/demand-list'
        self.token=Public.getDuetoken('huiyiditou','123123')
        self.uid=Public.getUserid(self.token)


    def test_getNotFound(self):
        print u'开始测试获取未找到需求接口'
        par={
            'uid':self.uid,
            'token':self.token,
            'status':'0',
        }
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        # self.id_Fab=r.json()['data']['id']
        # print self.id_Fab
        if(r_info==0 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,0)
        print u'______________获取未找到需求列表测试完毕_________________'

    def test_getFound(self):
        print u'开始测试获取已找到需求接口'
        par={
            'uid':self.uid,
            'token':self.token,
            'status':'1',
        }
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        # self.id_Fab=r.json()['data']['id']
        # print self.id_Fab
        if(r_info==0 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,0)
        print u'______________获取已找到需求列表测试完毕_________________'

    def test_getAll(self):
        print u'开始测试获取全部需求接口'
        par={
            'uid':self.uid,
            'token':self.token,
            'status':'2',
        }
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        # self.id_Fab=r.json()['data']['id']
        # print self.id_Fab
        if(r_info==0 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,0)
        print u'______________获取已找到需求列表测试完毕_________________'



    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
