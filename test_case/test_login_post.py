# coding:utf-8
import requests
import json
import unittest


class post_request(unittest.TestCase):
    """登录获取登录状态"""
    def setUp(self):
        self.post_url = 'https://test.bmqb.com/account/login'  # 根据实际接口，自己填写
        self.header = {'content-type': 'application/json','X-Token': 'mobile', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
  # 根据实际内容，自己填写
        self.session = requests.Session()  # 自动处理cookie
        self.date= {'mobile': '18217152656', 'password': '111111'}

    def test_post_01(self):
        """登录"""
        url = self.post_url
        header = self.header
        data = self.date# 根据实际内容，自己填写
        # 将data序列化为json格式数据，传递给data参数
        r = requests.post(url, data=json.dumps(data), headers=header)

        print(json.dumps(r.text))

    def test_post_02(self):
        """资产查询"""
        url = self.post_url
        header = self.header
        data = self.date  # 根据实际内容，自己填写

        r = self.session.post(url, data=json.dumps(data), headers=header)

        result = r.json()

        session_response = self.session.get('https://test.bmqb.com/account/my_assets')
        my_assets = session_response.json()

      #  print(json.dumps(session_response.json()))

        print  (json.dumps(my_assets, indent=4))

        assert session_response.status_code==200
        assert my_assets['assets']['total']>100
        assert my_assets['bonus']['invest_amount']>100

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()