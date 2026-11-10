
from datetime import date

class Persona:

    def __init__(self, nombre, nacimiento):
        self.nombre = nombre
        self.nacimiento = date.fromisoformat(nacimiento)

    # Calcular edad de la persona
    def calcular_edad(self):
        hoy = date.today()

        ya_cumplio = (
            (hoy.month, hoy.day) >=
            (self.nacimiento.month, self.nacimiento.day)
        )

        return hoy.year - self.nacimiento.year - (not ya_cumplio)

    # Mostrar información de la persona
    def mostrar_datos(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Fecha de nacimiento: {self.nacimiento}\n"
            f"Edad: {self.calcular_edad()} años"
        )
