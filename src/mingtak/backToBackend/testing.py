# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import mingtak.backToBackend


class MingtakBacktobackendLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=mingtak.backToBackend)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'mingtak.backToBackend:default')


MINGTAK_BACKTOBACKEND_FIXTURE = MingtakBacktobackendLayer()


MINGTAK_BACKTOBACKEND_INTEGRATION_TESTING = IntegrationTesting(
    bases=(MINGTAK_BACKTOBACKEND_FIXTURE,),
    name='MingtakBacktobackendLayer:IntegrationTesting',
)


MINGTAK_BACKTOBACKEND_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(MINGTAK_BACKTOBACKEND_FIXTURE,),
    name='MingtakBacktobackendLayer:FunctionalTesting',
)


MINGTAK_BACKTOBACKEND_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        MINGTAK_BACKTOBACKEND_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='MingtakBacktobackendLayer:AcceptanceTesting',
)
