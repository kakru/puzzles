#/usr/bin/env python3
import unittest

# TRY AGAIN
# this time without using OrderedDict

from collections import OrderedDict
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.storage = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        try:
            value = self.storage[key] = self.storage.pop(key)
            return value
        except KeyError:
            return -1

        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        try:
            self.storage.pop(key)
        except KeyError:
            if self.capacity <= len(self.storage):
                self.storage.popitem(last=False)
        self.storage[key] = value




class BasicTest(unittest.TestCase):
    def test_1(self):
        obj = LRUCache(2)
        self.assertEqual(obj.get(1), -1)
        obj.put(1, 1)
        obj.put(2, 2)
        self.assertEqual(obj.get(1), 1)
        obj.put(3, 3)
        self.assertEqual(obj.get(2), -1)
        obj.put(4, 4)
        self.assertEqual(obj.get(3), 3)
        self.assertEqual(obj.get(4), 4)

    def test_2(self):
        obj = LRUCache(2)
        self.assertEqual(obj.get(2), -1)
        obj.put(2, 6)
        self.assertEqual(obj.get(1), -1)
        obj.put(1, 5)
        obj.put(1, 2)
        self.assertEqual(obj.get(1), 2)
        self.assertEqual(obj.get(2), 6)

    def test_3(self):
        obj = LRUCache(2)
        obj.put(2, 1)
        obj.put(1, 1)
        obj.put(2, 3)
        obj.put(4, 1)
        self.assertEqual(obj.get(1), -1)
        self.assertEqual(obj.get(2), 3)


if __name__ == '__main__':
    unittest.main(verbosity=2)