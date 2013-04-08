# ./ftw/ech0039/bindings/eCH0147T1.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:9d7a30d1b6b0ef601242392269628535b2ba7d2e
# Generated 2013-04-08 08:34:57.870216 by PyXB version 1.2.1
# Namespace http://www.ech.ch/xmlns/eCH-0147/T1/1

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import StringIO
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:6db5aa07-a016-11e2-acc4-00254bc318a0')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import ftw.ech0039.bindings.eCH0147T0
import ftw.ech0039.bindings.eCH0039

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.ech.ch/xmlns/eCH-0147/T1/1', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
ModuleRecord = Namespace.lookupModuleRecordByUID(_GenerationUID, create_if_missing=True)
ModuleRecord._setModule(sys.modules[__name__])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.
    
    @kw default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    saxer.parse(StringIO.StringIO(xml_text))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {http://www.ech.ch/xmlns/eCH-0147/T1/1}messageType with content type ELEMENT_ONLY
class messageType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ech.ch/xmlns/eCH-0147/T1/1}messageType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'messageType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 38, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element header uses Python identifier header
    __header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'header'), 'header', '__httpwww_ech_chxmlnseCH_0147T11_messageType_header', False, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 40, 3), )

    
    header = property(__header.value, __header.set, None, None)

    
    # Element content uses Python identifier content_
    __content = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'content'), 'content_', '__httpwww_ech_chxmlnseCH_0147T11_messageType_content', False, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 41, 3), )

    
    content_ = property(__content.value, __content.set, None, None)


    _ElementMap = {
        __header.name() : __header,
        __content.name() : __content
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'messageType', messageType)


# Complex type {http://www.ech.ch/xmlns/eCH-0147/T1/1}contentType with content type ELEMENT_ONLY
class contentType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ech.ch/xmlns/eCH-0147/T1/1}contentType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'contentType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 44, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element directive uses Python identifier directive
    __directive = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'directive'), 'directive', '__httpwww_ech_chxmlnseCH_0147T11_contentType_directive', False, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 46, 3), )

    
    directive = property(__directive.value, __directive.set, None, None)

    
    # Element dossiers uses Python identifier dossiers
    __dossiers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'dossiers'), 'dossiers', '__httpwww_ech_chxmlnseCH_0147T11_contentType_dossiers', False, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 47, 3), )

    
    dossiers = property(__dossiers.value, __dossiers.set, None, None)

    
    # Element documents uses Python identifier documents
    __documents = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'documents'), 'documents', '__httpwww_ech_chxmlnseCH_0147T11_contentType_documents', False, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 48, 3), )

    
    documents = property(__documents.value, __documents.set, None, None)

    
    # Element addresses uses Python identifier addresses
    __addresses = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'addresses'), 'addresses', '__httpwww_ech_chxmlnseCH_0147T11_contentType_addresses', False, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 49, 3), )

    
    addresses = property(__addresses.value, __addresses.set, None, None)


    _ElementMap = {
        __directive.name() : __directive,
        __dossiers.name() : __dossiers,
        __documents.name() : __documents,
        __addresses.name() : __addresses
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'contentType', contentType)


