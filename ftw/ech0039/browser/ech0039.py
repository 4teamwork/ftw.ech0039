from Products.Five.browser import BrowserView
from StringIO import StringIO
from zipfile import ZipFile
from ftw.ech0039.bind import XMLExporter


class ExportView(BrowserView):
    """Render overview for all votes.
    """

    def __call__(self):
        xml_content = XMLExporter(self.context).toxml()
        memfile = StringIO()
        zipfile = ZipFile(memfile, mode='w')
        zipfile.writestr(self.context.title + '.xml', xml_content)
        zipfile.close()

        filename = self.context.title.encode('utf-8') + '.zip'

        self._write_to_response(memfile, filename)

    def _write_to_response(self, stringio, zipfilename):
        """Write content of StringIO to response and set zip-file header.
        """

        self.context.REQUEST.RESPONSE.setHeader(
                                    'content-type',
                                    'application/zip')
        self.context.REQUEST.RESPONSE.setHeader(
                                    'content-length',
                                    str(stringio.len))
        self.context.REQUEST.RESPONSE.setHeader(
                                    'Content-Disposition',
                                    ' attachment; filename=' + zipfilename)

        self.context.REQUEST.RESPONSE.write(stringio.getvalue())
