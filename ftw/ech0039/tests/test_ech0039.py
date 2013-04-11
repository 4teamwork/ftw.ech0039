from ftw.ech0039.bind import BIND
from ftw.ech0039.testing import ECH0039_FUNCTIONAL_FIXTURE
from ftw.ech0039.xmlexport import XMLExporter
from ftw.testing import MockTestCase
from plone.uuid.interfaces import IUUID
import hashlib


class TestECH0039Export(MockTestCase):

    layer = ECH0039_FUNCTIONAL_FIXTURE

    def setUp(self):
        super(TestECH0039Export, self).setUp()
        self.portal = self.layer['portal']

    def test_folder_dossier_export(self):
        """Test that a single folder is exported correctly as a dossier.
        """

        folder_content = self.portal['single_folder']
        exporter = XMLExporter(folder_content)

        dossier = BIND(
            dossiers=BIND(
                BIND(
                    uuid=IUUID(folder_content),
                    status=u'closed',
                    titles=BIND(
                        BIND(u'Single Folder', lang='de'),
                    ),
                ),
            ),
        )

        self.assertEqual(dossier, exporter.content)

    def test_document_export(self):
        """Test that a single file is exported correctly as a document.
        """

        txt_file = self.portal['single_file']
        exporter = XMLExporter(txt_file)

        expected_uuid = IUUID(txt_file)
        hash_code = hashlib.sha256('test-txt-file-content\n').hexdigest()
        document = BIND(
            documents=BIND(
                BIND(
                    uuid=expected_uuid,
                    titles=BIND(
                        BIND(u'Single File', lang='de'),
                    ),
                    status=u'approved',
                    files=BIND(
                        BIND(
                            pathFileName=u'files/{}.txt'.format(expected_uuid),
                            mimeType=u'text/plain',
                            hashCode=hash_code,
                            hashCodeAlgorithm=u'SHA-256',
                        ),
                    ),
                ),
            ),
        )
        self.assertEqual(document, exporter.content)

