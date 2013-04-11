from ftw.ech0039.bind import BIND
from ftw.ech0039.testing import ECH0039_FUNCTIONAL_FIXTURE
from ftw.ech0039.xmlexport import XMLExporter
from plone.uuid.interfaces import IUUID
from unittest2.case import TestCase


PDF_DATA = '%PDF-1.4 fake pdf...'


class TestECH0039Export(TestCase):

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
        self.portal.invokeFactory('File', 'file', title=u'File',
                                   file=PDF_DATA)
        file_content = self.portal['file']
        file_content.setFilename(u'file.pdf')

        exporter = XMLExporter(file_content)
        exporter.content
