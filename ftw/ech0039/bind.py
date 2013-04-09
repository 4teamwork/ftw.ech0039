from ftw.ech0039.bindings import eCH0039
from ftw.ech0039.bindings import eCH0058
from ftw.ech0039.bindings import eCH0147T0
from ftw.ech0039.bindings import eCH0147T1
from ftw.ech0039.xmlexport import IECH0039Exportable
from pyxb import BIND
from pyxb.binding import datatypes as xs
from pyxb.utils.domutils import BindingDOMSupport
from pyxb.utils.domutils import SetDOMImplementation
import uuid
import xml.dom.minidom


# SetDOMImplementation is necessary to make 100% sure that pyxb finds a
# working DOM implementation.
# Pyxb does not provide a DOM-implementation name or a list of required
# DOM-implementation features. Thus it just uses an arbitrary that might not
# provide all the required features.
SetDOMImplementation(xml.dom.minidom.DOMImplementation())

# Namespace prefixes
BindingDOMSupport.DeclareNamespace(eCH0147T1.Namespace, 'eCH-0147T1')
BindingDOMSupport.DeclareNamespace(eCH0147T0.Namespace, 'eCH-0147T0')
BindingDOMSupport.DeclareNamespace(eCH0039.Namespace, 'eCH-0039')
BindingDOMSupport.DeclareNamespace(eCH0058.Namespace, 'eCH-0058')


class ContentBind(object):
    """Knows how to fill the xml content node.
    """

    def __init__(self, *exportables):
        self.dossiers = []
        self.documents = []
        for exportable in exportables:
            self.add(exportable)

    def add(self, exportable):
        exportable.add_to(self)

    def add_dossier(self, exportable_dossier):
        self.dossiers.append(DossierBind(exportable_dossier))

    def add_document(self, exportable_document):
        self.documents.append(DocumentBind(exportable_document))

    def _make_kwargs(self):
        kwargs = dict()
        if self.dossiers:
            dossiers = [each.get_BIND() for each in self.dossiers]
            kwargs['dossiers'] = BIND(*dossiers)
        if self.documents:
            documents = [each.get_BIND() for each in self.documents]
            kwargs['documents'] = BIND(*documents)
        return kwargs

    def _make_args(self):
        return []

    def get_BIND(self):
        kwargs = self._make_kwargs()
        args = self._make_args()
        bind = BIND(*args, **kwargs)
        return bind


class DossierBind(ContentBind):

    def __init__(self, exportable_dossier):
        super(DossierBind, self).__init__()

        self.data = exportable_dossier.get_data()
        self._add_children(exportable_dossier)

    def _add_children(self, exportable_dossier):
        for child in exportable_dossier.get_children():
            self.add(child)

    def _make_kwargs(self):
        kwargs = super(DossierBind, self)._make_kwargs()
        kwargs.update(self.data)
        return kwargs


class DocumentBind(ContentBind):

    def __init__(self, exportable_document):
        super(DocumentBind, self).__init__()
        self.data = exportable_document.get_data()


class XMLExporter(object):

    def __init__(self, context):
        self.exportable = IECH0039Exportable(context)
        self.header = self._bind_header()
        self.content = self._bind_content()

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
            messageDate=xs.dateTime.today(),
            action=1,
            testDeliveryFlag=False,
        )

    def _bind_content(self):
        bind = ContentBind(self.exportable)
        return bind.get_BIND()

