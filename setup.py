#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='pyacdc',
    version='1.0',
    author='Raphaël Vinot',
    author_email='raphael.vinot@circl.lu',
    maintainer='Raphaël Vinot',
    url='https://github.com/CIRCL/PyACDC',
    description='Python API for ACDC.',
    long_description=open('README.md').read(),
    packages=['pyacdc'],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Telecommunications Industry',
        'Programming Language :: Python',
        'Topic :: Security',
        'Topic :: Internet',
    ],
    install_requires=['requests'],
)
