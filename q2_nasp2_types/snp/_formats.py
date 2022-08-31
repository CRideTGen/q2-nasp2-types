from qiime2.plugin import model

from q2_nasp2_types.plugin_setup import plugin


class VCFFileFormat(model.TextFileFormat):
    def _validate_(self, level):
        pass


class VCFFileDirFmt(model.DirectoryFormat):
    sam_files = model.FileCollection(r'*.sam', format=VCFFileFormat)


class NASP2MatrixFileFormat(model.TextFileFormat):
    def _validate_(self, level):
        pass


class NASP2MatrixFileDirFmt(model.DirectoryFormat):
    sam_files = model.FileCollection(r'*.sam', format=NASP2MatrixFileFormat)


plugin.register_formats(VCFFileFormat, VCFFileDirFmt, NASP2MatrixFileFormat, NASP2MatrixFileDirFmt)
