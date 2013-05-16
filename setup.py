from distutils.core import setup
from setuptools import find_packages

PACKAGE = "nav_bar"
NAME = "nav-bar"
DESCRIPTION = ""
AUTHOR = "xiechao"
AUTHOR_EMAIL = "xiechao06@gmail.com"
VERSION = "0.9.0"
URL = ""
DOC = """
doc
"""


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

