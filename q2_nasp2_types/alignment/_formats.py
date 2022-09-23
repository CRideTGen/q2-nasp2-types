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
    def sequences_path_maker(self, sample_id ):
        return f'{sample_id}.sam'


class BAMFileFormat(model.TextFileFormat):
    def _validate_(self, level):
        pass


class BAMFileDirFmt(model.DirectoryFormat):
    bam_files = model.FileCollection(r'.*\.bam', format=BAMFileFormat)

    def _validate_(self, level):
        pass

    @bam_files.set_path_maker
    def sequences_path_maker(self, sample_id ):
        return f'{sample_id}.bam'

plugin.register_formats(SAMFileFormat, SAMFileDirFmt, BAMFileFormat, BAMFileDirFmt)
