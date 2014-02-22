[buildout]
parts += wsgi

[wsgi]
recipe = collective.recipe.template
url = https://raw.github.com/plock/pins/master/wsgi-ini
output = ${buildout:directory}/plone.ini

[plone]
eggs +=
    PasteScript
    WebError
    repoze.retry
    repoze.tm2
    repoze.vhm
scripts += paster
