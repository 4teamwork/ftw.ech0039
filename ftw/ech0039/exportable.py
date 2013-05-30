from Products.ATContentTypes.interfaces import IFileContent
from Products.CMFCore.interfaces import IFolderish
from collections import OrderedDict
from ftw.ech0039.bind import BIND
from ftw.ech0039.interfaces import IECH0039Document
from ftw.ech0039.interfaces import IECH0039Dossier
from plone.uuid.interfaces import IUUID
from zope.component import adapts
from zope.interface import implements
import hashlib
import os


DEFAULT_MIME_TYPE = 'application/octet-stream'


class AbstractExportable(object):

    def __init__(self, context):
        self.context = context

    def add_to(self, marshaller):
        raise NotImplementedError()

    @property
    def workflow_state(self):
        raise NotImplementedError()

    @property
    def uuid(self):
        return IUUID(self.context)

    @property
    def title(self):
        return self.context.title

    def get_data(self):
        return OrderedDict(uuid=self.uuid,
                           status=self.workflow_state,
                           titles=BIND(BIND(self.title, lang='de'))
                           )


class FileAdapter(AbstractExportable):
    implements(IECH0039Document)
    adapts(IFileContent)

    def add_to(self, marshaller):
        marshaller.add_document(self)

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

        Return approved until a a mapping for our workflow states is
        available.

        """
        return 'approved'

    @property
    def file_path(self):
        filename = self.context.getFilename()
        _base, file_extension = os.path.splitext(filename)
        return u'files/{}{}'.format(self.uuid, file_extension)

    @property
    def file_content(self):
        return self.context.get_data()

    @property
    def mime_type(self):
        headers = self.context.getMetadataHeaders()
        return dict(headers).get('Format', DEFAULT_MIME_TYPE)

    @property
    def hash_code(self):
        return hashlib.sha256(self.file_content).hexdigest()

    @property
    def hash_function_name(self):
        return u'SHA-256'

    def append_files(self, data):
        data['files'] = BIND(BIND(
                pathFileName=self.file_path,
                mimeType=self.mime_type,
                hashCode=self.hash_code,
                hashCodeAlgorithm=self.hash_function_name,
            ))

    def get_data(self):
        data = super(FileAdapter, self).get_data()
        self.append_files(data)
        return data

    def write_file(self, zipfile):
        zipfile.writestr(self.file_path, self.file_content)


class FolderAdapter(AbstractExportable):
    implements(IECH0039Dossier)
    adapts(IFolderish)

    def add_to(self, marshaller):
        marshaller.add_dossier(self)

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

        Return closed until a a mapping for our workflow states is available.

        """
        return 'closed'

    def get_children(self):
        return self.context.listFolderContents()
