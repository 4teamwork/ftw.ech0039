# ./ftw/ech0039/bindings/eCH0044.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:74f799d93497653c948719b2a3ec36bcf58150b6
# Generated 2013-04-08 08:34:57.868653 by PyXB version 1.2.1
# Namespace http://www.ech.ch/xmlns/eCH-0044/1 [xmlns:eCH-0044]

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

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.ech.ch/xmlns/eCH-0044/1', create_if_missing=True)
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


# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0044/1}personIdCategoryType
class personIdCategoryType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'personIdCategoryType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 8, 1)
    _Documentation = None
personIdCategoryType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
personIdCategoryType._InitializeFacetMap(personIdCategoryType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'personIdCategoryType', personIdCategoryType)

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 17, 4)
    _Documentation = None
STD_ANON._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
STD_ANON._InitializeFacetMap(STD_ANON._CF_maxLength)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0044/1}baseNameType
class baseNameType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'baseNameType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 55, 1)
    _Documentation = None
baseNameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(100L))
baseNameType._InitializeFacetMap(baseNameType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'baseNameType', baseNameType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0044/1}officialFirstNameType
class officialFirstNameType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'officialFirstNameType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 60, 1)
    _Documentation = None
officialFirstNameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(50L))
officialFirstNameType._CF_whiteSpace = pyxb.binding.facets.CF_whiteSpace(value=pyxb.binding.facets._WhiteSpace_enum.collapse)
officialFirstNameType._InitializeFacetMap(officialFirstNameType._CF_maxLength,
   officialFirstNameType._CF_whiteSpace)
Namespace.addCategoryObject('typeBinding', u'officialFirstNameType', officialFirstNameType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0044/1}sexType
class sexType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'sexType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 66, 1)
    _Documentation = None
sexType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=sexType, enum_prefix=None)
sexType.n1 = sexType._CF_enumeration.addEnumeration(unicode_value=u'1', tag=u'n1')
sexType.n2 = sexType._CF_enumeration.addEnumeration(unicode_value=u'2', tag=u'n2')
sexType._InitializeFacetMap(sexType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'sexType', sexType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0044/1}vnType
class vnType (pyxb.binding.datatypes.unsignedLong):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'vnType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 72, 1)
    _Documentation = None
vnType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=vnType, value=pyxb.binding.datatypes.unsignedLong(7560000000001L))
vnType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=vnType, value=pyxb.binding.datatypes.unsignedLong(7569999999999L))
vnType._InitializeFacetMap(vnType._CF_minInclusive,
   vnType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', u'vnType', vnType)

# Complex type {http://www.ech.ch/xmlns/eCH-0044/1}namedPersonIdType with content type ELEMENT_ONLY
class namedPersonIdType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ech.ch/xmlns/eCH-0044/1}namedPersonIdType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'namedPersonIdType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 13, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}personIdCategory uses Python identifier personIdCategory
    __personIdCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'personIdCategory'), 'personIdCategory', '__httpwww_ech_chxmlnseCH_00441_namedPersonIdType_httpwww_ech_chxmlnseCH_00441personIdCategory', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 15, 3), )

    
    personIdCategory = property(__personIdCategory.value, __personIdCategory.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}personId uses Python identifier personId
    __personId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'personId'), 'personId', '__httpwww_ech_chxmlnseCH_00441_namedPersonIdType_httpwww_ech_chxmlnseCH_00441personId', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 16, 3), )

    
    personId = property(__personId.value, __personId.set, None, None)


    _ElementMap = {
        __personIdCategory.name() : __personIdCategory,
        __personId.name() : __personId
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'namedPersonIdType', namedPersonIdType)


