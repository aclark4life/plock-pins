[addon]
packages =
    zope2_bootstrap
zcml = 
    zope2_bootstrap

[buildout]
extends = 
    https://raw.github.com/pythonpackages/buildout-zope2/master/2.13.20-versions.cfg
    https://raw.github.com/pythonpackages/buildout-zope2/master/base.cfg

[zope2]
eggs = 
    ${base:packages}
    ${addon:packages}
recipe = plone.recipe.zope2instance
user = admin:admin
zcml = 
    ${base:zcml}
    ${addon:zcml}
