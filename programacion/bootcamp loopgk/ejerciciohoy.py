
class Usuario:
    def __init__(self, usuario, contraseña, nombre, apellido, correo):
        self.usuario=usuario
        self.contraseña=contraseña
        self.nombre= nombre
        self.apellido= apellido
        self.correo= correo

    def registro(self):
        return f"{self.nombre} {self.apellido} tus datos se han registrado exitosamente"

    dwef


usuario1 =Usuario("juan324", 12345, "juan", "lopez", "lop123@gm.com" )
print(usuario1.registro())
