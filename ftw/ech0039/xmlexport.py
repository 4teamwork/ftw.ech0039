from Products.ATContentTypes.interfaces import IFileContent
from Products.CMFCore.interfaces import IFolderish
from ftw.ech0039.pxbdebug import monkey_patch_pxb
from plone.uuid.interfaces import IUUID
from pyxb import BIND
from zope.component import adapts
from zope.component._api import getAdapter
from zope.interface import Interface
from zope.interface import implements
import os
import hashlib


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
        raise NotImplementedError()

    def add_to(self, bind_builder):
        raise NotImplementedError()

    def get_data(self):
        #XXX export should not know about binds
        return dict(uuid=self.uuid,
                    status=self.workflow_state,
                    titles=BIND(BIND(self.title, lang='de'))
                )


class FileExport(AbstractExport):
    implements(IECH0039Exportable)
    adapts(IFileContent)

    def add_to(self, bind_builder):
        bind_builder.add_document(self)

    @property
    def workflow_state(self):
        """ Must be one of:
            <xs:enumeration value="undefined"/>
            <xs:enumeration value="created"/>
            <xs:enumeration value="in_process"/>
            <xs:enumeration value="signed"/>
            <xs:enumeration value="approved"/>
            <xs:enumeration value="sent"/>
            <xs:enumeration value="canceled"/>
            <xs:enumeration value="invalidated"/>
            <xs:enumeration value="archived"/>
            <xs:enumeration value="preserved"/>
        """
        # just return closed untila a mapping for our workflow states is
        # available.
        #return api.content.get_state(self.context)
        return 'approved'

    def get_data(self, zipfile):
        data = super(FileExport, self).get_data()
        #XXX export should not know about binds

        filename = self.context.getFilename()
        _base, file_extension = os.path.splitext(filename)
        filepath = u'files/{}{}'.format(self.uuid, file_extension)
        headers = self.context.getMetadataHeaders()
        mime_type = dict(headers).get('Format', 'application/octet-stream')

        file_content = self.context.get_data()
        hashcode = hashlib.sha256(file_content).hexdigest()
        zipfile.writestr(filepath, file_content)

        data['files'] = BIND(BIND(
            pathFileName=filepath,
            mimeType=mime_type,
            hashCode=hashcode,
            hashCodeAlgorithm=u'SHA-256',
            ))
        return data


class FolderExport(AbstractExport):
    implements(IECH0039Exportable)
    adapts(IFolderish)

    def add_to(self, bind_builder):
        bind_builder.add_dossier(self)

    @property
    def workflow_state(self):
        """ Must be one of:
            <xs:enumeration value="undefined"/>
            <xs:enumeration value="created"/>
            <xs:enumeration value="in_process"/>
            <xs:enumeration value="moved"/>
            <xs:enumeration value="canceled"/>
            <xs:enumeration value="closed"/>
            <xs:enumeration value="archived"/>
            <xs:enumeration value="invalidated"/>
            <xs:enumeration value="in_selection"/>
            <xs:enumeration value="preserved"/>
        """
        # just return closed untila a mapping for our workflow states is
        # available.
        #return api.content.get_state(self.context)
        return 'closed'

    def get_children(self):
        for content in self.context.listFolderContents():
            adapter = getAdapter(content, interface=IECH0039Exportable)
            if adapter:
                yield adapter
