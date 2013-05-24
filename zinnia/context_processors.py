"""Context Processors for Zinnia"""
from zinnia import __version__
from zinnia import settings


def version(request):
    """
    Add version of Zinnia to the context.
    """
    return {
        'ZINNIA_VERSION': __version__,
        'ZINNIA_TITLE': settings.TITLE,
    }
