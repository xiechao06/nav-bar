from distutils.core import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
import sys
import os.path

PACKAGE = "nav_bar"
NAME = "nav-bar"
DESCRIPTION = ""
AUTHOR = ""
AUTHOR_EMAIL = ""
URL = ""
VERSION = __import__(PACKAGE).__version__
DOC = __import__(PACKAGE).__doc__


setup(
    name=NAME,
    version=VERSION,
    long_description=__doc__,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=open("requirements.txt").readlines(),
)

