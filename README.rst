Plock Pins
==========

Hosted configuration files for all versions of Plone

Usage
-----

Install Plone with Plock Pins

Install virtualenv & buildout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ virtualenv-2.7
    $ bin/pip install zc.buildout
    $ bin/buildout init

Edit buildout.cfg
~~~~~~~~~~~~~~~~~

::

    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-4-3

Run Buildout & Start Plone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ bin/buildout
    $ bin/plone fg
