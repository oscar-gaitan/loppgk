
from tokenize import PseudoExtras

from pkg_resources import PkgResourcesDeprecationWarning


payaso=int(input("Ingrese cantidad de payasos a enviar: "))
muñeca=int(input("Ingrese cantidad de muñecas a enviar: "))

peso_payaso= payaso * 0.112 
peso_muñeca= muñeca * 0.075
total= peso_muñeca + peso_payaso
print("peso total de payasos en kg: ",peso_payaso)
print("peso total de muñecas en kg: ", peso_muñeca)
print("Peso totalo del paquete a enviar: ", total, "kgs")