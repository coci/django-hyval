# -*- coding: utf-8 -*-
#
# Copyright (C) 2021- Soroush Safari <mr.safarii1992@gmail.com>
#
# This file is part of Hyval.
#
# Hyval is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hyval is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with grest.  If not, see <http://www.gnu.org/licenses/>.
#

import re
from os.path import dirname, join

from setuptools import find_packages, setup

# Extract requirements from requirements.txt
REQUIREMENTS = [
    r.rstrip() for r in open(
        join(
            dirname(__file__),
            'requirements.txt')).readlines()]

print(REQUIREMENTS)
with open(join(dirname(__file__), 'hyval', '__init__.py')) as v_file:
    package_version = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="django-hyval",
    version=package_version,
    description="Encryption over django CharField",
    url="https://github.com/coci/django-hyval",
    author="Soroush Safari",
    author_email="soroush.safari1992@gmail.com",
    license="GPLv3",
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=REQUIREMENTS,
    packages=find_packages(),
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    python_requires='>=3.6',
    zip_safe=False
)
