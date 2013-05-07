from Products.Five.browser import BrowserView
from StringIO import StringIO
from ftw.ech0039.xmlexport import XMLExporter
from plone.uuid.interfaces import IUUID


class ExportView(BrowserView):

    def __call__(self):
        memfile = XMLExporter(self.context).make_zipfile(StringIO())
        filename = IUUID(self.context)
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
