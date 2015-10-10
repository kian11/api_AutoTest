__author__ = 'huiyi_000'
# -*- coding: utf-8 -*-

import unittest
import requests
import HTMLTestRunner
import os,time,smtplib
from email.mime.text import MIMEText
import All_testCase.goodsCategory,All_testCase.goodsDetail
import All_testCase.goodsCategory,All_testCase.goodsCategory
import All_testCase.goodsCategory,All_testCase.goodsList
import All_testCase.goodsCategory,All_testCase.shopCompany
import All_testCase.goodsCategory,All_testCase.shopGoods
import All_testCase.goodsCategory,All_testCase.userCheckLogin
import All_testCase.goodsCategory,All_testCase.userLogin
import All_testCase.goodsCategory,All_testCase.userVerificationCode


#发送邮箱
sender = 'barryli@lianshang.cn'
#接收邮箱
receiver = 'barryli89@163.com'
#发送邮件主题
subject =u'【买家版】接口测试结果'
#发送邮箱服务器
smtpserver = 'smtp.lianshang.cn'
#发送邮箱用户/密码
username = 'barry.li@lianshang.cn'
password = 'lch67313559'
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

def sentmail(file_new):
    print 'sentmail'
    #发信邮箱
    mail_from=sender
    #收信邮箱
    mail_to=receiver
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题
    msg['Subject']=subject
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    #连接 SMTP 服务器
    smtp.connect(smtpserver)
    #用户名密码
    smtp.login(username,password)
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print 'email has send out !'
    #查找测试报告，调用发邮件功能
def sendreport():
    print 'sendreport'
    result_dir = "F:\\ApiTestResult"
    print result_dir
    lists=os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
    os.path.isdir(result_dir+"\\"+fn) else 0)
    print (u'最新测试生成的报告： '+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1])
    print file_new
    #调用发邮件模块
    sentmail(file_new)

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.targetApi = All_testCase.Public.domain() + '/goods/category'

    def test_something(self):
        filename="F:\ApiTestResult\\"+now+'report.html'
        print filename
        testunit=unittest.TestSuite()
        testunit.addTest(unittest.makeSuite(All_testCase.goodsCategory.GoodsCategory))
        testunit.addTest(unittest.makeSuite(All_testCase.goodsDetail.goodsDetail))
        testunit.addTest(unittest.makeSuite(All_testCase.goodsList.goodsList))
        testunit.addTest(unittest.makeSuite(All_testCase.shopGoods.shopGoods))
        testunit.addTest(unittest.makeSuite(All_testCase.shopCompany.shopCompany))
        testunit.addTest(unittest.makeSuite(All_testCase.userVerificationCode.userVerificationCode))
        testunit.addTest(unittest.makeSuite(All_testCase.userCheckLogin.userCheckLogin))
        testunit.addTest(unittest.makeSuite(All_testCase.userLogin.userLogin))

        fp=file(filename,'wb')
        runner=HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'移动端买家版接口测试结果',
            description=u'用例执行情况:'
        )
        runner.run(testunit)
    def tearDown(self):
        sendreport()


if __name__ == '__main__':
    unittest.main()
