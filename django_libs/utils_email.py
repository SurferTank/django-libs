"""Kept for backwards compatibility. Please add everything to the path below."""
import warnings
from .utils.email import *  # NOQA

warnings.warn('Please import from django_libs.utils.email instead.',
              DeprecationWarning)
