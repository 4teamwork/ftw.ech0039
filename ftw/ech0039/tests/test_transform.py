from DateTime import DateTime
from datetime import date
from datetime import datetime
from ftw.ech0039 import transform
from pyxb.binding import datatypes as xs
import unittest2


class TestAsToken(unittest2.TestCase):
    """Test transform helpers.
    """

    def test_as_token(self):
        """Test that a valid token is generated.
        """

        self.assertEqual(u'gak', transform.as_token(u' gak'))
        self.assertEqual(u'gak', transform.as_token(u'gak  '))
        self.assertEqual(u'gak', transform.as_token(u'  gak'))
        self.assertEqual(u'ga k', transform.as_token(u'ga  k'))
        self.assertEqual(u'ga k', transform.as_token(u'ga k'))
        self.assertEqual(u'ga k', transform.as_token(u'  ga  k  '))

        self.assertEqual(u'ga k', transform.as_token(u'ga\tk'))
        self.assertEqual(u'ga k', transform.as_token(u'ga\nk'))
        self.assertEqual(u'ga k', transform.as_token(u'ga\rk'))
        self.assertEqual(u'ga k', transform.as_token(u'ga\r\rk'))

    def test_as_normalized_string(self):
        """Test that a valid normalized string is generated.
        """

        self.assertEqual(u' ga  k ',
                         transform.as_normalized_string(u' ga  k '))

        self.assertEqual(u'ga k', transform.as_normalized_string(u'ga\tk'))
        self.assertEqual(u'ga k', transform.as_normalized_string(u'ga\nk'))
        self.assertEqual(u'ga k', transform.as_normalized_string(u'ga\rk'))
        self.assertEqual(u'ga  k', transform.as_normalized_string(u'ga\t\tk'))

    def test_as_date(self):
        """Test that different dates can be converted.
        """

        self.assertEqual(xs.date(2010, 1, 1),
                         transform.as_date(date(2010, 1, 1)))
        self.assertEqual(xs.date(2010, 1, 1),
                         transform.as_date(datetime(2010, 1, 1, 20, 10, 1)))
        self.assertEqual(xs.date(2010, 1, 1),
                         transform.as_date(DateTime(2010, 1, 1)))
        self.assertEqual(xs.date(2010, 1, 1),
                         transform.as_date(DateTime(2010, 1, 1, 15, 2, 7)))
