import os
from setuptools import setup


def version():

    setup_dir = os.path.dirname(os.path.realpath(__file__))
    version_file = open(os.path.join(setup_dir, 'detectCFP', 'VERSION'))

    return version_file.readline().strip()


__long_description__ = '''

detectCFP: Detect carbon fixation pathways
Weizhi Song (songwz03@gmail.com)
Center for Marine Science & Innovation (CMSI)
University of New South Wales, Sydney, Australia

'''

setup(name="detectCFP",
      version=version(),
      long_description=__long_description__,
      license="GPL3+",
      author="Weizhi Song",
      author_email="songwz03@gmail.com",
      keywords="Bioinformatics CarbonFixationPathway",
      description="Detect carbon fixation pathways",
      url="https://github.com/songweizhi/detectCFP",
      packages=['detectCFP'],
      package_data={'': ['*.r', '*.R', '*.py', 'VERSION']},
      include_package_data=True,
      install_requires=['biopython', 'pandas'],
      scripts=['bin/detectCFP'])
