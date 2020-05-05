""" Test for class feeling.py """

import unittest
import testpath
import feelings


class TestMethods(unittest.TestCase):
    """This class tests the feelings of someone."""

    def test_add(self):
        """See that we are happy"""
        self.assertEqual(feelings.smile(), ":)")
        self.assertEqual(feelings.frown(), ":(")


if __name__ == '__main__':
    unittest.main()
    assert testpath
