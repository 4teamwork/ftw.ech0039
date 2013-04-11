from StringIO import StringIO
from ftw.ech0039.bind import BIND
from ftw.ech0039.bindings import eCH0147T1
from ftw.ech0039.exportable import IECH0039Exportable
from ftw.ech0039.marshal import ContentBind
from pyxb.binding import datatypes
from zipfile import ZipFile
import uuid


class XMLExporter(object):

    XML_FILENAME = 'message.xml'

    def __init__(self, context):
        self.memfile = StringIO()
        self.zipfile = ZipFile(self.memfile, mode='w')
        self.context = context
        self.exportable = IECH0039Exportable(context)
        self.header = self._bind_header()
        self.content = self._bind_content()

    def get_zipfile(self):
        xml_content = XMLExporter(self.context).toxml()
        self.zipfile.writestr(self.XML_FILENAME, xml_content)
        self.zipfile.close()
        return self.memfile

    def toxml(self):
        msg = eCH0147T1.message(header=self.header, content_=self.content)
        return msg.toxml("UTF-8")

    def _bind_header(self):
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

    def _bind_content(self):
        bind = ContentBind(exportable=self.exportable, zipfile=self.zipfile)
        return bind.get_BIND()
