def funcion_decoradora(funcion):
    def funcion_interna():
        funcion()
        print("se reaalizara un calculo")
        return funcion_interna

