__author__ = 'huiyi_000'
# -*- coding: utf-8 -*-

import unittest
import time

import requests

import Public


class userCheckLogin(unittest.TestCase):
    def setUp(self):
        self.targetApi= Public.domain()+'/user/check'
        self.token= Public.getUserToken(username='huiyiditou',pwd='123123')
        #code：返回码，0登录成功，1登录失败，2参数错误，3账户或密码有误；
    def test_register(self):
        print u'开始测试登录后的token检查'
        print u'测试项1：正确未过期的token校验'
        par={'token':self.token}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==0 and r.status_code==200):
            print u"Result：Pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'Result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,0)
        print u'______________测试项1测试完毕_________________'
        print u'测试项2：过期的token校验'
        time.sleep(1)
        errorToken='90f0b04a5eaa075770fa13461'
        newtoken= Public.getUserToken('huiyiditou','123123')
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==-1 and r.status_code==200):
            print u"Result：Pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'Result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,-1)
        print u'______________测试项1测试完毕_________________'


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
