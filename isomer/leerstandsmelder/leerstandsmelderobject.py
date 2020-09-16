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
Schema: leerstandsmelderobject
==============================

Contains
--------

leerstandsmelderobject: Sample structure to adapt to your own use cases


"""

from isomer.schemata.defaultform import *
from isomer.schemata.base import base_object

leerstandsmelderobjectSchema = base_object('leerstandsmelderobject')

leerstandsmelderobjectSchema['properties'].update({
    'text': {
        'type': 'string', 'title': 'Some Text',
        'description': 'Sample Text Field'
    },
    'number': {
        'type': 'integer', 'title': 'Some Integer',
        'description': 'Sample Integer Field'
    },
    'enum': {
        'type': 'string',
        'enum': [
            'Turtles', 'Lions', 'Hippos', 'Monkeys'
        ],
        'title': 'Some Enum',
        'description': 'Sample Enum Field'
    },
    'secret': {
        'type': 'string', 'title': 'Very Secret',
        'description': 'Sample Secret Field',
        'default': ''
    },
    'timestamp': {
        'type': 'string', 'format': 'datetimepicker',
        'title': 'Some Datetime',
        'description': 'Sample Datetime Field'
    }
})

leerstandsmelderobjectForm = [
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
    'secret',
    editbuttons
]

leerstandsmelderObject = {
    'schema': leerstandsmelderobjectSchema,
    'form': leerstandsmelderobjectForm
}