# Complex type {http://www.ech.ch/xmlns/eCH-0147/T1/1}directiveType with content type ELEMENT_ONLY
class directiveType (pyxb.binding.basis.complexTypeDefinition):
    """Anweisung: Basiskomponente zur Abbildung von Bearbeitungsanweisungen an den Empfänger."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'directiveType')
    _XSDLocation = pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 53, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element uuid uses Python identifier uuid
    __uuid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'uuid'), 'uuid', '__httpwww_ech_chxmlnseCH_0147T11_directiveType_uuid', False, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 58, 3), )

    
    uuid = property(__uuid.value, __uuid.set, None, u'UUID: Universally Unique Identifier der Anweisung. Referenz des Objekts, nicht der Nachricht.')

    
    # Element instruction uses Python identifier instruction
    __instruction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'instruction'), 'instruction', '__httpwww_ech_chxmlnseCH_0147T11_directiveType_instruction', False, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 63, 3), )

    
    instruction = property(__instruction.value, __instruction.set, None, None)

    
    # Element priority uses Python identifier priority
    __priority = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'priority'), 'priority', '__httpwww_ech_chxmlnseCH_0147T11_directiveType_priority', False, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 65, 3), )

    
    priority = property(__priority.value, __priority.set, None, None)

    
    # Element titles uses Python identifier titles
    __titles = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'titles'), 'titles', '__httpwww_ech_chxmlnseCH_0147T11_directiveType_titles', False, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 66, 3), )

    
    titles = property(__titles.value, __titles.set, None, u'Titel: Benennung von T\xe4tigkeit und Gegenstand des Gesch\xe4ftsvorfalls.')

    
    # Element deadline uses Python identifier deadline
    __deadline = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'deadline'), 'deadline', '__httpwww_ech_chxmlnseCH_0147T11_directiveType_deadline', False, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 71, 3), )

    
    deadline = property(__deadline.value, __deadline.set, None, u'Bearbeitungsfrist: Tag, an dem die Aktivit\xe4t erledigt sein soll.')

    
    # Element serviceId uses Python identifier serviceId
    __serviceId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'serviceId'), 'serviceId', '__httpwww_ech_chxmlnseCH_0147T11_directiveType_serviceId', False, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 76, 3), )

    
    serviceId = property(__serviceId.value, __serviceId.set, None, u'Leistungsidentifikation: Identifikation der Leistung gem\xe4ss eCH-0070 Leistungsinventar eGov CH.')

    
    # Element comments uses Python identifier comments
    __comments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'comments'), 'comments', '__httpwww_ech_chxmlnseCH_0147T11_directiveType_comments', False, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 81, 3), )

    
    comments = property(__comments.value, __comments.set, None, None)

    
    # Element applicationCustom uses Python identifier applicationCustom
    __applicationCustom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, u'applicationCustom'), 'applicationCustom', '__httpwww_ech_chxmlnseCH_0147T11_directiveType_applicationCustom', True, pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 82, 3), )

    
    applicationCustom = property(__applicationCustom.value, __applicationCustom.set, None, None)


    _ElementMap = {
        __uuid.name() : __uuid,
        __instruction.name() : __instruction,
        __priority.name() : __priority,
        __titles.name() : __titles,
        __deadline.name() : __deadline,
        __serviceId.name() : __serviceId,
        __comments.name() : __comments,
        __applicationCustom.name() : __applicationCustom
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'directiveType', directiveType)


header = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'header'), ftw.ech0039.bindings.eCH0147T0.headerType, documentation=u'Root-Elements f\xfcr header.xml einer Erstmeldung nach eCH-0147T1.', location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 18, 1))
Namespace.addCategoryObject('elementBinding', header.name().localName(), header)

message = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'message'), messageType, documentation=u'Root-Elements f\xfcr message.xml einer Erstmeldung nach eCH-0147T1.', location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 23, 1))
Namespace.addCategoryObject('elementBinding', message.name().localName(), message)

reportHeader = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'reportHeader'), ftw.ech0039.bindings.eCH0147T0.reportHeaderType, documentation=u'Root-Element f\xfcr header.xml einer Antwortmeldung nach eCH-0147T1.', location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 28, 1))
Namespace.addCategoryObject('elementBinding', reportHeader.name().localName(), reportHeader)

eventReport = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'eventReport'), ftw.ech0039.bindings.eCH0147T0.eventReportType, documentation=u'Root-Element f\xfcr message.xml einer Antwortmeldung nach eCH-0147T1.', location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 33, 1))
Namespace.addCategoryObject('elementBinding', eventReport.name().localName(), eventReport)



messageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'header'), ftw.ech0039.bindings.eCH0147T0.headerType, scope=messageType, location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 40, 3)))

messageType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'content'), contentType, scope=messageType, location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 41, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(messageType._UseForTag(pyxb.namespace.ExpandedName(None, u'header')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 40, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(messageType._UseForTag(pyxb.namespace.ExpandedName(None, u'content')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 41, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
messageType._Automaton = _BuildAutomaton()




contentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'directive'), directiveType, scope=contentType, location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 46, 3)))

contentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'dossiers'), ftw.ech0039.bindings.eCH0147T0.dossiersType, scope=contentType, location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 47, 3)))

contentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'documents'), ftw.ech0039.bindings.eCH0147T0.documentsType, scope=contentType, location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 48, 3)))

contentType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'addresses'), ftw.ech0039.bindings.eCH0147T0.addressesType, scope=contentType, location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 49, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 46, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 47, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 48, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 49, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(contentType._UseForTag(pyxb.namespace.ExpandedName(None, u'directive')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 46, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(contentType._UseForTag(pyxb.namespace.ExpandedName(None, u'dossiers')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 47, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(contentType._UseForTag(pyxb.namespace.ExpandedName(None, u'documents')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 48, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(contentType._UseForTag(pyxb.namespace.ExpandedName(None, u'addresses')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 49, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
contentType._Automaton = _BuildAutomaton_()




directiveType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'uuid'), pyxb.binding.datatypes.token, scope=directiveType, documentation=u'UUID: Universally Unique Identifier der Anweisung. Referenz des Objekts, nicht der Nachricht.', location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 58, 3)))

directiveType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'instruction'), ftw.ech0039.bindings.eCH0039.directiveInstructionType, scope=directiveType, location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 63, 3)))

directiveType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'priority'), ftw.ech0039.bindings.eCH0039.priorityType, scope=directiveType, location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 65, 3)))

directiveType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'titles'), ftw.ech0039.bindings.eCH0039.titlesType, scope=directiveType, documentation=u'Titel: Benennung von T\xe4tigkeit und Gegenstand des Gesch\xe4ftsvorfalls.', location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 66, 3)))

directiveType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'deadline'), pyxb.binding.datatypes.date, scope=directiveType, documentation=u'Bearbeitungsfrist: Tag, an dem die Aktivit\xe4t erledigt sein soll.', location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 71, 3)))

directiveType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'serviceId'), pyxb.binding.datatypes.token, scope=directiveType, documentation=u'Leistungsidentifikation: Identifikation der Leistung gem\xe4ss eCH-0070 Leistungsinventar eGov CH.', location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 76, 3)))

directiveType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'comments'), ftw.ech0039.bindings.eCH0039.commentsType, scope=directiveType, location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 81, 3)))

directiveType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, u'applicationCustom'), ftw.ech0039.bindings.eCH0147T0.applicationCustomType, scope=directiveType, location=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 82, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 66, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 71, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 76, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 81, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 82, 3))
    counters.add(cc_4)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(directiveType._UseForTag(pyxb.namespace.ExpandedName(None, u'uuid')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 58, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(directiveType._UseForTag(pyxb.namespace.ExpandedName(None, u'instruction')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 63, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(directiveType._UseForTag(pyxb.namespace.ExpandedName(None, u'priority')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 65, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(directiveType._UseForTag(pyxb.namespace.ExpandedName(None, u'titles')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 66, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(directiveType._UseForTag(pyxb.namespace.ExpandedName(None, u'deadline')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 71, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(directiveType._UseForTag(pyxb.namespace.ExpandedName(None, u'serviceId')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 76, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(directiveType._UseForTag(pyxb.namespace.ExpandedName(None, u'comments')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 81, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(directiveType._UseForTag(pyxb.namespace.ExpandedName(None, u'applicationCustom')), pyxb.utils.utility.Location('/Users/tom/Plone/buildouts/ivbe-intranet/src/ftw.ech0039/ftw/ech0039/schemas/eCH-0147T1.xsd', 82, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
directiveType._Automaton = _BuildAutomaton_2()

