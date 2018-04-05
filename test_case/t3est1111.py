import unittest
import requests
import json

login_data = {'mobile': '18217152656', 'password': '111111'}
headers = {'content-type': 'application/json','X-Token': 'mobile', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

class MyTestCase(unittest.TestCase):
    '''登录查询资产'''
    def test_my_assets(self):
        # 举例：登录名　密码　 key为登陆表单中对应的input的name值
        login_data = {'mobile': '18217152656', 'password': '111111'}
        headers = {'content-type': 'application/json', 'X-Token': 'mobile',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        session = requests.Session()  # 自动处理cookie
        r = session.post("https://test.bmqb.com/account/login", headers=headers, data=json.dumps(login_data))
        # 获取发送的session
        result = r.json()
        session_response = session.get('https://test.bmqb.com/account/my_assets')
        print(session_response.text)
        print('session请求返回的状态码为：' + str(session_response.status_code))
        my_assets = session_response.json()
        print(result)
        print(result['token'], result['is_admin'])
        print(my_assets['assets']['total'], my_assets['bonus']['invest_amount'])




        assert session_response.status_code==200
        assert my_assets['assets']['total']>100
        assert my_assets['bonus']['invest_amount']>100


if __name__ == '__main__':
    MyTestCase()


