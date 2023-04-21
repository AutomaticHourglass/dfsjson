from __future__ import annotations

import unittest

from dfsjson.src.dfsjson import DFSJson

dj = DFSJson()


class TestJSON(unittest.TestCase):
    def test_01(self):
        t = """{
        "key1": "value1'
        "key2": [1 2, 3]
        "key3":  {
            "subkey1": "subvalue1"
            "subkey2": "subvalue2"
        ,
        }"""
        correct = {
            'key1': 'value1', 'key2': [1, 2, 3], 'key3': {
                'subkey1': 'subvalue1', 'subkey2': 'subvalue2',
            },
        }

        self.assertEqual(dj.loads(t), correct)


if __name__ == '__main__':
    unittest.main()