# Complex type {http://www.ech.ch/xmlns/eCH-0044/1}personIdentificationType with content type ELEMENT_ONLY
class personIdentificationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ech.ch/xmlns/eCH-0044/1}personIdentificationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'personIdentificationType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 25, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}vn uses Python identifier vn
    __vn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'vn'), 'vn', '__httpwww_ech_chxmlnseCH_00441_personIdentificationType_httpwww_ech_chxmlnseCH_00441vn', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 27, 3), )

    
    vn = property(__vn.value, __vn.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}localPersonId uses Python identifier localPersonId
    __localPersonId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'localPersonId'), 'localPersonId', '__httpwww_ech_chxmlnseCH_00441_personIdentificationType_httpwww_ech_chxmlnseCH_00441localPersonId', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 28, 3), )

    
    localPersonId = property(__localPersonId.value, __localPersonId.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}OtherPersonId uses Python identifier OtherPersonId
    __OtherPersonId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'OtherPersonId'), 'OtherPersonId', '__httpwww_ech_chxmlnseCH_00441_personIdentificationType_httpwww_ech_chxmlnseCH_00441OtherPersonId', True, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 29, 3), )

    
    OtherPersonId = property(__OtherPersonId.value, __OtherPersonId.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}EuPersonId uses Python identifier EuPersonId
    __EuPersonId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EuPersonId'), 'EuPersonId', '__httpwww_ech_chxmlnseCH_00441_personIdentificationType_httpwww_ech_chxmlnseCH_00441EuPersonId', True, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 30, 3), )

    
    EuPersonId = property(__EuPersonId.value, __EuPersonId.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}officialName uses Python identifier officialName
    __officialName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'officialName'), 'officialName', '__httpwww_ech_chxmlnseCH_00441_personIdentificationType_httpwww_ech_chxmlnseCH_00441officialName', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 31, 3), )

    
    officialName = property(__officialName.value, __officialName.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'firstName'), 'firstName', '__httpwww_ech_chxmlnseCH_00441_personIdentificationType_httpwww_ech_chxmlnseCH_00441firstName', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 32, 3), )

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}sex uses Python identifier sex
    __sex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sex'), 'sex', '__httpwww_ech_chxmlnseCH_00441_personIdentificationType_httpwww_ech_chxmlnseCH_00441sex', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 33, 3), )

    
    sex = property(__sex.value, __sex.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}dateOfBirth uses Python identifier dateOfBirth
    __dateOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dateOfBirth'), 'dateOfBirth', '__httpwww_ech_chxmlnseCH_00441_personIdentificationType_httpwww_ech_chxmlnseCH_00441dateOfBirth', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 34, 3), )

    
    dateOfBirth = property(__dateOfBirth.value, __dateOfBirth.set, None, None)


    _ElementMap = {
        __vn.name() : __vn,
        __localPersonId.name() : __localPersonId,
        __OtherPersonId.name() : __OtherPersonId,
        __EuPersonId.name() : __EuPersonId,
        __officialName.name() : __officialName,
        __firstName.name() : __firstName,
        __sex.name() : __sex,
        __dateOfBirth.name() : __dateOfBirth
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'personIdentificationType', personIdentificationType)


