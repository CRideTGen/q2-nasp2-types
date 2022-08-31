from qiime2.plugin import SemanticType

from ._formats import VCFFileDirFmt, NASP2MatrixFileDirFmt
from ..plugin_setup import plugin

# Semantic Types
SNPFile = SemanticType('SNPFile', field_names='type')
VCFFile = SemanticType('VCFFile', variant_of=[SNPFile.field['type']])
NASP2MatrixFile = SemanticType('NASPMatrixFile', variant_of=[SNPFile.field['type']])

# Registering Types
plugin.register_semantic_types(SNPFile, NASP2MatrixFile, VCFFile)
plugin.register_semantic_type_to_format(SNPFile[NASP2MatrixFile], artifact_format=NASP2MatrixFileDirFmt)
plugin.register_semantic_type_to_format(SNPFile[VCFFile], artifact_format=VCFFileDirFmt)
