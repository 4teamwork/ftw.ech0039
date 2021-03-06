from ftw.ech0039.bind import BIND
from ftw.ech0039.interfaces import IECH0039Document
from ftw.ech0039.interfaces import IECH0039Dossier
from ftw.ech0039.interfaces import IECH0039Exportable
from zope.component import queryAdapter


class ContentMarshaller(object):
    """Knows how to fill the main xml content node.
    """

    def __init__(self):
        self.dossiers = []
        self.documents = []

    def add(self, exportable):
        adapter = queryAdapter(exportable, IECH0039Exportable)
        if adapter:
            adapter.add_to(self)
        return self

    def write_files(self, zipfile):
        """Write all documents to the zipfile.
        """
        for each in self.dossiers:
            each.write_files(zipfile)
        for each in self.documents:
            each.write_file(zipfile)

    def add_dossier(self, exportable_dossier):
        adapter = IECH0039Dossier(exportable_dossier)
        self.dossiers.append(DossierMarshaller(adapter))

    def add_document(self, exportable_document):
        adapter = IECH0039Document(exportable_document)
        self.documents.append(DocumentMarshaller(adapter))

    def _make_kwargs(self):
        kwargs = dict()
        if self.dossiers:
            dossiers = [each.get_bind() for each in self.dossiers]
            kwargs['dossiers'] = BIND(*dossiers)
        if self.documents:
            documents = [each.get_bind() for each in self.documents]
            kwargs['documents'] = BIND(*documents)
        return kwargs

    def _make_args(self):
        return []

    def get_bind(self):
        kwargs = self._make_kwargs()
        args = self._make_args()
        return BIND(*args, **kwargs)


class DossierMarshaller(ContentMarshaller):

    def __init__(self, exportable_dossier):
        super(DossierMarshaller, self).__init__()

        self.data = exportable_dossier.get_data()
        self._add_children(exportable_dossier)

    def _add_children(self, exportable_dossier):
        for child in exportable_dossier.get_children():
            self.add(child)

    def _make_kwargs(self):
        kwargs = super(DossierMarshaller, self)._make_kwargs()
        kwargs.update(self.data)
        return kwargs


class DocumentMarshaller(object):

    def __init__(self, exportable_document):
        self.document = exportable_document
        self.data = self.document.get_data()

    def write_file(self, zipfile):
        self.document.write_file(zipfile)

    def get_bind(self):
        return BIND(**self.data)
