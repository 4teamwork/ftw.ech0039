# ./ftw/ech0039/bindings/eCH0010.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e748480a55ead84c56568153d044e26d44c2ec2f
# Generated 2013-04-08 08:34:57.868276 by PyXB version 1.2.1
# Namespace http://www.ech.ch/xmlns/eCH-0010/3 [xmlns:eCH-0010]

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

Namespace = pyxb.namespace.NamespaceForURI(u'http://www.ech.ch/xmlns/eCH-0010/3', create_if_missing=True)
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


# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}organisationNameType
class organisationNameType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'organisationNameType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 98, 1)
    _Documentation = None
organisationNameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
organisationNameType._InitializeFacetMap(organisationNameType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'organisationNameType', organisationNameType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}mrMrsType
class mrMrsType (pyxb.binding.datatypes.token, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'mrMrsType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 103, 1)
    _Documentation = None
mrMrsType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=mrMrsType, enum_prefix=None)
mrMrsType.n1 = mrMrsType._CF_enumeration.addEnumeration(unicode_value=u'1', tag=u'n1')
mrMrsType.n2 = mrMrsType._CF_enumeration.addEnumeration(unicode_value=u'2', tag=u'n2')
mrMrsType.n3 = mrMrsType._CF_enumeration.addEnumeration(unicode_value=u'3', tag=u'n3')
mrMrsType._InitializeFacetMap(mrMrsType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'mrMrsType', mrMrsType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}titleType
class titleType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'titleType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 110, 1)
    _Documentation = None
titleType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(20L))
titleType._InitializeFacetMap(titleType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'titleType', titleType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}firstNameType
class firstNameType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'firstNameType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 115, 1)
    _Documentation = None
firstNameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30L))
firstNameType._InitializeFacetMap(firstNameType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'firstNameType', firstNameType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}lastNameType
class lastNameType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'lastNameType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 120, 1)
    _Documentation = None
lastNameType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(30L))
lastNameType._InitializeFacetMap(lastNameType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'lastNameType', lastNameType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}addressLineType
class addressLineType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'addressLineType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 125, 1)
    _Documentation = None
addressLineType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
addressLineType._InitializeFacetMap(addressLineType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'addressLineType', addressLineType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}streetType
class streetType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'streetType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 130, 1)
    _Documentation = None
streetType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(60L))
streetType._InitializeFacetMap(streetType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'streetType', streetType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}houseNumberType
class houseNumberType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'houseNumberType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 135, 1)
    _Documentation = None
houseNumberType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(12L))
houseNumberType._InitializeFacetMap(houseNumberType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'houseNumberType', houseNumberType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}dwellingNumberType
class dwellingNumberType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'dwellingNumberType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 140, 1)
    _Documentation = None
dwellingNumberType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10L))
dwellingNumberType._InitializeFacetMap(dwellingNumberType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'dwellingNumberType', dwellingNumberType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}postOfficeBoxNumberType
class postOfficeBoxNumberType (pyxb.binding.datatypes.unsignedInt):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'postOfficeBoxNumberType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 145, 1)
    _Documentation = None
postOfficeBoxNumberType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=postOfficeBoxNumberType, value=pyxb.binding.datatypes.unsignedInt(9999L))
postOfficeBoxNumberType._InitializeFacetMap(postOfficeBoxNumberType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', u'postOfficeBoxNumberType', postOfficeBoxNumberType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}postOfficeBoxTextType
class postOfficeBoxTextType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'postOfficeBoxTextType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 150, 1)
    _Documentation = None
postOfficeBoxTextType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15L))
postOfficeBoxTextType._InitializeFacetMap(postOfficeBoxTextType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'postOfficeBoxTextType', postOfficeBoxTextType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}swissZipCodeType
class swissZipCodeType (pyxb.binding.datatypes.unsignedInt):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 155, 1)
    _Documentation = None
swissZipCodeType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=swissZipCodeType, value=pyxb.binding.datatypes.unsignedInt(1000L))
swissZipCodeType._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=swissZipCodeType, value=pyxb.binding.datatypes.unsignedInt(9999L))
swissZipCodeType._InitializeFacetMap(swissZipCodeType._CF_minInclusive,
   swissZipCodeType._CF_maxInclusive)
