from ftw.ech0039.bind import BIND
from ftw.ech0039.testing import ECH0039_FUNCTIONAL_FIXTURE
from ftw.ech0039.xmlexport import XMLExporter
from plone.uuid.interfaces import IUUID
from unittest2.case import TestCase


class TestECH0039Export(TestCase):

    layer = ECH0039_FUNCTIONAL_FIXTURE

    def setUp(self):
        super(TestECH0039Export, self).setUp()
        self.portal = self.layer['portal']

    def test_folder_dossier_export(self):
        """Test that a single folder is correctly exported as a dossier.
        """

        self.portal.invokeFactory('Folder', 'folder', title=u'Folder')
        folder = self.portal['folder']
        exporter = XMLExporter(folder)

        dossier = BIND(
            dossiers=BIND(
                BIND(
                    uuid=IUUID(folder),
                    status=u'closed',
                    titles=BIND(
                        BIND(u'Folder', lang='de'),
                    ),
                ),
            ),
        )

        self.assertEqual(dossier, exporter.content)
