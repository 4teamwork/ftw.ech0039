from ftw.ech0039.bind import BIND


class ContentBind(object):
    """Knows how to fill the xml content node.
    """

    def __init__(self, exportable=None, zipfile=None):
        self.dossiers = []
        self.documents = []
        self.zipfile = zipfile
        if exportable:
            self.add(exportable)

    def add(self, exportable):
        exportable.add_to(self)

    def add_dossier(self, exportable_dossier):
        self.dossiers.append(DossierBind(exportable_dossier,
                                         zipfile=self.zipfile))

    def add_document(self, exportable_document):
        self.documents.append(DocumentBind(exportable_document,
                                           zipfile=self.zipfile))

    def _make_kwargs(self):
        kwargs = dict()
        if self.dossiers:
            dossiers = [each.get_BIND() for each in self.dossiers]
            kwargs['dossiers'] = BIND(*dossiers)
        if self.documents:
            documents = [each.get_BIND() for each in self.documents]
            kwargs['documents'] = BIND(*documents)
        return kwargs

    def _make_args(self):
        return []

    def get_BIND(self):
        kwargs = self._make_kwargs()
        args = self._make_args()
        bind = BIND(*args, **kwargs)
        return bind


class DossierBind(ContentBind):

    def __init__(self, exportable_dossier, zipfile=None):
        super(DossierBind, self).__init__(zipfile=zipfile)

        self.data = exportable_dossier.get_data()
        self._add_children(exportable_dossier)

    def _add_children(self, exportable_dossier):
        for child in exportable_dossier.get_children():
            self.add(child)

    def _make_kwargs(self):
        kwargs = super(DossierBind, self)._make_kwargs()
        kwargs.update(self.data)
        return kwargs


class DocumentBind(ContentBind):

    def __init__(self, exportable_document, zipfile=None):
        super(DocumentBind, self).__init__(zipfile=zipfile)
        self.data = exportable_document.get_data(self.zipfile)

    def _make_kwargs(self):
        kwargs = super(DocumentBind, self)._make_kwargs()
        kwargs.update(self.data)
        return kwargs