Namespace.addCategoryObject('typeBinding', u'swissZipCodeType', swissZipCodeType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}swissZipCodeAddOnType
class swissZipCodeAddOnType (pyxb.binding.datatypes.string):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeAddOnType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 161, 1)
    _Documentation = None
swissZipCodeAddOnType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
swissZipCodeAddOnType._InitializeFacetMap(swissZipCodeAddOnType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'swissZipCodeAddOnType', swissZipCodeAddOnType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}swissZipCodeIdType
class swissZipCodeIdType (pyxb.binding.datatypes.int):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeIdType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 166, 1)
    _Documentation = None
swissZipCodeIdType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', u'swissZipCodeIdType', swissZipCodeIdType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}foreignZipCodeType
class foreignZipCodeType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'foreignZipCodeType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 169, 1)
    _Documentation = None
foreignZipCodeType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(15L))
foreignZipCodeType._InitializeFacetMap(foreignZipCodeType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'foreignZipCodeType', foreignZipCodeType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}localityType
class localityType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'localityType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 174, 1)
    _Documentation = None
localityType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40L))
localityType._InitializeFacetMap(localityType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'localityType', localityType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}townType
class townType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'townType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 179, 1)
    _Documentation = None
townType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(40L))
townType._InitializeFacetMap(townType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'townType', townType)

# Atomic simple type: {http://www.ech.ch/xmlns/eCH-0010/3}countryType
class countryType (pyxb.binding.datatypes.token):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'countryType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 184, 1)
    _Documentation = None
countryType._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2L))
countryType._InitializeFacetMap(countryType._CF_maxLength)
Namespace.addCategoryObject('typeBinding', u'countryType', countryType)

# Atomic simple type: [anonymous]
class STD_ANON (countryType, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 90, 4)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.CH = STD_ANON._CF_enumeration.addEnumeration(unicode_value=u'CH', tag=u'CH')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)

# Complex type {http://www.ech.ch/xmlns/eCH-0010/3}mailAddressType with content type ELEMENT_ONLY
class mailAddressType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ech.ch/xmlns/eCH-0010/3}mailAddressType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'mailAddressType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 8, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}organisation uses Python identifier organisation
    __organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'organisation'), 'organisation', '__httpwww_ech_chxmlnseCH_00103_mailAddressType_httpwww_ech_chxmlnseCH_00103organisation', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 11, 4), )

    
    organisation = property(__organisation.value, __organisation.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'person'), 'person', '__httpwww_ech_chxmlnseCH_00103_mailAddressType_httpwww_ech_chxmlnseCH_00103person', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 12, 4), )

    
    person = property(__person.value, __person.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}addressInformation uses Python identifier addressInformation
    __addressInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'addressInformation'), 'addressInformation', '__httpwww_ech_chxmlnseCH_00103_mailAddressType_httpwww_ech_chxmlnseCH_00103addressInformation', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 14, 3), )

    
    addressInformation = property(__addressInformation.value, __addressInformation.set, None, None)


    _ElementMap = {
        __organisation.name() : __organisation,
        __person.name() : __person,
        __addressInformation.name() : __addressInformation
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'mailAddressType', mailAddressType)


# Complex type {http://www.ech.ch/xmlns/eCH-0010/3}personMailAddressType with content type ELEMENT_ONLY
class personMailAddressType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ech.ch/xmlns/eCH-0010/3}personMailAddressType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'personMailAddressType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 17, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}person uses Python identifier person
    __person = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'person'), 'person', '__httpwww_ech_chxmlnseCH_00103_personMailAddressType_httpwww_ech_chxmlnseCH_00103person', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 19, 3), )

    
    person = property(__person.value, __person.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}addressInformation uses Python identifier addressInformation
    __addressInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'addressInformation'), 'addressInformation', '__httpwww_ech_chxmlnseCH_00103_personMailAddressType_httpwww_ech_chxmlnseCH_00103addressInformation', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 20, 3), )

    
    addressInformation = property(__addressInformation.value, __addressInformation.set, None, None)


    _ElementMap = {
        __person.name() : __person,
        __addressInformation.name() : __addressInformation
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'personMailAddressType', personMailAddressType)


