# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from mingtak.backToBackend.testing import MINGTAK_BACKTOBACKEND_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that mingtak.backToBackend is properly installed."""

    layer = MINGTAK_BACKTOBACKEND_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if mingtak.backToBackend is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'mingtak.backToBackend'))

    def test_browserlayer(self):
        """Test that IMingtakBacktobackendLayer is registered."""
        from mingtak.backToBackend.interfaces import (
            IMingtakBacktobackendLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IMingtakBacktobackendLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = MINGTAK_BACKTOBACKEND_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['mingtak.backToBackend'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if mingtak.backToBackend is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'mingtak.backToBackend'))

    def test_browserlayer_removed(self):
        """Test that IMingtakBacktobackendLayer is removed."""
        from mingtak.backToBackend.interfaces import \
            IMingtakBacktobackendLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IMingtakBacktobackendLayer,
            utils.registered_layers())
