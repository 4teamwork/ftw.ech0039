from ftw.ech0039.bind import BIND
from ftw.ech0039.testing import ECH0039_FUNCTIONAL_FIXTURE
from ftw.ech0039.xmlexport import XMLExporter
from plone.uuid.interfaces import IUUID
from unittest2.case import TestCase
from ftw.testing import MockTestCase
from StringIO import StringIO
import hashlib


PDF_DATA = '%PDF-1.4 fake pdf...'


class TestECH0039Export(MockTestCase):

    layer = ECH0039_FUNCTIONAL_FIXTURE

    def setUp(self):
        super(TestECH0039Export, self).setUp()
        self.portal = self.layer['portal']

    def test_folder_dossier_export(self):
        """Test that a single folder is exported correctly as a dossier.
        """

        self.portal.invokeFactory('Folder', 'folder', title=u'Folder')
        folder_content = self.portal['folder']
        exporter = XMLExporter(folder_content)

        dossier = BIND(
            dossiers=BIND(
                BIND(
                    uuid=IUUID(folder_content),
                    status=u'closed',
                    titles=BIND(
                        BIND(u'Folder', lang='de'),
                    ),
                ),
            ),
        )

        self.assertEqual(dossier, exporter.content)

    def test_document_export(self):
        """Test that a single file is exported correctly as a document.
        """
        memfile = StringIO(buf=PDF_DATA)
        memfile.filename = 'file.pdf'
        self.portal.invokeFactory('File', 'file', title=u'File',
                                   file=memfile)

        pdf_file = self.portal['file']
        exporter = XMLExporter(pdf_file)

        expected_uuid = IUUID(pdf_file)
        hash_code = hashlib.sha256(PDF_DATA).hexdigest()
        document = BIND(
            documents=BIND(
                BIND(
                    uuid=expected_uuid,
                    titles=BIND(
                        BIND(u'File', lang='de'),
                    ),
                    status=u'approved',
                    files=BIND(
                        BIND(
                            pathFileName=u'files/{}.pdf'.format(expected_uuid),
                            mimeType=u'application/pdf',
                            hashCode=hash_code,
                            hashCodeAlgorithm=u'SHA-256',
                        ),
                    ),
                ),
            ),
        )
        self.assertEqual(document, exporter.content)

