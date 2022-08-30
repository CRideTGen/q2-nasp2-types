from q2_types.feature_data import FeatureData
from qiime2.plugin import SemanticType

from q2_nasp2_types import BWAIndexDirFmt, SAMFileDirFmt, BAMFileDirFmt, VCFFileDirFmt, NASP2MatrixFileDirFmt, \
    YAMLFileDirFmt, XMLFileDirFmt
from q2_nasp2_types.plugin_setup import plugin

# Semantic Types
BWAIndex = SemanticType('BWAIndex')
plugin.register_semantic_types(BWAIndex)

AlignedReads = SemanticType('AlignedReads', variant_of=[FeatureData.field['type']])

SNPFile = SemanticType('SNPFile', field_names='type')
VCFFile = SemanticType('VCFFile', variant_of=[SNPFile.field['type']])
NASP2MatrixFile = SemanticType('NASPMatrixFile', variant_of=[SNPFile.field['type']])

Config = SemanticType('Config', field_names='type')
YAMLFile = SemanticType('YAMLFile', variant_of=[Config.field['type']])
XMLFile = SemanticType('XMLFile', variant_of=[Config.field['type']])

# Registering Types

plugin.register_semantic_types(AlignedReads, BWAIndex,SNPFile, NASP2MatrixFile, VCFFile)
plugin.register_semantic_type_to_format(BWAIndex, artifact_format=BWAIndexDirFmt)
plugin.register_semantic_type_to_format(FeatureData[AlignedReads], artifact_format=SAMFileDirFmt)
plugin.register_semantic_type_to_format(FeatureData[AlignedReads], artifact_format=BAMFileDirFmt)

plugin.register_semantic_types()
plugin.register_semantic_type_to_format(SNPFile[NASP2MatrixFile], artifact_format=NASP2MatrixFileDirFmt)
plugin.register_semantic_type_to_format(SNPFile[VCFFile], artifact_format=VCFFileDirFmt)

plugin.register_semantic_types(Config, YAMLFile, XMLFile)

plugin.register_semantic_type_to_format(Config[XMLFile], artifact_format=XMLFileDirFmt)
plugin.register_semantic_type_to_format(Config[YAMLFile], artifact_format=YAMLFileDirFmt)
