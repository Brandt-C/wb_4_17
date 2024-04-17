import unittest

from yester import *

class MatchTestCase2(unittest.TestCase):
    def test_caps_diffrence(self):
        self.assertEqual(spot_diff( "racecar","RaceCar" ),[0, 4] )
    def test_two_diff_word(self):
         self.assertEqual(spot_diff("Cat","Dog"), [0, 1, 2])
    def test_same(self):
        self.assertEqual(spot_diff("same","same"),[])
    def broken_test(self):# wont work because we have to start our test definition with test in order for unittest to find it
        self.assertEqual(spot_diff("broke","break"), [2, 3, 4])

if __name__ == '__main__':
    unittest.main()