__author__ = 'huiyi_000'
# -*- coding: utf-8 -*-

import unittest

import requests

import Public


class userLogin(unittest.TestCase):
    def setUp(self):
        self.targetApi= Public.domain()+'/user/login'
        self.validUsername='huiyiditou'
        self.invalidUsername='huiyidd'
        self.validPwd='123123'
        self.invalidPwd='123456777'
        #code：返回码，0登录成功，1登录失败，2参数错误，3账户或密码有误；
    def test_login(self):
        print u'开始测试用户登录接口'
        print u'测试项1：正确的用户名+密码成功登录'
        par={'username':self.validUsername,'pwd':self.validPwd}
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
        print u'测试项2：正确的用户名+错误的密码登录报错'
        par={'username':self.validUsername,'pwd':self.invalidPwd}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==3 and r.status_code==200):
            print u"Result：Pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'Result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,3)
        print u'______________测试项2测试完毕_________________'


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
