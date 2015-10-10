__author__ = 'huiyi_000'
# -*- coding: utf-8 -*-

import unittest
import  time

import requests

import Public


class userPublishRequest(unittest.TestCase):
    def setUp(self):
        self.targetApi= Public.domain()+'/user/publish'
        self.token=Public.getDuetoken('huiyiditou','123123')
        self.uid=Public.getUserid(self.token)
        self.color='39,40,41,42,43,35,37,38,9,10,11,12,13,14,15,16,21,33,34,36,31,32,22,23,24,25,26,27,28,29,30,17,18,19,20,8'#面辅料都有
        self.style='1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22'#风格，面辅料都有
        self.season_Fab='1,2,3,4'#季节面料才有
        self.uses_Fab='1,2,3,4,5,6,7,8,9,10'#用途，面料才有
        self.craftwork_Fab='1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29'#面料工艺
        self.craftwork_Acc='30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61'#辅料工艺


        self.material_Acc='1,2,3,4,5,6,7,8,9,10,11,12,13,14,15'#材质，辅料才有


    def test_publishFabric(self):
        print u'开始测试发布面料接口'
        par={
            'uid':self.uid,
            'token':self.token,
            'goods_type':'1',
            'brand':'自动化测试专用品牌',
            'description':'自动化测试—发布面料需求',
            'num':'199',
            'unit':'米',
            'charactor':'1',
            'color':self.color,
            'category':'22',#棉纺面料、仿天丝
            'season':self.season_Fab,
            'pattern':'16',#单选项，但是数据库里还是多选项
            'style':self.style,#风格
            'craftwork':self.craftwork_Fab,#工艺
            'width':'256',
            'width_unit':'码',
            'weight':'379',
            'weight_unit':'英寸',
            'uses':self.uses_Fab,
            'origin':'16'#柯桥
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
        print u'______________发布面料需求测试完毕_________________'

    def test_publishAccessories(self):
        print u'开始测试发布辅料接口'
        par={
            'uid':self.uid,
            'token':self.token,
            'goods_type':'2',
            'brand':'自动化测试专用品牌',
            'description':'自动化测试—发布辅料需求',
            'num':'199',
            'unit':'米',
            'charactor':'0',#1现货、0定制
            'material':self.material_Acc,#村质
            'color':self.color,
            'category':'22',#棉纺面料、仿天丝
            'pattern':'16',#单选项，但是数据库里还是多选项
            'style':self.style,#风格
            'craftwork':self.craftwork_Acc,#工艺
            'width':'256',
            'width_unit':'码',
            'weight':'379',
            'weight_unit':'英寸',
            'origin':'16'#柯桥
        }
        r=requests.post(self.targetApi,data=par)
        r_info=r.json()['code']
        # self.id_Acc=r.json()['data']['id']
        # print self.id_Acc
        if(r_info==0 and r.status_code==200):
            print u"result：pass"
            print u'接口返回消息：'+ r.json()['msg']
        else:
            print(u'result：false')
            print u'接口返回code:',r_info,u'状态码：',r.status_code
            print u'接口返回消息：'+ r.json()['msg']
        self.assertEqual(r_info,0)
        print u'______________发布辅料需求测试完毕_________________'

    # def test_modifyFabric(self):
    #     print u'开始测试修改面料需求接口'
    #     print self.id_Fab
    #     par={
    #         'id':self.id_Fab,
    #         'uid':self.uid,
    #         'token':self.token,
    #         'goods_type':'1',
    #         'brand':'自动化测试专用品牌',
    #         'description':'自动化测试—发布面料需求',
    #         'num':'199',
    #         'unit':'米',
    #         'charactor':'1',
    #         'color':'40',
    #         'category':'22',#棉纺面料、仿天丝
    #         'season':'1',
    #         'pattern':'15',#单选项，但是数据库里还是多选项
    #         'style':'2',#风格
    #         'craftwork':'6',#工艺
    #         'width':'999',
    #         'width_unit':'码',
    #         'weight':'1999',
    #         'weight_unit':'英寸',
    #         'uses':'5',
    #         'origin':'1'#广州
    #     }
    #     r=requests.post(self.targetApi,data=par)
    #     r_info=r.json()['code']
    #     if(r_info==0 and r.status_code==200):
    #         print u"result：pass"
    #         print u'接口返回消息：'+ r.json()['msg']
    #     else:
    #         print(u'result：false')
    #         print u'接口返回code:',r_info,u'状态码：',r.status_code
    #         print u'接口返回消息：'+ r.json()['msg']
    #     self.assertEqual(r_info,0)
    #     print u'______________修改面料需求测试完毕_________________'




    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
