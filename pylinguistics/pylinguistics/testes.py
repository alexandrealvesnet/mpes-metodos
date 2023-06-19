import Pylinguistics as pl
objpl=pl.text('foi dado nessa decisão que o executor não deve ser aplicado na ausência de interrupções ou suspensões do prazo prescrito, sendo seu silêncio interpretado como extensão do fato.')
objpl.setLanguage("pt-br")
# this is a multiline comment
output = objpl.getFeatures()
print(output)

"""valor = "{:.2f}".format(13.949999999999999)
print(valor)"""
