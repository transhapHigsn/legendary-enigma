import unittest
import requests
import json

class LocatorTestCase(unittest.TestCase):

    maxDiff = None

    headers = {
            'Content-Type':'application/json',
            'Accept': 'application/json',
        }
    
    data = json.dumps({
            'latitude':28.6333,
            'longitude': 77.2167,
        })            

    def setup(self):
        pass

    def tearDown(self):
        pass
    
    def testGetGeoLocation(self):
        res = requests.get("http://127.0.0.1:5000/geo_location", data=self.data, headers=self.headers)
        val = res.json()
        self.assertEqual(val['location'],'Gurgaon')   


if __name__ =='__main__':
    unittest.main()       