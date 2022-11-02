#!/usr/bin/env python3

from setuptools import setup

VERSION = '0.1'

packages = ['quickplot']
requires = ['pandas>=1.4.4', 'numpy>=1.22.4', 'seaborn>=0.12.0',
    'matplotlib>=3.5.3',]

with open('README.md', mode='r') as f:
    readme = f.read()

setup(
    name="quickplot", 
    version=VERSION,
    description='TBD',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/coindataschool/quickplot',
    author="Coin Data School",
    author_email="<coindataschool@gmail.com>",
    packages=packages,
    install_requires=requires, # dependencies    
    keywords=['python 3', 'data vis', 'statistical charts', 'seaborn', 
        'matplotlib'],
    classifiers= [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)