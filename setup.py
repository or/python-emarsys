#!/usr/bin/env python
from setuptools import setup, find_packages

CLASSIFIERS = ["Development Status :: 2 - Pre-Alpha",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: Apache Software License",
               "Natural Language :: English",
               "Operating System :: OS Independent",
               "Programming Language :: Python",
               "Topic :: Software Development :: Libraries :: Python Modules"]

KEYWORDS = "emarsys api wrapper"

REPO_URL = "https://github.com/eugene-wee/python-emarsys"

setup(name="python-emarsys",
      version='0.1',
      description="""Emarsys REST API wrapper for Python.""",
      author='Eugene Wee',
      url=REPO_URL,
      packages=find_packages(),
      download_url=REPO_URL + "/tarball/master",
      classifiers=CLASSIFIERS,
      keywords=KEYWORDS,
      zip_safe=True,
      install_requires=["distribute", "requests"])
