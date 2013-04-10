from Products.Five.browser import BrowserView
from ftw.ech0039.bind import XMLExporter


class ExportView(BrowserView):
    """Render overview for all votes.
    """

    def __call__(self):

        memfile = XMLExporter(self.context).get_zipfile()
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
