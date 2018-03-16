import unittest

from graphene.test import Client

import schema


class TestQueries(unittest.TestCase):

    def test_info(self):
        client = Client(schema.schema)
        executed = client.execute('''{ info { id name description } }''')
        print(executed)
        assert executed == {
            'data': {
                'info': {
                    'id': "ab739864-c0ff-40aa-bcdf-972c0bc794dd",
                    'name': 'Maana NLTK service',
                    'description': 'This is a service for using NLTK with MaanaQ'
                }
            }
        }


if __name__ == '__main__':
    unittest.main()