# Complex type {http://www.ech.ch/xmlns/eCH-0010/3}personMailAddressInfoType with content type ELEMENT_ONLY
class personMailAddressInfoType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ech.ch/xmlns/eCH-0010/3}personMailAddressInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'personMailAddressInfoType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 23, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}mrMrs uses Python identifier mrMrs
    __mrMrs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'mrMrs'), 'mrMrs', '__httpwww_ech_chxmlnseCH_00103_personMailAddressInfoType_httpwww_ech_chxmlnseCH_00103mrMrs', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 25, 3), )

    
    mrMrs = property(__mrMrs.value, __mrMrs.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpwww_ech_chxmlnseCH_00103_personMailAddressInfoType_httpwww_ech_chxmlnseCH_00103title', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 26, 3), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'firstName'), 'firstName', '__httpwww_ech_chxmlnseCH_00103_personMailAddressInfoType_httpwww_ech_chxmlnseCH_00103firstName', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 27, 3), )

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'lastName'), 'lastName', '__httpwww_ech_chxmlnseCH_00103_personMailAddressInfoType_httpwww_ech_chxmlnseCH_00103lastName', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 28, 3), )

    
    lastName = property(__lastName.value, __lastName.set, None, None)


    _ElementMap = {
        __mrMrs.name() : __mrMrs,
        __title.name() : __title,
        __firstName.name() : __firstName,
        __lastName.name() : __lastName
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'personMailAddressInfoType', personMailAddressInfoType)


# Complex type {http://www.ech.ch/xmlns/eCH-0010/3}organisationMailAddressType with content type ELEMENT_ONLY
class organisationMailAddressType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ech.ch/xmlns/eCH-0010/3}organisationMailAddressType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'organisationMailAddressType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 31, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}organisation uses Python identifier organisation
    __organisation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'organisation'), 'organisation', '__httpwww_ech_chxmlnseCH_00103_organisationMailAddressType_httpwww_ech_chxmlnseCH_00103organisation', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 33, 3), )

    
    organisation = property(__organisation.value, __organisation.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}addressInformation uses Python identifier addressInformation
    __addressInformation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'addressInformation'), 'addressInformation', '__httpwww_ech_chxmlnseCH_00103_organisationMailAddressType_httpwww_ech_chxmlnseCH_00103addressInformation', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 34, 3), )

    
    addressInformation = property(__addressInformation.value, __addressInformation.set, None, None)


    _ElementMap = {
        __organisation.name() : __organisation,
        __addressInformation.name() : __addressInformation
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'organisationMailAddressType', organisationMailAddressType)


# Complex type {http://www.ech.ch/xmlns/eCH-0010/3}organisationMailAddressInfoType with content type ELEMENT_ONLY
class organisationMailAddressInfoType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ech.ch/xmlns/eCH-0010/3}organisationMailAddressInfoType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'organisationMailAddressInfoType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 37, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}organisationName uses Python identifier organisationName
    __organisationName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'organisationName'), 'organisationName', '__httpwww_ech_chxmlnseCH_00103_organisationMailAddressInfoType_httpwww_ech_chxmlnseCH_00103organisationName', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 39, 3), )

    
    organisationName = property(__organisationName.value, __organisationName.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}organisationNameAddOn1 uses Python identifier organisationNameAddOn1
    __organisationNameAddOn1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'organisationNameAddOn1'), 'organisationNameAddOn1', '__httpwww_ech_chxmlnseCH_00103_organisationMailAddressInfoType_httpwww_ech_chxmlnseCH_00103organisationNameAddOn1', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 40, 3), )

    
    organisationNameAddOn1 = property(__organisationNameAddOn1.value, __organisationNameAddOn1.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}organisationNameAddOn2 uses Python identifier organisationNameAddOn2
    __organisationNameAddOn2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'organisationNameAddOn2'), 'organisationNameAddOn2', '__httpwww_ech_chxmlnseCH_00103_organisationMailAddressInfoType_httpwww_ech_chxmlnseCH_00103organisationNameAddOn2', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 41, 3), )

    
    organisationNameAddOn2 = property(__organisationNameAddOn2.value, __organisationNameAddOn2.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}title uses Python identifier title
    __title = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'title'), 'title', '__httpwww_ech_chxmlnseCH_00103_organisationMailAddressInfoType_httpwww_ech_chxmlnseCH_00103title', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 42, 3), )

    
    title = property(__title.value, __title.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}firstName uses Python identifier firstName
    __firstName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'firstName'), 'firstName', '__httpwww_ech_chxmlnseCH_00103_organisationMailAddressInfoType_httpwww_ech_chxmlnseCH_00103firstName', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 43, 3), )

    
    firstName = property(__firstName.value, __firstName.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}lastName uses Python identifier lastName
    __lastName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'lastName'), 'lastName', '__httpwww_ech_chxmlnseCH_00103_organisationMailAddressInfoType_httpwww_ech_chxmlnseCH_00103lastName', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 44, 3), )

    
    lastName = property(__lastName.value, __lastName.set, None, None)


    _ElementMap = {
        __organisationName.name() : __organisationName,
        __organisationNameAddOn1.name() : __organisationNameAddOn1,
        __organisationNameAddOn2.name() : __organisationNameAddOn2,
        __title.name() : __title,
        __firstName.name() : __firstName,
        __lastName.name() : __lastName
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'organisationMailAddressInfoType', organisationMailAddressInfoType)


