from qiime2.plugin import model

from ..plugin_setup import plugin


class YAMLFileFormat(model.TextFileFormat):
    def _validate_(self, level):
        pass


class YAMLFileDirFmt(model.DirectoryFormat):
    config_file = model.File(r'*.yaml', format=YAMLFileFormat)


class XMLFileFormat(model.TextFileFormat):
    def _validate_(self, level):
        pass


class XMLFileDirFmt(model.DirectoryFormat):
    config_file = model.File(r'*.xml', format=XMLFileFormat)


plugin.register_formats(YAMLFileFormat, YAMLFileDirFmt, XMLFileFormat, XMLFileDirFmt)
