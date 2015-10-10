__author__ = 'huiyi_000'
# -*- coding: utf-8 -*-
import requests
import json

def domain():
    domain='http://192.168.1.252'
    # domain='http://app.lianshang.cn'
    return  domain

def getRequestID(status):
    targetApi= domain()+'/user/demand-list'
    token=getUserToken('huiyiditou','123123')
    par={
         'uid':getUserid(token),
         'token':token,
         'status':status,
    }
    r=requests.post(targetApi,par)
    rid=r.json()['data']['id']
    # json_data=json.load(rid)
    return rid
def getUserToken(username,pwd):
    targetApi=domain()+'/user/login'
    par={'username':username,'pwd':pwd}
    r=requests.post(targetApi,par)
    token=r.json()['data']['token']
    return token

def getUserid(token):
    targetApi=domain()+'/user/check'
    par={'token':token}
    r=requests.post(targetApi,par)
    uid=r.json()['data']['uid']
    return uid

def getDuetoken(username,pwd):

    targetApi=domain()+'/user/login'
    par={'username':username,'pwd':pwd}
    r=requests.post(targetApi,par)
    token=r.json()['data']['token']
    return token

if __name__ == '__main__':
    pass



