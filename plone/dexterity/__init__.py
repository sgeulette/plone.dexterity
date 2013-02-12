# Kick dynamic module factory
import schema

"""Dynamic SearchableText index for dexterity content types
"""
import zope.deferredimport

zope.deferredimport.defineFrom(
    'plone.dexterity.interfaces',
    'IDynamicTextIndexExtender', 'IDexterityTextIndexFieldConverter')

