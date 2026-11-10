
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class Cita:

    ETIQUETAS = {
        "paciente": "Paciente",
        "medico": "Médico",
        "fecha": "Fecha",
        "hora": "Hora",
        "tipo": "Tipo",
    }

    def __init__(self, paciente, medico, fecha, hora, tipo):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.hora = hora
        self.tipo = tipo

    # Mostrar información de la cita
    def mostrar_cita(self):
        return "\n".join(
            f"{etiqueta}: {getattr(self, clave)}"
            for clave, etiqueta in self.ETIQUETAS.items()
        )


class VentanaCitas(tk.Tk):

    CAMPOS = [
        ("paciente", "Nombre del paciente"),
        ("medico", "Nombre del médico"),
        ("fecha", "Fecha (DD/MM/AAAA)"),
        ("hora", "Hora (HH:MM)"),
        ("tipo", "Tipo de cita"),
    ]

    def __init__(self):
        super().__init__()

        self.title("Registro de Citas")
        self.geometry("400x580")
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
            anchor="w",
            wraplength=340,
            padx=15,
            pady=12
        )

        self.resultado.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=10
        )

    def _crear_formulario(self):

        tk.Label(
            self,
            text="GESTIÓN DE CITAS MÉDICAS",
            font=("Arial", 15, "bold"),
            bg="#0F172A",
            fg="#38BDF8"
        ).pack(pady=18)

        for clave, etiqueta in self.CAMPOS:

            tk.Label(
                self,
                text=etiqueta,
                font=("Arial", 10),
                bg="#0F172A",
                fg="white"
            ).pack()

            entrada = tk.Entry(
                self,
                font=("Arial", 11),
                bg="#1E293B",
                fg="white",
                insertbackground="white",
                relief="flat"
            )

            entrada.pack(
                padx=40,
                fill="x",
                ipady=5,
                pady=(3, 8)
            )

            self.entradas[clave] = entrada

        tk.Button(
            self,
            text="REGISTRAR CITA",
            command=self.registrar,
            bg="#0284C7",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2"
        ).pack(pady=12, ipadx=15, ipady=6)

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
            # Validar fecha
            datetime.strptime(datos["fecha"], "%d/%m/%Y")

            # Validar hora
            datetime.strptime(datos["hora"], "%H:%M")

            # Crear cita
            cita = Cita(**datos)

            self.resultado.config(
                text=cita.mostrar_cita(),
                fg="#67E8F9"
            )

            messagebox.showinfo(
                "Registro exitoso",
                "La cita fue registrada correctamente."
            )

            # Limpiar campos
            for entrada in self.entradas.values():
                entrada.delete(0, tk.END)

        except ValueError:
            messagebox.showerror(
                "Datos inválidos",
                "Verifica la fecha (DD/MM/AAAA) "
                "y la hora (HH:MM)."
            )


if __name__ == "__main__":
    VentanaCitas().mainloop()
