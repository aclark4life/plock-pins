Plock Pins
==========

Hosted Buildout configuration files for all your Plone deployments and versions.

Usage
-----

Installation of Plone with Plock Pins looks like this::

    $ virtualenv-2.7
    $ bin/pip install --upgrade setuptools
    $ bin/pip install zc.buildout
    $ bin/buildout init

Edit ``buildout.cfg`` to contain::

    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-5-0

Now run Buildout.
