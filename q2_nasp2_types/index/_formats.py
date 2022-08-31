from qiime2.plugin import model
from q2_nasp2_types.plugin_setup import plugin


class BWAIndexFileFormat(model.BinaryFileFormat):
    def _validate_(self, level):
        pass


class BWAIndexDirFmt(model.DirectoryFormat):
    amb = model.File(r'.*\.amb', format=BWAIndexFileFormat)
    ann = model.File(r'.*\.ann', format=BWAIndexFileFormat)
    bwt = model.File(r'..*\.bwt', format=BWAIndexFileFormat)
    pac = model.File(r'.*\.pac', format=BWAIndexFileFormat)
    sa = model.File(r'.*\.sa', format=BWAIndexFileFormat)

    def return_reference_index(self):
        return


plugin.register_formats(BWAIndexFileFormat, BWAIndexDirFmt)