# Complex type {http://www.ech.ch/xmlns/eCH-0010/3}addressInformationType with content type ELEMENT_ONLY
class addressInformationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ech.ch/xmlns/eCH-0010/3}addressInformationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'addressInformationType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 47, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}addressLine1 uses Python identifier addressLine1
    __addressLine1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'addressLine1'), 'addressLine1', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103addressLine1', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 49, 3), )

    
    addressLine1 = property(__addressLine1.value, __addressLine1.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}addressLine2 uses Python identifier addressLine2
    __addressLine2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'addressLine2'), 'addressLine2', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103addressLine2', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 50, 3), )

    
    addressLine2 = property(__addressLine2.value, __addressLine2.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}street uses Python identifier street
    __street = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'street'), 'street', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103street', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 52, 4), )

    
    street = property(__street.value, __street.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}houseNumber uses Python identifier houseNumber
    __houseNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'houseNumber'), 'houseNumber', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103houseNumber', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 53, 4), )

    
    houseNumber = property(__houseNumber.value, __houseNumber.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}dwellingNumber uses Python identifier dwellingNumber
    __dwellingNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dwellingNumber'), 'dwellingNumber', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103dwellingNumber', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 54, 4), )

    
    dwellingNumber = property(__dwellingNumber.value, __dwellingNumber.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}postOfficeBoxNumber uses Python identifier postOfficeBoxNumber
    __postOfficeBoxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'postOfficeBoxNumber'), 'postOfficeBoxNumber', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103postOfficeBoxNumber', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 57, 4), )

    
    postOfficeBoxNumber = property(__postOfficeBoxNumber.value, __postOfficeBoxNumber.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}postOfficeBoxText uses Python identifier postOfficeBoxText
    __postOfficeBoxText = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'postOfficeBoxText'), 'postOfficeBoxText', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103postOfficeBoxText', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 58, 4), )

    
    postOfficeBoxText = property(__postOfficeBoxText.value, __postOfficeBoxText.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}locality uses Python identifier locality
    __locality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'locality'), 'locality', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103locality', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 60, 3), )

    
    locality = property(__locality.value, __locality.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}town uses Python identifier town
    __town = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'town'), 'town', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103town', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 61, 3), )

    
    town = property(__town.value, __town.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}swissZipCode uses Python identifier swissZipCode
    __swissZipCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'swissZipCode'), 'swissZipCode', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103swissZipCode', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 64, 5), )

    
    swissZipCode = property(__swissZipCode.value, __swissZipCode.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}swissZipCodeAddOn uses Python identifier swissZipCodeAddOn
    __swissZipCodeAddOn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeAddOn'), 'swissZipCodeAddOn', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103swissZipCodeAddOn', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 65, 5), )

    
    swissZipCodeAddOn = property(__swissZipCodeAddOn.value, __swissZipCodeAddOn.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}swissZipCodeId uses Python identifier swissZipCodeId
    __swissZipCodeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeId'), 'swissZipCodeId', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103swissZipCodeId', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 66, 5), )

    
    swissZipCodeId = property(__swissZipCodeId.value, __swissZipCodeId.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}foreignZipCode uses Python identifier foreignZipCode
    __foreignZipCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'foreignZipCode'), 'foreignZipCode', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103foreignZipCode', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 68, 4), )

    
    foreignZipCode = property(__foreignZipCode.value, __foreignZipCode.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'country'), 'country', '__httpwww_ech_chxmlnseCH_00103_addressInformationType_httpwww_ech_chxmlnseCH_00103country', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 70, 3), )

    
    country = property(__country.value, __country.set, None, None)


    _ElementMap = {
        __addressLine1.name() : __addressLine1,
        __addressLine2.name() : __addressLine2,
        __street.name() : __street,
        __houseNumber.name() : __houseNumber,
        __dwellingNumber.name() : __dwellingNumber,
        __postOfficeBoxNumber.name() : __postOfficeBoxNumber,
        __postOfficeBoxText.name() : __postOfficeBoxText,
        __locality.name() : __locality,
        __town.name() : __town,
        __swissZipCode.name() : __swissZipCode,
        __swissZipCodeAddOn.name() : __swissZipCodeAddOn,
        __swissZipCodeId.name() : __swissZipCodeId,
        __foreignZipCode.name() : __foreignZipCode,
        __country.name() : __country
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'addressInformationType', addressInformationType)


