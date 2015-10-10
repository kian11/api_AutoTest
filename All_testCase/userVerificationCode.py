__author__ = 'huiyi_000'
# -*- coding: utf-8 -*-

import unittest
import  time

import requests

import Public


class userVerificationCode(unittest.TestCase):
    def setUp(self):
        self.targetApi= Public.domain()+'/user/yzm'
        self.new_tel='13777777777'#用于返回code0发送成功及code6该手机未注册（修改与找回用）
        self.exist_tel='18817763313'#用于返回code5手机号已存在
        self.invalid_tel='1371234564'#用于返回code3手机号无效
        #code：返回码，
        # 0发送验证码成功，
        # 1发送失败，
        # 2参数错误，
        # 3手机号无效，
        # 4一分钟内不能重复发短信，
        # 5该手机号已注册，
        # 6该手机号还未注册，
        # 7添加验证码失败；
    def test_register(self):
        print u'开始测试注册验证码接口'
        time.sleep(60)
        print u'测试项1：新手机号注册时成功返回验证码'
        par={'mobile':self.new_tel,'type':'register'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==0 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,0)
        print u'______________测试项1测试完毕_________________'
        print u'测试项2：新手机号注册时60秒内重复发送报错'
        par={'mobile':self.new_tel,'type':'register'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==4 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,4)
        print u'______________测试项2测试完毕_________________'
        print u'测试项3：新手机号注册时手机号已被使用'
        par={'mobile':self.exist_tel,'type':'register'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==5 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,5)
        print u'______________测试项3测试完毕_________________'
        print u'测试项4：新手机号注册时手机号无效'
        par={'mobile':self.invalid_tel,'type':'register'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==3 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,3)
        print u'______________测试项4测试完毕_________________'


    def test_find(self):
        print u'开始测试找回验证码接口'
        time.sleep(60)
        print u'测试项1：找回密码时成功返回验证码'
        par={'mobile':self.exist_tel,'type':'find'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==0 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,0)
        print u'______________测试项1测试完毕_________________'
        print u'测试项2：找回密码时60秒内重复发送报错'
        par={'mobile':self.exist_tel,'type':'find'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==4 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,4)
        print u'______________测试项2测试完毕_________________'
        print u'测试项3：找回密码时手机号未被注册'
        par={'mobile':self.new_tel,'type':'find'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==6 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,6)
        print u'______________测试项3测试完毕_________________'
        print u'测试项4：找回密码时手机号无效'
        par={'mobile':self.invalid_tel,'type':'find'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==3 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,3)
        print u'______________测试项4测试完毕_________________'


    def test_change(self):
        print u'开始测试修改密码接口'
        time.sleep(60)
        print u'测试项1：修改密码时成功返回验证码'
        par={'mobile':self.exist_tel,'type':'find'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==0 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,0)
        print u'______________测试项1测试完毕_________________'
        print u'测试项2：修改密码时60秒内重复发送报错'
        par={'mobile':self.exist_tel,'type':'find'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==4 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,4)
        print u'______________测试项2测试完毕_________________'
        print u'测试项3：修改密码时手机号未被注册'
        par={'mobile':self.new_tel,'type':'find'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==6 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,6)
        print u'______________测试项3测试完毕_________________'
        print u'测试项4：修改密码时手机号无效'
        par={'mobile':self.invalid_tel,'type':'find'}
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        if(r_info==3 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,3)
        print u'______________测试项4测试完毕_________________'


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
