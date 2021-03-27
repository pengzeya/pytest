# - * - coding : utf-8 - * -
# @Time ： 2021/3/27 2:12 
# @author ： pengzeya
# @Email ： 281232686@qq.com
import requests

def test_get_token():
    corpid = 'ww27614a4a8c44ef65'
    corpsecret = 'aCjdJ9EPCVgyENmcw3zi_YQKRBvLPkpfQeCxoPsIRDE'
    r = requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}')
    print(r.json()['access_token'])
    return r.json()['access_token']
def test_get_name():
    userid= 'pengzeya'
    token = ''
    r= requests.get(f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_get_token()}&userid={userid}')
    print(r.json())

def test_create():
    data = {
        "userid": "pengzeya",
        "name": "张三",
        "alias": "jackzhang",
        "mobile": "+86 13800000000",
         "department": [1]
    }

    res =requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_get_token()}',
                  json = data)
    print(res.json())

def test_updata():
    data = {
        "userid": "pengzeya",
        "name": "张三",
        "alias": "jackzhang",
        "mobile": "+86 13800000000",
        "department": [1]
    }
    res = requests.post(f'https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_get_token()}',
                        json = data)
    print(res.json())