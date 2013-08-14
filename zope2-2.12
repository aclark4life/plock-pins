[buildout]
allow-hosts = *.python.org
extends = http://download.zope.org/Zope2/index/2.12.20/versions.cfg
extends-cache = .
extensions = buildout.bootstrap
parts = zope2

[zope2]
recipe = plone.recipe.zope2instance
eggs = Zope2
user = admin:admin

[versions]
distribute = 0.6.30
zc.buildout = 1.6.3
