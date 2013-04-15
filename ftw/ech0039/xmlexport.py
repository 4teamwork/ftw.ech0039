from StringIO import StringIO
from ftw.ech0039.bind import BIND
from ftw.ech0039.bindings import eCH0147T1
from ftw.ech0039.exportable import IECH0039Exportable
from ftw.ech0039.marshal import ContentMarshaller
from pyxb.binding import datatypes
from zipfile import ZipFile
import uuid


class XMLExporter(object):

    XML_FILENAME = 'message.xml'

    def __init__(self, context):
        self.context = context
        self.exportable = IECH0039Exportable(context)
        self.marshaller = ContentMarshaller().add(self.exportable)

    def make_zipfile(self):
        memfile = StringIO()
        zipfile = ZipFile(memfile, mode='w')

        msg = eCH0147T1.message(header=self.get_header(),
                                content_=self.get_content())
        zipfile.writestr(self.XML_FILENAME, msg.toxml("UTF-8"))
        self.write_files(zipfile)
        zipfile.close()
        return memfile

    def write_files(self, zipfile):
        self.marshaller.write_files(zipfile)

    def get_content(self):
        return self.marshaller.get_bind()

    def get_header(self):
        return BIND(
            senderId='plone@4teamwork.ch',
            messageId=str(uuid.uuid4()),
            messageType=1,
            # messageGroup is mandatory in eCH 0030 V2.0 but was removed in V3.0
            messageGroup=BIND(messageGroupId=1, messageTypeId=1),
            sendingApplication=BIND(
                manufacturer='4teamwork GmbH',
                product='teamraum',
                productVersion='4.0',
            ),
            messageDate=datatypes.dateTime.today(),
            action=1,
            testDeliveryFlag=False,
        )
