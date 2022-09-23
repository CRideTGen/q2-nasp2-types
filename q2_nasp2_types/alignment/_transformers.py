import subprocess

from q2_nasp2_types.alignment import SAMFileDirFmt, BAMFileDirFmt
import pysam

from ..plugin_setup import plugin
from pathlib import Path


@plugin.register_transformer
def _0(data: SAMFileDirFmt) -> BAMFileDirFmt:
    bam_output = BAMFileDirFmt()

    sam_files = data.path.glob("*.sam")
    for sam in sam_files:
        bam_output_path = Path(bam_output.path).joinpath(sam.name.replace('sam', 'bam'))

        with open(bam_output_path, "wb", 0) as b_file:
            build_cmd = ['samtools', 'view', '-bS', f'{sam}']
            process = subprocess.run(build_cmd, check=True, stdout=subprocess.PIPE,
                                     stdin=None,
                                     cwd=None)
            output = process.stdout
            b_file.write(output)

    return bam_output


@plugin.register_transformer
def _1(data: BAMFileDirFmt) -> SAMFileDirFmt:
    bam_output = BAMFileDirFmt()

    sam_files = data.path.glob("*.bam")
    for sam in sam_files:
        bam_output_path = Path(bam_output.path).joinpath(sam.name.replace('bam', 'sam'))

        with open(bam_output_path, "wb", 0) as b_file:
            build_cmd = ['samtools', 'view', '-h', f'{sam}']
            process = subprocess.run(build_cmd, check=True, stdout=subprocess.PIPE,
                                     stdin=None,
                                     cwd=None)
            output = process.stdout
            b_file.write(output)

    return bam_output
