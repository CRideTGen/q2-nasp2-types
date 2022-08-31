from qiime2.plugin import SemanticType

from ._formats import YAMLFileDirFmt, XMLFileDirFmt
from ..plugin_setup import plugin

# Semantic Types
Config = SemanticType('Config', field_names='type')
YAMLFile = SemanticType('YAMLFile', variant_of=[Config.field['type']])
XMLFile = SemanticType('XMLFile', variant_of=[Config.field['type']])

# Registering Types

plugin.register_semantic_types(Config, YAMLFile, XMLFile)

plugin.register_semantic_type_to_format(Config[XMLFile], artifact_format=XMLFileDirFmt)
plugin.register_semantic_type_to_format(Config[YAMLFile], artifact_format=YAMLFileDirFmt)