# Complex type {http://www.ech.ch/xmlns/eCH-0010/3}swissAddressInformationType with content type ELEMENT_ONLY
class swissAddressInformationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.ech.ch/xmlns/eCH-0010/3}swissAddressInformationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'swissAddressInformationType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 73, 1)
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}addressLine1 uses Python identifier addressLine1
    __addressLine1 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'addressLine1'), 'addressLine1', '__httpwww_ech_chxmlnseCH_00103_swissAddressInformationType_httpwww_ech_chxmlnseCH_00103addressLine1', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 75, 3), )

    
    addressLine1 = property(__addressLine1.value, __addressLine1.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}addressLine2 uses Python identifier addressLine2
    __addressLine2 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'addressLine2'), 'addressLine2', '__httpwww_ech_chxmlnseCH_00103_swissAddressInformationType_httpwww_ech_chxmlnseCH_00103addressLine2', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 76, 3), )

    
    addressLine2 = property(__addressLine2.value, __addressLine2.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}street uses Python identifier street
    __street = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'street'), 'street', '__httpwww_ech_chxmlnseCH_00103_swissAddressInformationType_httpwww_ech_chxmlnseCH_00103street', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 78, 4), )

    
    street = property(__street.value, __street.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}houseNumber uses Python identifier houseNumber
    __houseNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'houseNumber'), 'houseNumber', '__httpwww_ech_chxmlnseCH_00103_swissAddressInformationType_httpwww_ech_chxmlnseCH_00103houseNumber', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 79, 4), )

    
    houseNumber = property(__houseNumber.value, __houseNumber.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}dwellingNumber uses Python identifier dwellingNumber
    __dwellingNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'dwellingNumber'), 'dwellingNumber', '__httpwww_ech_chxmlnseCH_00103_swissAddressInformationType_httpwww_ech_chxmlnseCH_00103dwellingNumber', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 80, 4), )

    
    dwellingNumber = property(__dwellingNumber.value, __dwellingNumber.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}locality uses Python identifier locality
    __locality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'locality'), 'locality', '__httpwww_ech_chxmlnseCH_00103_swissAddressInformationType_httpwww_ech_chxmlnseCH_00103locality', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 82, 3), )

    
    locality = property(__locality.value, __locality.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}town uses Python identifier town
    __town = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'town'), 'town', '__httpwww_ech_chxmlnseCH_00103_swissAddressInformationType_httpwww_ech_chxmlnseCH_00103town', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 83, 3), )

    
    town = property(__town.value, __town.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}swissZipCode uses Python identifier swissZipCode
    __swissZipCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'swissZipCode'), 'swissZipCode', '__httpwww_ech_chxmlnseCH_00103_swissAddressInformationType_httpwww_ech_chxmlnseCH_00103swissZipCode', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 85, 4), )

    
    swissZipCode = property(__swissZipCode.value, __swissZipCode.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}swissZipCodeAddOn uses Python identifier swissZipCodeAddOn
    __swissZipCodeAddOn = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeAddOn'), 'swissZipCodeAddOn', '__httpwww_ech_chxmlnseCH_00103_swissAddressInformationType_httpwww_ech_chxmlnseCH_00103swissZipCodeAddOn', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 86, 4), )

    
    swissZipCodeAddOn = property(__swissZipCodeAddOn.value, __swissZipCodeAddOn.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}swissZipCodeId uses Python identifier swissZipCodeId
    __swissZipCodeId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeId'), 'swissZipCodeId', '__httpwww_ech_chxmlnseCH_00103_swissAddressInformationType_httpwww_ech_chxmlnseCH_00103swissZipCodeId', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 87, 4), )

    
    swissZipCodeId = property(__swissZipCodeId.value, __swissZipCodeId.set, None, None)

    
    # Element {http://www.ech.ch/xmlns/eCH-0010/3}country uses Python identifier country
    __country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'country'), 'country', '__httpwww_ech_chxmlnseCH_00103_swissAddressInformationType_httpwww_ech_chxmlnseCH_00103country', False, pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 89, 3), )

    
    country = property(__country.value, __country.set, None, None)


    _ElementMap = {
        __addressLine1.name() : __addressLine1,
        __addressLine2.name() : __addressLine2,
        __street.name() : __street,
        __houseNumber.name() : __houseNumber,
        __dwellingNumber.name() : __dwellingNumber,
        __locality.name() : __locality,
        __town.name() : __town,
        __swissZipCode.name() : __swissZipCode,
        __swissZipCodeAddOn.name() : __swissZipCodeAddOn,
        __swissZipCodeId.name() : __swissZipCodeId,
        __country.name() : __country
    }
    _AttributeMap = {
        
    }
