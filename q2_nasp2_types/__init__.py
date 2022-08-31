import importlib

from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

importlib.import_module('q2_nasp2_types.index')
importlib.import_module('q2_nasp2_types.alignment')
importlib.import_module('q2_nasp2_types.snp')
importlib.import_module('q2_nasp2_types.config')
