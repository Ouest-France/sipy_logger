#!/usr/bin/env python

import setuptools

with open('README.md', 'r') as fh:
    longDescription = fh.read()

setuptools.setup(name='sipy_logger',
    version='0.1.1',
    description='Programmatically creates python loggers with different handlers (console, file, graylog)',
    long_description=longDescription,
    long_description_content_type="text/markdown",
    author='Ouest-France/SIPA Tech',
    url='https://github.com/Ouest-France/sipy_logger',
    packages=setuptools.find_packages(),
    install_requires=[
        'graypy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)