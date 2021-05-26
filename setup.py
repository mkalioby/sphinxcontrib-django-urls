#!/usr/bin/env python
import codecs
import re
from os import path

from setuptools import find_packages, setup


def read(*parts):
    file_path = path.join(path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding="utf-8").read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")


setup(
    name="sphinxcontrib-django-urls",
    version=find_version("sphinxcontrib_django_urls", "__init__.py"),
    license="MIT",
    description="Improve the Sphinx autodoc for Django views by adding urls.",
    long_description=read("README.md"),
    long_description_content_type = "text/markdown",
    author="Mohamed ElKalioby",
    author_email="mkalioby@mkalioby.com",
    url="https://github.com/mkalioby/sphinxcontrib-django-urls",
    download_url="https://github.com/mkalioby/sphinxcontrib-django-urls/zipball/master",
    packages=find_packages(exclude=("example*",)),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Framework :: Django :: 1.8",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)