Namespace.addCategoryObject('typeBinding', u'swissAddressInformationType', swissAddressInformationType)


personMailAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'personMailAddress'), personMailAddressType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 189, 1))
Namespace.addCategoryObject('elementBinding', personMailAddress.name().localName(), personMailAddress)

organisationMailAdress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'organisationMailAdress'), organisationMailAddressType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 190, 1))
Namespace.addCategoryObject('elementBinding', organisationMailAdress.name().localName(), organisationMailAdress)

mailAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mailAddress'), mailAddressType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 191, 1))
Namespace.addCategoryObject('elementBinding', mailAddress.name().localName(), mailAddress)



mailAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'organisation'), organisationMailAddressInfoType, scope=mailAddressType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 11, 4)))

mailAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'person'), personMailAddressInfoType, scope=mailAddressType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 12, 4)))

mailAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressInformation'), addressInformationType, scope=mailAddressType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 14, 3)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mailAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'organisation')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 11, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(mailAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'person')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 12, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(mailAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressInformation')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 14, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
mailAddressType._Automaton = _BuildAutomaton()




personMailAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'person'), personMailAddressInfoType, scope=personMailAddressType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 19, 3)))

personMailAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressInformation'), addressInformationType, scope=personMailAddressType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 20, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personMailAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'person')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 19, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(personMailAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressInformation')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 20, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
personMailAddressType._Automaton = _BuildAutomaton_()




personMailAddressInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'mrMrs'), mrMrsType, scope=personMailAddressInfoType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 25, 3)))

personMailAddressInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), titleType, scope=personMailAddressInfoType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 26, 3)))

personMailAddressInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstName'), firstNameType, scope=personMailAddressInfoType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 27, 3)))

personMailAddressInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lastName'), lastNameType, scope=personMailAddressInfoType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 28, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 25, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 26, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 27, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personMailAddressInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'mrMrs')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 25, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personMailAddressInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 26, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(personMailAddressInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'firstName')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 27, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(personMailAddressInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lastName')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 28, 3))
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
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
personMailAddressInfoType._Automaton = _BuildAutomaton_2()




organisationMailAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'organisation'), organisationMailAddressInfoType, scope=organisationMailAddressType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 33, 3)))

organisationMailAddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressInformation'), addressInformationType, scope=organisationMailAddressType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 34, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(organisationMailAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'organisation')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 33, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(organisationMailAddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressInformation')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 34, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
organisationMailAddressType._Automaton = _BuildAutomaton_3()




organisationMailAddressInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'organisationName'), organisationNameType, scope=organisationMailAddressInfoType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 39, 3)))

organisationMailAddressInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'organisationNameAddOn1'), organisationNameType, scope=organisationMailAddressInfoType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 40, 3)))

organisationMailAddressInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'organisationNameAddOn2'), organisationNameType, scope=organisationMailAddressInfoType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 41, 3)))

organisationMailAddressInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'title'), titleType, scope=organisationMailAddressInfoType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 42, 3)))

organisationMailAddressInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'firstName'), firstNameType, scope=organisationMailAddressInfoType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 43, 3)))

organisationMailAddressInfoType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'lastName'), lastNameType, scope=organisationMailAddressInfoType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 44, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 40, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 41, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 42, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 43, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 44, 3))
    counters.add(cc_4)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(organisationMailAddressInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'organisationName')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 39, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(organisationMailAddressInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'organisationNameAddOn1')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 40, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(organisationMailAddressInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'organisationNameAddOn2')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 41, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(organisationMailAddressInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'title')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 42, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(organisationMailAddressInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'firstName')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 43, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(organisationMailAddressInfoType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'lastName')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 44, 3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
organisationMailAddressInfoType._Automaton = _BuildAutomaton_4()




addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressLine1'), addressLineType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 49, 3)))

addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressLine2'), addressLineType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 50, 3)))

addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'street'), streetType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 52, 4)))

addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'houseNumber'), houseNumberType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 53, 4)))

addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dwellingNumber'), dwellingNumberType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 54, 4)))

addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postOfficeBoxNumber'), postOfficeBoxNumberType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 57, 4)))

addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'postOfficeBoxText'), postOfficeBoxTextType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 58, 4)))

addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'locality'), localityType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 60, 3)))

addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'town'), townType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 61, 3)))

addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'swissZipCode'), swissZipCodeType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 64, 5)))

addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeAddOn'), swissZipCodeAddOnType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 65, 5)))

addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeId'), swissZipCodeIdType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 66, 5)))

addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'foreignZipCode'), foreignZipCodeType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 68, 4)))

addressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'country'), countryType, scope=addressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 70, 3)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 49, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 50, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 51, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 53, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 54, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 56, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 57, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 60, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 65, 5))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 66, 5))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 68, 4))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressLine1')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 49, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressLine2')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 50, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'street')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 52, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'houseNumber')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 53, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dwellingNumber')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 54, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postOfficeBoxNumber')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 57, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'postOfficeBoxText')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 58, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'locality')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 60, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'town')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 61, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'swissZipCode')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 64, 5))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeAddOn')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 65, 5))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeId')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 66, 5))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'foreignZipCode')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 68, 4))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(addressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'country')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 70, 3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    transitions.append(fac.Transition(st_11, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
addressInformationType._Automaton = _BuildAutomaton_5()




swissAddressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressLine1'), addressLineType, scope=swissAddressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 75, 3)))

swissAddressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'addressLine2'), addressLineType, scope=swissAddressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 76, 3)))

swissAddressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'street'), streetType, scope=swissAddressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 78, 4)))

swissAddressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'houseNumber'), houseNumberType, scope=swissAddressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 79, 4)))

swissAddressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'dwellingNumber'), dwellingNumberType, scope=swissAddressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 80, 4)))

swissAddressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'locality'), localityType, scope=swissAddressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 82, 3)))

swissAddressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'town'), townType, scope=swissAddressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 83, 3)))

swissAddressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'swissZipCode'), swissZipCodeType, scope=swissAddressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 85, 4)))

swissAddressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeAddOn'), swissZipCodeAddOnType, scope=swissAddressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 86, 4)))

swissAddressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeId'), swissZipCodeIdType, scope=swissAddressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 87, 4)))

swissAddressInformationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'country'), STD_ANON, scope=swissAddressInformationType, location=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 89, 3)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it's invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 75, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 76, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 77, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 79, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 80, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 82, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 86, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 87, 4))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(swissAddressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressLine1')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 75, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(swissAddressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'addressLine2')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 76, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(swissAddressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'street')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 78, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(swissAddressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'houseNumber')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 79, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(swissAddressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'dwellingNumber')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 80, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(swissAddressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'locality')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 82, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(swissAddressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'town')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 83, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(swissAddressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'swissZipCode')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 85, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(swissAddressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeAddOn')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 86, 4))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(swissAddressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'swissZipCodeId')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 87, 4))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(swissAddressInformationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'country')), pyxb.utils.utility.Location(u'http://www.ech.ch/xmlns/eCH-0010/3/eCH-0010-3-1.xsd', 89, 3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    transitions.append(fac.Transition(st_10, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
swissAddressInformationType._Automaton = _BuildAutomaton_6()

