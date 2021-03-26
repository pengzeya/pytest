# - * - coding : utf-8 - * -
# @Time ： 2021/3/27 0:27 
# @author ： pengzeya
# @Email ： 281232686@qq.com
import requests
from jsonpath import jsonpath
class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.text)
        print(r.json())
        print(r.status_code)
        assert r.status_code ==200


    def test_query(self):
        payload={
            "level": 1,
            "name":"seveniruby"
        }
        r = requests.get('http://httpbin.testing-studio.com/get',params = payload)
        print(r)
        assert r.status_code == 200

    def test_past_form(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', data = payload)
        print(r.text)
        assert r.status_code == 200

    def test_header(self):
        r = requests.get('http://httpbin.testing-studio.com/get',headers ={"h":"header demo"})
        print(r.text)
        print(r.json())
        print(r.status_code)
        assert r.status_code == 200
        print(r.json()['headers']['H'])
        assert r.json()['headers']["H"] =="header demo"

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json = payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level']==1


    def test_xuexi(self):
        r = requests.post('http://ceshiren.com/categories.json')
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '开源项目'
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(),'$..name')[0] == '开源项目'

