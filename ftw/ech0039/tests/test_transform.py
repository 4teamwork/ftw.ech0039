from ftw.ech0039 import transform
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
