#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

from whachuptu import __version__

setup(
    name='whachuptu',
    version=__version__,
    author='Shane R. Spencer',
    author_email='shane@bogomip.com',
    packages=['whachuptu'],
    url='https://github.com/whardier/whachuptu',
    license='MIT',
    description='Active Work/Project Logger',
    long_description=open('README.md').read(),
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 1 - Planning',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ],
    entry_points={
        'console_scripts': [
            'whachuptu = whachuptu.__main__:main',
        ],
    }

)


