from ftw.ech0039.bindings import eCH0039
from ftw.ech0039.bindings import eCH0058
from ftw.ech0039.bindings import eCH0147T0
from ftw.ech0039.bindings import eCH0147T1
from plone.uuid.interfaces import IUUID
from pyxb import BIND
from pyxb.binding import datatypes as xs
from pyxb.utils.domutils import BindingDOMSupport
from pyxb.utils.domutils import SetDOMImplementation
import uuid
import xml.dom.minidom
from plone import api


#  SetDOMImplementation is necessary to make 100% sure that there is a working
#  zip implementation.
SetDOMImplementation(xml.dom.minidom.DOMImplementation())

# Namespace prefixes
BindingDOMSupport.DeclareNamespace(eCH0147T1.Namespace, 'eCH-0147T1')
BindingDOMSupport.DeclareNamespace(eCH0147T0.Namespace, 'eCH-0147T0')
BindingDOMSupport.DeclareNamespace(eCH0039.Namespace, 'eCH-0039')
BindingDOMSupport.DeclareNamespace(eCH0058.Namespace, 'eCH-0058')


class DefaultBind(object):

    def __init__(self, context):
        self._dossier = context
        import pudb; pudb.set_trace()
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
        dossier_uuid = api.content.get_uuid(obj=self._dossier)

        return BIND(
            dossiers=BIND(
                BIND(
                    uuid=dossier_uuid,
                    status=u'closed',
                    titles=BIND(
                        BIND(self._dossier.title, lang='de'),
                    ),
                    documents=BIND(
                        BIND(
                            uuid=u'91e7b933-fe57-4b5f-ae7c-5d49ba5b70fd',
                            titles=BIND(
                                BIND(u'Deutscher Titel', lang='de'),
                                BIND(u'Titre fran\xe7ais', lang='fr'),
                            ),
                            status=u'approved',
                            files=BIND(
                                BIND(
                                    pathFileName=u'files/document.doc',
                                    mimeType=u'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                                    hashCode=u'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3',
                                    hashCodeAlgorithm=u'SHA-256',
                                ),
                            ),
                        ),
                    ),
                ),
            ),
        )
