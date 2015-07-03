Plock Pins
==========

Extendable configuration files for Plone

Install Plone 
-------------

Cut and paste in terminal

::

    virtualenv-2.7 .
    bin/pip install zc.buildout
    echo "[buildout]\nextends = https://raw.githubusercontent.com/plock/pins/master/plone-4-3" \
        > buildout.cfg
    bin/buildout
    bin/plone foreground
