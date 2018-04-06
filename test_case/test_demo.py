#!/usr/bin/python
# coding=utf-8
import unittest
import json
from pprint import pprint
from requests.sessions import Session
try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


class DemoApi(object):

    def __init__(self, base_url):
        self.base_url = base_url
        # 创建session实例
        self.session = Session()

    def login(self, mobile, password):
        """
        登录接口
        :param username: 用户名
        :param password: 密码
        """
        url = urljoin(self.base_url, 'account/login')
        data = {
            'mobile': mobile,
            'password': password
        }
        headers = {'content-type': 'application/json', 'X-Token': 'mobile',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}


        response = self.session.post(url ,data=json.dumps(data), headers=headers).json()
        print('\n*****************************************')
        print(u'\n1、请求url: \n%s' % url)
        print(u'\n2、请求头信息:')
        pprint(self.session.headers)
        print(u'\n3、请求参数:')
        pprint(data)
        print(u'\n4、响应:')
        pprint(response)
        return response

    def info(self):
        """
        详情接口
        """
        url = urljoin(self.base_url, 'account/my_assets')
        response = self.session.get(url).json()

        print('\n*****************************************')
        print(u'\n1、请求url: \n%s' % url)
        print(u'\n2、请求头信息:')
        pprint(self.session.headers)
        print(u'\n3、请求cookies:')
        pprint(dict(self.session.cookies))
        print(u'\n4、响应:')
        pprint(response)
        return response


class TestLogin(unittest.TestCase):
    """
    测试登录
    """
    @classmethod
    def setUpClass(self):
        self.base_url = 'https://test.bmqb.com/account'
        self.mobile = '18217152656'
        self.password = '111111'
        self.app = DemoApi(self.base_url)

    def test_login(self):
        """
        测试登录
        """
        response = self.app.login(self.mobile, self.password)
        assert response['account_id'] == 3

    def test_info(self):
        """
        测试获取详情信息
        """
        self.app.login(self.mobile, self.password)
        response = self.app.info()
        assert response['accumulative_interest'] >0
        assert response['yesterday_interest'] >0
if __name__ == "__main__":
    unittest.main()
