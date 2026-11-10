

import tkinter as tk
from tkinter import messagebox

from CLASSPERSONA import Persona


class Medico(Persona):
    MESES_ANIO = 12

    def __init__(self, nombre, nacimiento, especialidad, sueldo):
        super().__init__(nombre, nacimiento)
        self.especialidad = especialidad
        self.sueldo = float(sueldo)

    # Calcular sueldo anual
    def calcular_sueldo_anual(self):
        return self.sueldo * self.MESES_ANIO

    # Mostrar información del médico
    def resumen(self):
        return (
            f"Médico: {self.nombre}\n"
            f"Edad: {self.calcular_edad()} años\n"
            f"Especialidad: {self.especialidad}\n"
            f"Sueldo mensual: ${self.sueldo:,.0f}\n"
            f"Sueldo anual: ${self.calcular_sueldo_anual():,.0f}"
        )


class VentanaMedico(tk.Tk):

    CAMPOS = [
        ("nombre", "Nombre del médico"),
        ("nacimiento", "Fecha de nacimiento (AAAA-MM-DD)"),
        ("especialidad", "Especialidad"),
        ("sueldo", "Sueldo mensual"),
    ]

    def __init__(self):
        super().__init__()

        self.title("Registro de Médico")
        self.geometry("380x380")
        self.configure(bg="#0F172A")
        self.resizable(False, False)

        self.entradas = {}

        self._crear_formulario()

        self.resultado = tk.Label(
            self,
            text="Los datos aparecerán aquí",
            bg="#1E293B",
            fg="#67E8F9",
            font=("Arial", 10),
            justify="left",
            padx=12,
            pady=10
        )

        self.resultado.pack(fill="x", padx=20, pady=15)

    def _crear_formulario(self):

        tk.Label(
            self,
            text="REGISTRO DE MÉDICOS",
            font=("Arial", 15, "bold"),
            bg="#0F172A",
            fg="#38BDF8"
        ).pack(pady=15)

        for clave, etiqueta in self.CAMPOS:

            tk.Label(
                self,
                text=etiqueta,
                bg="#0F172A",
                fg="white",
                font=("Arial", 10)
            ).pack()

            entrada = tk.Entry(
                self,
                font=("Arial", 10),
                bg="#1E293B",
                fg="white",
                insertbackground="white",
                relief="flat"
            )

            entrada.pack(
                padx=35,
                fill="x",
                ipady=4,
                pady=(3, 7)
            )

            self.entradas[clave] = entrada

        tk.Button(
            self,
            text="REGISTRAR MÉDICO",
            command=self.registrar,
            bg="#0284C7",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack(pady=10, ipadx=12, ipady=5)

    def registrar(self):

        datos = {
            clave: entrada.get().strip()
            for clave, entrada in self.entradas.items()
        }

        if not all(datos.values()):
            messagebox.showwarning(
                "Campos incompletos",
                "Por favor, completa todos los campos."
            )
            return

        try:
            medico = Medico(**datos)

            if medico.sueldo < 0:
                raise ValueError

            self.resultado.config(
                text=medico.resumen()
            )

        except ValueError:
            messagebox.showerror(
                "Datos inválidos",
                "Verifica la fecha de nacimiento y el sueldo."
            )


if __name__ == "__main__":
    VentanaMedico().mainloop()
