
import importlib

from ._version import get_versions


__version__ = get_versions()['version']
del get_versions

importlib.import_module('q2_types.all')
