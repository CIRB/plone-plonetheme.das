from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope browser layer.
    """
class IMenuBreathcrumb(IViewletManager):
    """ A viewlet manger that sits at the very top of the rendered page content
    """

class IThemeView(Interface):
    """ """

    def getColumnsClass():
        """ Returns the CSS class based on columns presence. """
