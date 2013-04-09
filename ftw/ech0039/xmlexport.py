from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.interfaces import IFolderish
from plone import api
from plone.uuid.interfaces import IUUID
from pyxb import BIND
from zope.component import adapts
from zope.interface import Interface
from zope.interface import implements


class IECH0039Exportable(Interface):
    pass


class AbstractExport(object):

    def __init__(self, context):
        self.context = context

    @property
    def uuid(self):
        return IUUID(self.context)

    @property
    def title(self):
        return self.context.title

    @property
    def workflow_state(self):
        return api.content.get_state(self.context)

    def add_to(self, bind_builder):
        raise NotImplementedError()

    def get_data(self):
        #XXX export should not know about binds
        return dict(uuid=self.uuid,
                    status=self.workflow_state,
                    titles=BIND(BIND(self.title, lang='de'))
                )


class FolderExport(AbstractExport):
    implements(IECH0039Exportable)
    adapts(IFolderish)

    def add_to(self, bind_builder):
        bind_builder.add_dossier(self)

    def get_children(self):
        for child in self.context.getFolderContents():
            yield IECH0039Exportable(child)


class ItemExport(AbstractExport):
    implements(IECH0039Exportable)
    adapts(IContentish)

    def add_to(self, bind_builder):
        bind_builder.add_document(self)

    def get_data(self):
        data = super(ItemExport, self).get_data()
        data['files'] = BIND(BIND(
            pathFileName=u'files/document.doc',
            mimeType=u'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
            hashCode=u'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',
            hashCodeAlgorithm=u'SHA-256',
            ))
        return data
