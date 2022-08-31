from qiime2.plugin import SemanticType

from ._formats import BWAIndexDirFmt
from ..plugin_setup import plugin

# Semantic Types
BWAIndex = SemanticType('BWAIndex')

# Registering Types

plugin.register_semantic_types(BWAIndex)
plugin.register_semantic_type_to_format(BWAIndex, artifact_format=BWAIndexDirFmt)
