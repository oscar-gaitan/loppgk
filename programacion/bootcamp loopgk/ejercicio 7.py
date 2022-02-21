from bdb import GENERATOR_AND_COROUTINE_FLAGS


cantidad= float(input("Que cantidad desea invertir: "))
interes= float(input("Cual es la tasa de interes: "))
tiempo=float(input("Tiempo de su inersion: "))
interesn=interes/ 100
ganancia=(cantidad * interesn)*tiempo
nuevosaldo=cantidad + ganancia
print("los inereses que obtendra son: ", ganancia)
print("su nuevo saldo con intereses sera:", nuevosaldo)