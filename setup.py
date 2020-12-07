#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Leerstandsmelder
# ================
# Copyright (C) 2020 Leerstandsmelder Community <info@leerstandsmelder.de> and
# others.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages

setup(
    name="leerstandsmelder",
    version="2.0.0",
    description="leerstandsmelder",
    author="Leerstandsmelder Community",
    author_email="software@leerstandsmelder.de",
    url="https://github.com/leerstandsmelder/leerstandsmelder-zwo",
    license="GNU Affero General Public License v3",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        # 'Framework :: Isomer :: 1',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    packages=find_packages(),
    package_data={'isomer-leerstandsmelder': ['../docs/*', '../frontend/*']},
    include_package_data=True,
    long_description="""Leerstandsmelder
================

Der Leerstandsmelder wird den Bürger*innen die Möglichkeit geben, wieder auf
Stadtentwicklung Einfluss zu nehmen und sich konstruktiv zu beteiligen. Er wird dazu
beitragen, gesetzliche Maßnahmen durchzusetzen sowie Gesetze zu verschärfen. Sinnloser
Leerstand soll effizienter beseitigt werden, damit die vielen aktuell nicht genutzten
Quadratmeter dem überlasteten Wohnungsmarkt zur Verfügung gestellt werden können. 

Dieses Software-Paket ist ein Plugin-Modul für Isomer: https://isomer.eu
""",
    dependency_links=[
    ],
    install_requires=[
        'isomer>=1.0.7',
    ],
    entry_points="""[isomer.components]
    leerstandsmeldermanager=isomer.leerstandsmelder.leerstandsmeldermanager:leerstandsmelderManager
    [isomer.schemata]
    location=isomer.leerstandsmelder.location:location
    region=isomer.leerstandsmelder.region:region
    [isomer.provisions]
    location=isomer.leerstandsmelder.provisions.location:provision
    region=isomer.leerstandsmelder.provisions.region:provision
    """,
    test_suite="tests.main.main",
)
