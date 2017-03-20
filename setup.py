import codecs
import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()



NAME = "xueshanlinghu"

PACKAGES = ["xueshanlinghu"]

DESCRIPTION = "this is a package created by xueshanlinghu tutor. Now including math class."

LONG_DESCRIPTION = read("README.rst")

KEYWORDS = "xueshanlinghu python package math"

AUTHOR = "xueshanlinghu"

AUTHOR_EMAIL = "xueshanlinghu@xueshanlinghu.com"

URL = "https://github.com/xueshanlinghu/xueshanlinghu-package.git"

VERSION = "1.2.3"

LICENSE = "MIT"

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = PACKAGES,
    include_package_data=True,
    zip_safe=True,
)