# Complex type {http://www.ech.ch/xmlns/eCH-0044/1}personIdentificationPartnerType with content type ELEMENT_ONLY
class personIdentificationPartnerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ech.ch/xmlns/eCH-0044/1}personIdentificationPartnerType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'personIdentificationPartnerType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 37, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}vn uses Python identifier vn
    __vn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'vn'), 'vn', '__httpwww_ech_chxmlnseCH_00441_personIdentificationPartnerType_httpwww_ech_chxmlnseCH_00441vn', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 39, 3), )

    
    vn = property(__vn.value, __vn.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}localPersonId uses Python identifier localPersonId
    __localPersonId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'localPersonId'), 'localPersonId', '__httpwww_ech_chxmlnseCH_00441_personIdentificationPartnerType_httpwww_ech_chxmlnseCH_00441localPersonId', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 40, 3), )

    
    localPersonId = property(__localPersonId.value, __localPersonId.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}OtherPersonId uses Python identifier OtherPersonId
    __OtherPersonId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'OtherPersonId'), 'OtherPersonId', '__httpwww_ech_chxmlnseCH_00441_personIdentificationPartnerType_httpwww_ech_chxmlnseCH_00441OtherPersonId', True, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 41, 3), )

    
    OtherPersonId = property(__OtherPersonId.value, __OtherPersonId.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}officialName uses Python identifier officialName
    __officialName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'officialName'), 'officialName', '__httpwww_ech_chxmlnseCH_00441_personIdentificationPartnerType_httpwww_ech_chxmlnseCH_00441officialName', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 42, 3), )

    
    officialName = property(__officialName.value, __officialName.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'firstName'), 'firstName', '__httpwww_ech_chxmlnseCH_00441_personIdentificationPartnerType_httpwww_ech_chxmlnseCH_00441firstName', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 43, 3), )

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}sex uses Python identifier sex
    __sex = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'sex'), 'sex', '__httpwww_ech_chxmlnseCH_00441_personIdentificationPartnerType_httpwww_ech_chxmlnseCH_00441sex', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 44, 3), )

    
    sex = property(__sex.value, __sex.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}dateOfBirth uses Python identifier dateOfBirth
    __dateOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dateOfBirth'), 'dateOfBirth', '__httpwww_ech_chxmlnseCH_00441_personIdentificationPartnerType_httpwww_ech_chxmlnseCH_00441dateOfBirth', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 45, 3), )

    
    dateOfBirth = property(__dateOfBirth.value, __dateOfBirth.set, None, None)


    _ElementMap = {
        __vn.name() : __vn,
        __localPersonId.name() : __localPersonId,
        __OtherPersonId.name() : __OtherPersonId,
        __officialName.name() : __officialName,
        __firstName.name() : __firstName,
        __sex.name() : __sex,
        __dateOfBirth.name() : __dateOfBirth
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'personIdentificationPartnerType', personIdentificationPartnerType)


# Complex type {http://www.ech.ch/xmlns/eCH-0044/1}datePartiallyKnownType with content type ELEMENT_ONLY
class datePartiallyKnownType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ech.ch/xmlns/eCH-0044/1}datePartiallyKnownType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'datePartiallyKnownType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 48, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}yearMonthDay uses Python identifier yearMonthDay
    __yearMonthDay = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'yearMonthDay'), 'yearMonthDay', '__httpwww_ech_chxmlnseCH_00441_datePartiallyKnownType_httpwww_ech_chxmlnseCH_00441yearMonthDay', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 50, 3), )

    
    yearMonthDay = property(__yearMonthDay.value, __yearMonthDay.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}yearMonth uses Python identifier yearMonth
    __yearMonth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'yearMonth'), 'yearMonth', '__httpwww_ech_chxmlnseCH_00441_datePartiallyKnownType_httpwww_ech_chxmlnseCH_00441yearMonth', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 51, 3), )

    
    yearMonth = property(__yearMonth.value, __yearMonth.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}year uses Python identifier year
    __year = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'year'), 'year', '__httpwww_ech_chxmlnseCH_00441_datePartiallyKnownType_httpwww_ech_chxmlnseCH_00441year', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 52, 3), )

    
    year = property(__year.value, __year.set, None, None)


    _ElementMap = {
        __yearMonthDay.name() : __yearMonthDay,
        __yearMonth.name() : __yearMonth,
        __year.name() : __year
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'datePartiallyKnownType', datePartiallyKnownType)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 79, 2)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ech.ch/xmlns/eCH-0044/1}personIdentification uses Python identifier personIdentification
    __personIdentification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'personIdentification'), 'personIdentification', '__httpwww_ech_chxmlnseCH_00441_CTD_ANON_httpwww_ech_chxmlnseCH_00441personIdentification', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 81, 4), )

    
    personIdentification = property(__personIdentification.value, __personIdentification.set, None, None)


    _ElementMap = {
        __personIdentification.name() : __personIdentification
    }
    _AttributeMap = {
        
    }



