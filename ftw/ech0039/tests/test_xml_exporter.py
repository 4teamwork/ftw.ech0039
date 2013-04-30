from ftw.ech0039.bind import BIND
from ftw.ech0039.testing import ECH0039_FUNCTIONAL_FIXTURE
from ftw.ech0039.xmlexport import XMLExporter
from ftw.testing import MockTestCase
from plone.uuid.interfaces import IUUID
from zipfile import ZipFile
import hashlib


class TestXmlExport(MockTestCase):

    layer = ECH0039_FUNCTIONAL_FIXTURE

    def setUp(self):
        super(TestXmlExport, self).setUp()
        self.portal = self.layer['portal']

    def test_dossier_export(self):
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

        self.assertEqual(dossier, exporter.get_content())

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
        self.assertEqual(document, exporter.get_content())

    def test_nested_dossier_export(self):
        """Test that nested folders are exported correctly.
        """

        parent_folder = self.portal['parent_folder_1']
        child_folder = self.portal['parent_folder_1']['child_folder']
        exporter = XMLExporter(parent_folder)

        dossier = BIND(
            dossiers=BIND(
                BIND(
                    uuid=IUUID(parent_folder),
                    status=u'closed',
                    titles=BIND(
                        BIND(u'Parent Folder', lang='de'),
                    ),
                    dossiers=BIND(
                        BIND(
                            uuid=IUUID(child_folder),
                            status=u'closed',
                            titles=BIND(
                                BIND(u'Child Folder', lang='de'),
                            ),
                        ),
                    ),
                ),
            ),
        )

        self.assertEqual(dossier, exporter.get_content())

    def test_nested_document_export(self):
        """Test that a nested document can be exported.
        """

        parent_folder = self.portal['parent_folder_2']
        child_file = self.portal['parent_folder_2']['child_file']
        exporter = XMLExporter(parent_folder)
        expected_file_uuid = IUUID(child_file)
        expected_filename = u'files/{}.txt'.format(expected_file_uuid)
        hash_code = hashlib.sha256('test-txt-file-content\n').hexdigest()

        dossier = BIND(
            dossiers=BIND(
                BIND(
                    uuid=IUUID(parent_folder),
                    status=u'closed',
                    titles=BIND(
                        BIND(u'Parent Folder', lang='de'),
                    ),
                    documents=BIND(
                        BIND(
                            uuid=expected_file_uuid,
                            titles=BIND(
                                BIND(u'Child File', lang='de'),
                            ),
                            status=u'approved',
                            files=BIND(
                                BIND(
                                    pathFileName=expected_filename,
                                    mimeType=u'text/plain',
                                    hashCode=hash_code,
                                    hashCodeAlgorithm=u'SHA-256',
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        )

        self.assertEqual(dossier, exporter.get_content())

    def test_zipfile_creation(self):
        """Test that the zipfiles contain all expected files.
        """

        parent_folder = self.portal['parent_folder_2']
        child_file = self.portal['parent_folder_2']['child_file']
        expected_file_uuid = IUUID(child_file)
        expected_filename = u'files/{}.txt'.format(expected_file_uuid)

        memfile = XMLExporter(parent_folder).make_zipfile()
        zipfile = ZipFile(memfile)
        self.assertEqual([XMLExporter.XML_FILENAME, expected_filename],
                         zipfile.namelist())
