from setuptools import setup, find_packages
import versioneer

setup(
    name='q2-nasp2-types',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    url='github.com/CRideTGen/q2-nasp2-types',
    license='Apache-2.0',
    author='Chase Ridenour',
    author_email='cridenour@tgen.org',
    description='',
    entry_points={
        'qiime2.plugins': ['q2-nasp2-types=q2_nasp2_types.plugin_setup:plugin']
    },
    zip_safe=False,
)
