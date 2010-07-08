"""Event definitions
"""

from zope.interface import implements

from zope.component.interfaces import ObjectEvent

from plone.dexterity.interfaces import IAddBegunEvent
from plone.dexterity.interfaces import IEditBegunEvent


class AddBegunEvent(ObjectEvent):
    """An add operation was begun
    """
    implements(IAddBegunEvent)
    
class EditBegunEvent(ObjectEvent):
    """An edit operation was begun
    """
    implements(IEditBegunEvent)
    