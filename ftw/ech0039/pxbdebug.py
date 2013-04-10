from pyxb import BIND
from pprint import pformat


def monkey_patch_pxb():
    """Monkey-patch pyxb.BIND for debugging purposes.
    """

    def debug_repr(self):
        """Better readable __repr__ that contains the original parameters
        of the bind __init__ call.

        """

        result = "BIND<< "
        if self._BIND__args:
            result += pformat(self._BIND__args)
        if self._BIND__kw:
            result += pformat(self._BIND__kw)
        result += " >>"
        return result
    BIND.__repr__ = debug_repr

    def debug_eq(self, other):
        """Comparison that drops into debug shell when an AttributeError is
        raised during comparison.

        """

        try:
            return self._BIND__args == other._BIND__args and \
               self._BIND__kw == other._BIND__kw
        except AttributeError:
            import pdb; pdb.set_trace()

    BIND.__eq__ = debug_eq

