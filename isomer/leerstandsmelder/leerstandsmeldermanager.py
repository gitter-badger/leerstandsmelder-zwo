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

"""


Module: leerstandsmelderManager
===============================


"""

from isomer.component import ConfigurableComponent, handler
from isomer.events.system import authorized_event
from isomer.events.client import send


class leerstandsmelderevent(authorized_event):
    pass


class leerstandsmelderManager(ConfigurableComponent):
    """
    """

    configprops = {
        'some_bool_field': {
            'type': 'boolean',
            'title': 'Some bool field',
            'description': 'Sample Field for boolean configuration values',
            'default': True
        }
    }

    channel = 'isomer-web'

    def __init__(self, *args, **kwargs):
        """
        Initialize the leerstandsmelder Manager component.

        :param args:
        """

        super(leerstandsmelderManager, self).__init__(
            "LEERSTANDSMELDERMANAGER",
            *args, **kwargs
        )

        self.log("Started")

    @handler(leerstandsmelderevent)
    def leerstandsmelderevent(self, event):
        """Handler for sample event"""

        packet = {
            'component': 'isomer.leerstandsmelder.leerstandsmeldermanager',
            'action': 'leerstandsmelderevent',
            'data': {
                'text': 'Hello World!'
            }
        }

        self.fireEvent(send(event.client.uuid, packet))
