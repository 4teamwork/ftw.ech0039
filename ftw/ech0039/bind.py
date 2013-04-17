from ftw.ech0039.bindings import eCH0039
from ftw.ech0039.bindings import eCH0058
from ftw.ech0039.bindings import eCH0147T0
from ftw.ech0039.bindings import eCH0147T1
from pprint import pformat
from pyxb import BIND as PYXB_BIND
from pyxb.utils.domutils import BindingDOMSupport
from pyxb.utils.domutils import SetDOMImplementation
import xml.dom.minidom


# SetDOMImplementation is necessary to make 100% sure that pyxb finds a
# working DOM implementation.
# Pyxb does not provide a DOM-implementation name or a list of required
# DOM-implementation features. Thus it just uses an arbitrary implementation
# that might not provide all the required features.
SetDOMImplementation(xml.dom.minidom.DOMImplementation())

# Namespace prefixes
BindingDOMSupport.DeclareNamespace(eCH0147T1.Namespace, 'eCH-0147T1')
BindingDOMSupport.DeclareNamespace(eCH0147T0.Namespace, 'eCH-0147T0')
BindingDOMSupport.DeclareNamespace(eCH0039.Namespace, 'eCH-0039')
BindingDOMSupport.DeclareNamespace(eCH0058.Namespace, 'eCH-0058')


class BIND(PYXB_BIND):
    """Add (limited) rich comparison support to BIND.
    """

    def __eq__(self, other):
        if isinstance(other, BIND):
            return self._args == other._args and \
               self._kwargs == other._kwargs
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    @property
    def _kwargs(self):
        return self._BIND__kw

    @property
    def _args(self):
        return self._BIND__args

    def __repr__(self):
        result = "BIND<< "
        if self._BIND__args:
            result += pformat(self._BIND__args)
        if self._BIND__kw:
            result += pformat(self._BIND__kw)
        result += " >>"
        return result
