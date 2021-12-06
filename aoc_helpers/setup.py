from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='aoc_helpers',
    version='0.1',
    description='Package to support Advent of Code',
    long_description=long_description,
    long_description_content_type='text/markdown',
    # Author
    author='Kevin Metherell',
    author_email='kevindickens@gmail.com',

    packages=find_packages(),
    install_requires=[
        # 'pandas',
        # 'numpy',
        # 'datetime',
        # 'networkx',
        'requests',
        'bs4',
        # 'urllib3',
        # 'fake-useragent'
    ],
    zip_safe=False)
