#!/usr/bin/python

from setuptools import setup, find_packages
from codecs import open

with open('README.md', 'r', 'utf-8') as fd:
    long_description = fd.read()

setup(
    name='nchoice',
    version='0.1.0',
    description='Prompt user for making a choice using ncurses',
    long_description=long_description,
    url='https://github.com/fg1/nchoice',
    author='fg1',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
    ],
    keywords='curses',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'nchoice=nchoice:main',
        ],
    }, )
