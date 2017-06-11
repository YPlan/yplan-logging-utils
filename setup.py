# -*- coding: utf-8 -*-
import codecs
import os
import re

from setuptools import find_packages, setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    with codecs.open(os.path.join(package, '__init__.py'), 'r', 'utf-8') as fp:
        init_py = fp.read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('yplan_logging_utils')

with codecs.open('README.rst', 'r', 'utf-8') as readme_file:
    readme = readme_file.read()

with codecs.open('HISTORY.rst', 'r', 'utf-8') as history_file:
    history = history_file.read()


setup(
    name='yplan-logging-utils',
    version=version,
    description="Utilities we use for logging.",
    long_description=readme + '\n\n' + history,
    author="YPlan",
    author_email='adam@yplanapp.com',
    url='https://github.com/YPlan/yplan-logging-utils',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    license="ISCL",
    zip_safe=False,
    install_requires=[
        'six>=1.5.0',
    ],
    keywords='Logging, YPlan',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',
        'Topic :: System :: Logging',
    ],
)
