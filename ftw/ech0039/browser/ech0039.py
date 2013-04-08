from Products.Five.browser import BrowserView
from StringIO import StringIO
from ftw.ech0039.bind import DefaultBind
from zipfile import ZipFile


class ExportView(BrowserView):
    """Render overview for all votes.
    """

    def __call__(self):
        xml_content = DefaultBind(self.context).toxml()
        memfile = StringIO()
        zipfile = ZipFile(memfile, mode='w')
        zipfile.writestr(self.context.title + '.xml', xml_content)
        zipfile.close()

        self._write_to_response(memfile, self.context.title + '.zip')

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
