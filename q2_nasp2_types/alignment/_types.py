from q2_types.feature_data import FeatureData
from qiime2.plugin import SemanticType

from ._formats import SAMFileDirFmt, BAMFileDirFmt
from ..plugin_setup import plugin

# Semantic Types

AlignedReads = SemanticType('AlignedReads', variant_of=[FeatureData.field['type']])

# Registering Types

plugin.register_semantic_types(AlignedReads)
plugin.register_semantic_type_to_format(FeatureData[AlignedReads], artifact_format=SAMFileDirFmt)
plugin.register_semantic_type_to_format(FeatureData[AlignedReads], artifact_format=BAMFileDirFmt)
