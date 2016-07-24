Plock Pins
==========

Installation configuration files for Plone

Install
-------

::

    virtualenv-2.7 .;bin/pip install zc.buildout;echo "[buildout]\nextends = https://raw.githubusercontent.com/plock/pins/master/plone-5-0">buildout.cfg; bin/buildout;bin/plone fg

Versions
--------

Plone 5
+++++++

*Requires Python 2.7*

::

    [buildout]
    extends = http://raw.githubusercontent.com/plock/pins/master/plone-5-0

Plone 4
+++++++

*Requires Python 2.7*

::

    [buildout]
    extends = http://raw.githubusercontent.com/plock/pins/master/plone-4-3

Plone 3
+++++++

*Requires Python 2.4*

::

    [buildout]
    extends = http://raw.githubusercontent.com/plock/pins/master/plone-3-3

Plone 2
+++++++

*Requires Python 2.4*

::

    [buildout]
    extends = http://raw.githubusercontent.com/plock/pins/master/plone-2-5

Plone 1
+++++++

*Requires Python 2.4*

::

    [buildout]
    extends = http://raw.githubusercontent.com/plock/pins/master/plone-1-1
