Plock Pins
==========

Extendable configuration files for Plone

Install Plone 
-------------

::

    $ virtualenv-2.7
    $ bin/pip install zc.buildout
    $ echo "[buildout]\nextends = https://raw.github.com/plock/pins/dev/plone-4-3" > buildout.cfg
    $ bin/buildout
    $ bin/plone fg
