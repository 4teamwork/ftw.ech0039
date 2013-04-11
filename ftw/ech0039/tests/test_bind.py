from unittest2.case import TestCase
from pyxb import BIND as PYXB_BIND
from ftw.ech0039.bind import BIND


class TestBind(TestCase):

    bind_1 = BIND(
            BIND(
                uuid=u'b78f19a669a24597af1c3b2120e19eb7',
                status=u'closed',
                titles=BIND(
                    BIND(u'Folder', lang='de'),
                ),
            ),
        )

    bind_2 = BIND(
            BIND(
                uuid=u'gak',
                status=u'closed',
                titles=BIND(
                    BIND(u'Folder', lang='de'),
                ),
            ),
        )

    def test_attributes(self):
        """Document that we use 'private' attributes and fails as soon as the
        implementation has changed.
        """

        b = PYXB_BIND()
        self.assertTrue(hasattr(b, '_BIND__kw'))
        self.assertTrue(hasattr(b, '_BIND__args'))

    def test_comparison(self):
        """Test that equality comparison works.
        """

        self.assertEqual(self.bind_1, self.bind_1)
        self.assertEqual(self.bind_2, self.bind_2)
        self.assertNotEqual(self.bind_1, self.bind_2)
        self.assertNotEqual(self.bind_2, self.bind_1)
