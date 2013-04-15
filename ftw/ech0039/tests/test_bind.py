from ftw.ech0039.bind import BIND
from pyxb import BIND as PYXB_BIND
from unittest2.case import TestCase


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

        self.assertFalse(self.bind_1 == None)
        self.assertFalse(self.bind_1 == 'gak')

    def test_repr(self):
        """Test that repr does not fail but don't test exact representation.
        """

        dossier = BIND(
            dossiers=BIND(
                BIND(
                    uuid='1234-5678',
                    status=u'closed',
                    titles=BIND(
                        BIND(u'Parent Folder', lang='de'),
                    ),
                    documents=BIND(
                        BIND(
                            uuid='2345-6789',
                            titles=BIND(
                                BIND(u'Child File', lang='de'),
                            ),
                            status=u'approved',
                            files=BIND(
                                BIND(
                                    pathFileName='files/foo.txt',
                                    mimeType=u'text/plain',
                                    hashCode='kashdkajsdhklsadhksajd',
                                    hashCodeAlgorithm=u'SHA-256',
                                ),
                            ),
                        ),
                    ),
                    dossiers=BIND(
                        BIND(
                            uuid='3456-7891',
                            status=u'closed',
                            titles=BIND(
                                BIND(u'Child Folder', lang='de'),
                            ),
                        ),
                    ),
                ),
            ),
        )
        self.assertIsNotNone(repr(dossier))
        self.assertIsNotNone(str(dossier))

        self.assertEqual(repr(dossier), str(dossier))
