from __future__ import annotations

import unittest

from dfsjson.src.dfsjson import DFSJson

dj = DFSJson(max_diff=10)


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

    def test_02(self):
        t = """
        {
            "name": "John",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "New York",
                "state": "NY"
            },
            "hobbies": [
                "reading",
                "playing video games",
                "cooking"
            ]
            "isMarried": true,
        }"""

        correct = \
            {
                'name': 'John',
                'age': 30,
                'address': {
                    'street': '123 Main St',
                    'city': 'New York',
                    'state': 'NY',
                },
                'hobbies': [
                    'reading',
                    'playing video games',
                    'cooking',
                ],
                'isMarried': True,
            }

        self.assertEqual(dj.loads(t), correct)

    def test_03(self):
        t = """
        {
            "name": "Sarah",
            "age": 25,
            "address": {
                "street": "456 Pine St",
                "city": "Los Angeles",
                "state": "CA"
            },
            "hobbies": [
                "reading",
                "playing guitar",
                "watching movies"
            ]
            "isMarried": false
            "pets": {
                "dog": "Rover",
                "cat": "Fluffy"
            }
        }"""

        correct = \
            {
                'name': 'Sarah',
                'age': 25,
                'address': {
                    'street': '456 Pine St',
                    'city': 'Los Angeles',
                    'state': 'CA',
                },
                'hobbies': [
                    'reading',
                    'playing guitar',
                    'watching movies',
                ],
                'isMarried': False,
                'pets': {
                    'dog': 'Rover',
                    'cat': 'Fluffy',
                },
            }

        self.assertEqual(dj.loads(t), correct)

    def test_04(self):
        t = """
        {
            "name": "Alice",
            "age": 28,
            "address": {
                "street": "789 Elm St",
                "city": "Seattle",
                "state": "WA",
            },
            "hobbies": [
                "hiking"
                "yoga",
                "reading"
            ],
            "isMarried": true
            "spouse": {
                "name": "Bob",
                "age": 32,
                "occupation": "engineer"
        }"""

        correct = \
            {
                'name': 'Alice',
                'age': 28,
                'address': {
                    'street': '789 Elm St',
                    'city': 'Seattle',
                    'state': 'WA',
                },
                'hobbies': [
                    'hiking',
                    'yoga',
                    'reading',
                ],
                'isMarried': True,
                'spouse': {
                    'name': 'Bob',
                    'age': 32,
                    'occupation': 'engineer',
                },
            }

        self.assertEqual(dj.loads(t), correct)

    def test_05(self):
        t = """
        {
            "title": "The Hitchhikers Guide to the Galaxy,
            "author": "Douglas Adams"
            "year": 1979,
            "genre": ["science-fiction", "comedy"]
            "characters": {
                "Arthur Dent": "human",
                "Ford Prefect": "alien",
                "Zaphod Beeblebrox": "two-headed alien"
            }
            "isAudiobook": true
            "audioBookDuration": "5 hours 45 minutes"
            "publishingInfo": {
                "publisher": "Pan Books",
                "publicationDate": "12 Oct 1979"
        }"""

        correct = \
            {
                'title': 'The Hitchhikers Guide to the Galaxy',
                'author': 'Douglas Adams',
                'year': 1979,
                'genre': ['science-fiction', 'comedy'],
                'characters': {
                    'Arthur Dent': 'human',
                    'Ford Prefect': 'alien',
                    'Zaphod Beeblebrox': 'two-headed alien',
                },
                'isAudiobook': True,
                'audioBookDuration': '5 hours 45 minutes',
                'publishingInfo': {
                    'publisher': 'Pan Books',
                    'publicationDate': '12 Oct 1979',
                },
            }

        self.assertEqual(dj.loads(t), correct)


if __name__ == '__main__':
    unittest.main()
