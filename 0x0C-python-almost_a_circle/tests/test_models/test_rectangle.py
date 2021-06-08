#!/usr/bin/python3
'''
Test module for the rectangle.py file
'''
import unittest
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    def setUp(self):
        '''
        Create an instance of a Rectangle to be used across the tests
        '''
        self.rec = Rectangle(20, 5)

    def tearDown(self):
        '''
        Deletes the instance used for testing
        '''
        del self.rec

    def test_2_pars(self):
        # Will be 3 because in the base tests we created two instances
        self.assertEqual(self.rec.id, 3)
        self.assertEqual(self.rec.width, 20)
        self.assertEqual(self.rec.height, 5)

    def test_errors(self):
        #When no argument is passed
        with self.assertRaises(TypeError):
            r = Rectangle()

        # When more than five arguments are passed
        with self.assertRaises(TypeError):
            r = Rectangle(2, 3, 4, 5, 5, 6)
