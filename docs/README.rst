Leerstandsmelder Zwo
====================

This is the new Leerstandsmelder.


This software package is a module for `Isomer <https://github.com/isomeric/isomer>`__.

It comes with its own full frontend. Most of Isomer's old frontend technology will be
rebuilt with new technology for this package and parts will be reused in the new
generalized, next generation Isomer frontend.

Bugs & Discussion
=================

Please research any bugs you find via our `Github issue tracker for
Leerstandsmelder <https://github.com/leerstandsmelder/leerstandsmelder-zwo/issues>`__
and report them, if they're still unknown.

You can also find us here:

.. TODO: Mention chat location? Do we want to have a discord or something?

* Chat:
* Github Org: `github.com/isomeric <https://github.com/isomeric>`__

Installation
============

Install Isomer first, then install this module, its provisions and finally
rebuild your frontend.
Restarting the Isomer backend should now give you access to the Leerstandsmelder
components.

Development Setup
=================

These instructions are for Debian. If you're not on Debian, you'll need to get two parts
running. An asterisk in the following lists means, that earlier versions might work,
too - no guarantees!

Backend
-------

 * Python >= 3.6
 * Pip3 >= 20.0*
 * Pymongo for Python3 >= 3.0
 * Pillow for Python3 >= 8.0*
 * MongoDB >= 3.2


Frontend
--------

Debian Sid has these, Buster is very probably too old:

 * nodejs >= 12.0 (>= 10.0 *might* work, too)
 * npm >= 7.1.0

Setting up with (Debian) Linux
------------------------------

There are instructions for multiple variants of setting up Isomer along with
the Leerstandsmelder-zwo module at the `Isomer documentation site,
<https://isomer.readthedocs.io/en/latest/start/quick.html>`_ but here's a quick rough up
for immediate development.

OS preparations
~~~~~~~~~~~~~~~

Below are instructions to set up Debian and most derivatives like Ubuntu.
These may be different for Arch, Gentoo, FreeBSD, etc, so please adapt:

.. code-block::

    # Development basics
    sudo apt install git virtualenv gnupg wget python3 python3-pip

    # Isomer specific
    sudo apt install python3-pymongo python3-pymongo-ext python3-spur \
        python3-bson pyton3-bson-ext enchant

    # Install these only if you're at least on Debian Sid:
    sudo apt install nodejs npm

Isomer + Leerstandsmelder Zwo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's download the source code and install it for development:

.. code-block::

    mkdir leerstandsmelder-zwo

    cd leerstandsmelder-zwo
    git clone https://github.com/isomeric/isomer.git
    git clone https://github.com/Leerstandsmelder/leerstandsmelder-zwo.git
    git clone https://github.com/leerstandsmelder/leerstandsmelder-zwo-frontend.git

    virtualenv -p /usr/bin/python3 --system-site-packages venv
    source venv/bin/activate

    cd isomer
    pip3 install -r requirements-dev.txt
    python3 setup.py develop

    cd ../leerstandsmelder-zwo
    python3 setup.py develop

Setting up an Instance
~~~~~~~~~~~~~~~~~~~~~~

Test installation and create default instance to work with:

.. code-block::

    iso dev entrypoints --all -f leerstand
    iso instance create

Create admin user:

.. code-block::

    iso db user create-admin

Frontend
~~~~~~~~

Install and build Frontend:

.. code-block::

    cd ../leerstandsmelder-zwo-frontend

    npm install -g ionic @angular/cli
    npm install
    ionic serve

See the frontend readme for more details on frontend matters.

History
=======

- 0.x? - RIP
- startnext(?)
- 1.0? - RIP
- 1.2.2 - Still working online
- 2.0! - In the works

License
=======

AGPL3.0
-------

Copyright (C) 2020 Leerstandsmelder Community and others.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
