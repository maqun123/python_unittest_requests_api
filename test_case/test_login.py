# coding:utf-8
import requests
import unittest

class get_request(unittest.TestCase):
    def setUp(self):
        self.get_url = 'https://www.bmqb.com/'
    def test_post_01(self):
        url=self.get_url
        r = requests.get(url)
        print (r.text)
    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()