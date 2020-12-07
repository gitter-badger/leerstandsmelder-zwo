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
Schema: region
==============

Contains
--------

region: combines groups of moderators with region-local locations and other meta data


"""

from isomer.schemata.defaultform import *
from isomer.schemata.base import base_object, uuid_object, geo_coordinate

regionSchema = base_object('region', no_additional=True)


regionSchema['properties'].update({
    'title': {'type': 'string'},
    'description': {'type': 'string'},
    'zoom': {'type': 'integer', 'max': 16, 'min': 5},
    'coordinate': geo_coordinate(),
    'moderators': {
        'type': 'array',
        'items': uuid_object('user'),
    },
    'active': {'type': 'boolean'},
    'hide': {'type': 'boolean'},
    'hide_message': {'type': 'string'},
    'slug': {'type': 'string'},
    'slug_aliases': {'type': 'string'},
    'created': {'type': 'string', 'format': 'datetime'},
    'updated': {'type': 'string', 'format': 'datetime'},
})

regionForm = [
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

region = {
    'schema': regionSchema,
    'form': regionForm
}
