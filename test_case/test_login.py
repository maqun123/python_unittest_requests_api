# coding:utf-8
import requests
import unittest
import  json

class get_request(unittest.TestCase):
    def setUp(self):
        self.get_url = 'https://test-m.bmqb.com/api/about/v2/event.json'

    def test_post_01(self):
        url=self.get_url
        r = requests.get(url)
        print(json.dumps(r.json(), indent=4))
        assert r.status_code == 200

    def tearDown(self):
        pass
if __name__ == "__main__":
    unittest.main()