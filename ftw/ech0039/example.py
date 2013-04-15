from pyxb.binding import datatypes as xs
from pyxb import BIND
from pyxb.utils.domutils import BindingDOMSupport
from ftw.ech0039.bindings import eCH0147T1, eCH0147T0, eCH0039, eCH0058

# Namespace prefixes
BindingDOMSupport.DeclareNamespace(eCH0147T1.Namespace, 'eCH-0147T1')
BindingDOMSupport.DeclareNamespace(eCH0147T0.Namespace, 'eCH-0147T0')
BindingDOMSupport.DeclareNamespace(eCH0039.Namespace, 'eCH-0039')
BindingDOMSupport.DeclareNamespace(eCH0058.Namespace, 'eCH-0058')


header = BIND(
    senderId='plone@4teamwork.ch',
    messageId='5cfda51e-0261-4e9f-a045-c73003ebc7bb',
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

content = BIND(
    dossiers=BIND(
        BIND(
            uuid=u'369151ee-80c7-4eab-a3ca-450552433341',
            status=u'closed',
            titles=BIND(
                BIND(u'Deutscher Titel', lang='de'),
                BIND(u'Titre fran\xe7ais', lang='fr'),
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


dossier = BIND(
    dossiers=BIND(
        BIND(
            uuid=u'b78f19a669a24597af1c3b2120e19eb7',
            status=u'closed',
            titles=BIND(
                BIND(u'i am a folder. for real.', lang='de'),
            ),
        ),
    ),
)


if __name__ == '__main__':
    msg = eCH0147T1.message(header=header, content_=content)

    from ivbe.intranet.bindings import appcustom
    teamraum = appcustom.teamraum()
    teamraum.append(BIND(key='key1', value_='value1'))
    teamraum.append(BIND(key='key2', value_='value2'))
    msg.content_.dossiers.content()[0].applicationCustom.append(BIND(teamraum))

    print msg.toxml("UTF-8")
