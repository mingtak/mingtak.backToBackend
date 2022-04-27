# -*- coding: utf-8 -*-
from plone import api
from mingtak.backToBackend import _
from zope.globalrequest import getRequest

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import transaction_note


def toFolderContents(obj, event):
    """
    Return to Folder Contents
    """
    request = getRequest()

    portal_type = getattr(obj, 'portal_type', None)

    if portal_type == 'Plone Site' and request:
        request.response.redirect('%s/folder_contents' % obj.absolute_url())
        return

    try:
        folder = obj.getParentNode()
    except:
        return
    if folder == None:
        try:
            folder = api.portal.get()
        except:
            return
    elif getattr(obj, 'portal_type', None) == 'Plone Site':
        folder = obj

    if request:
        request.response.redirect('%s/folder_contents' % folder.absolute_url())


def back_to_cover(event):
    request = getRequest()
    portal = api.portal.get()
    request.response.redirect(portal.absolute_url())