personIdentificationRoot = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'personIdentificationRoot'), CTD_ANON, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 78, 1))
Namespace.addCategoryObject('elementBinding', personIdentificationRoot.name().localName(), personIdentificationRoot)



namedPersonIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'personIdCategory'), personIdCategoryType, scope=namedPersonIdType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 15, 3)))

namedPersonIdType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'personId'), STD_ANON, scope=namedPersonIdType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 16, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(namedPersonIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'personIdCategory')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 15, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(namedPersonIdType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'personId')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 16, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
namedPersonIdType._Automaton = _BuildAutomaton()




personIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'vn'), vnType, scope=personIdentificationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 27, 3)))

personIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'localPersonId'), namedPersonIdType, scope=personIdentificationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 28, 3)))

personIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OtherPersonId'), namedPersonIdType, scope=personIdentificationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 29, 3)))

personIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EuPersonId'), namedPersonIdType, scope=personIdentificationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 30, 3)))

personIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'officialName'), baseNameType, scope=personIdentificationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 31, 3)))

personIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstName'), baseNameType, scope=personIdentificationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 32, 3)))

personIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sex'), sexType, scope=personIdentificationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 33, 3)))

personIdentificationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dateOfBirth'), datePartiallyKnownType, scope=personIdentificationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 34, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 27, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 29, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 30, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'vn')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 27, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'localPersonId')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 28, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OtherPersonId')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 29, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EuPersonId')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 30, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'officialName')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 31, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'firstName')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 32, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sex')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 33, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(personIdentificationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dateOfBirth')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 34, 3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
personIdentificationType._Automaton = _BuildAutomaton_()




personIdentificationPartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'vn'), vnType, scope=personIdentificationPartnerType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 39, 3)))

personIdentificationPartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'localPersonId'), namedPersonIdType, scope=personIdentificationPartnerType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 40, 3)))

personIdentificationPartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OtherPersonId'), namedPersonIdType, scope=personIdentificationPartnerType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 41, 3)))

personIdentificationPartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'officialName'), baseNameType, scope=personIdentificationPartnerType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 42, 3)))

personIdentificationPartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstName'), baseNameType, scope=personIdentificationPartnerType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 43, 3)))

personIdentificationPartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'sex'), sexType, scope=personIdentificationPartnerType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 44, 3)))

personIdentificationPartnerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dateOfBirth'), datePartiallyKnownType, scope=personIdentificationPartnerType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 45, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 39, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 41, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 44, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 45, 3))
    counters.add(cc_3)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personIdentificationPartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'vn')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personIdentificationPartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'localPersonId')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personIdentificationPartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'OtherPersonId')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personIdentificationPartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'officialName')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(personIdentificationPartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'firstName')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(personIdentificationPartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'sex')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 44, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(personIdentificationPartnerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dateOfBirth')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 45, 3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
personIdentificationPartnerType._Automaton = _BuildAutomaton_2()




datePartiallyKnownType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'yearMonthDay'), pyxb.binding.datatypes.date, scope=datePartiallyKnownType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 50, 3)))

datePartiallyKnownType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'yearMonth'), pyxb.binding.datatypes.gYearMonth, scope=datePartiallyKnownType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 51, 3)))

datePartiallyKnownType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'year'), pyxb.binding.datatypes.gYear, scope=datePartiallyKnownType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 52, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(datePartiallyKnownType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'yearMonthDay')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 50, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(datePartiallyKnownType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'yearMonth')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 51, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(datePartiallyKnownType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'year')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 52, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
datePartiallyKnownType._Automaton = _BuildAutomaton_3()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'personIdentification'), personIdentificationType, scope=CTD_ANON, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 81, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'personIdentification')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0044/1/eCH-0044-1-1.xsd', 81, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_4()

