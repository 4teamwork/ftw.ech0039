from StringIO import StringIO
from ftw.ech0039.bind import BIND
from ftw.ech0039.bindings import eCH0147T1
from ftw.ech0039.marshal import ContentMarshaller
from pyxb.binding import datatypes
from zipfile import ZipFile
import uuid
from plone.memoize import instance


class XMLExporter(object):

    XML_FILENAME = 'message.xml'

    def __init__(self, context):
        self.context = context
        self.marshaller = ContentMarshaller().add(self.context)

    def make_zipfile(self, output_file):
        zipfile = ZipFile(output_file, mode='w')
        zipfile.writestr(self.XML_FILENAME, self.get_xml_message())
        self.write_files(zipfile)
        zipfile.close()
        return output_file

    def get_xml_message(self):
        """Return the xml message as string.
        """

        msg = eCH0147T1.message(header=self.get_header(),
                                content_=self.get_content())
        return msg.toDOM().toprettyxml(encoding="UTF-8")

    def write_files(self, zipfile):
        """Write all files to the zipfile.
        """

        self.marshaller.write_files(zipfile)

    def get_content(self):
        """Return bound xml content.
        """

        return self.marshaller.get_bind()

    @instance.memoize
    def get_header(self):
        """Return bound xml header.
        """

        return BIND(
            senderId='plone@4teamwork.ch',
            messageId=str(uuid.uuid4()),
            messageType=1,
            # messageGroup is mandatory in eCH0030 V2.0 but was removed in V3.0
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
