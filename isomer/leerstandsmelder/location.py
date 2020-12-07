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

__author__ = "Heiko 'riot' Weinen"
__license__ = "AGPLv3"

"""
Schema: location
================

Contains
--------

location: basic data structure to capture vacancies.


"""

from isomer.schemata.defaultform import *
from isomer.schemata.base import base_object, uuid_object, geo_coordinate

locationSchema = base_object('location', no_additional=True)


locationSchema['properties'].update({
    'title': {'type': 'string'},
    'description': {'type': 'string'},
    'degree': {'type': 'string'},
    'emptySince': {'type': 'string', 'format': 'datetime'},
    'buildingType': {'type': 'string'},
    'reporter': {'type': 'string'},
    'street': {'type': 'string'},
    'city': {'type': 'string'},
    'postcode': {'type': 'string'},
    'coordinate': geo_coordinate(),
    'region': uuid_object('region'),
    'active': {'type': 'boolean'},
    'demolished': {'type': 'boolean'},
    'demolish_rumor': {'type': 'boolean'},
    'slug': {'type': 'string'},
    'slug_aliases': {'type': 'string'},
    'created': {'type': 'string', 'format': 'datetime'},
    'updated': {'type': 'string', 'format': 'datetime'},
})

locationForm = [
    {
        'type': 'section',
        'htmlClass': 'row',
        'items': [
            {
                'type': 'section',
                'htmlClass': 'col-xs-4',
                'items': [
                    'text', 'number'
                ]
            },
            {
                'type': 'section',
                'htmlClass': 'col-xs-4',
                'items': [
                    'enum', 'timestamp'
                ]
            },
        ]
    },
    editbuttons
]

location = {
    'schema': locationSchema,
    'form': locationForm
}
