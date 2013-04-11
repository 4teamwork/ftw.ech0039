from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
from zope.configuration import xmlconfig
import ftw.ech0039


class Ech0039Layer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        xmlconfig.file('configure.zcml', ftw.ech0039,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        setRoles(portal, TEST_USER_ID, ['Manager'])


ECH0039_FIXTURE = Ech0039Layer()
ECH0039_FUNCTIONAL_FIXTURE = FunctionalTesting(
    bases=(ECH0039_FIXTURE, ), name="eCH-0039-Integration")
