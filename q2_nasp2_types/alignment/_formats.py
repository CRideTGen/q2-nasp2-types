from qiime2.plugin import model

from ..plugin_setup import plugin


class SAMFileFormat(model.TextFileFormat):
    def _validate_(self, level):
        pass


class SAMFileDirFmt(model.DirectoryFormat):
    sam_files = model.FileCollection(
        r'.*\.sam',
        format=SAMFileFormat)

    @sam_files.set_path_maker
    def sequences_path_maker(self, sample_id, ):
        return '%s.sam' % (sample_id)


class BAMFileFormat(model.TextFileFormat):
    def _validate_(self, level):
        pass


class BAMFileDirFmt(model.DirectoryFormat):
    sam_files = model.FileCollection(r'*.sam', format=BAMFileFormat)

    def _validate_(self, level):
        pass


plugin.register_formats(SAMFileFormat, SAMFileDirFmt, BAMFileFormat, BAMFileDirFmt)
