
import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class Horario:

    def __init__(self, medico, dia, hora_inicio, hora_fin):
        self.medico = medico
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.disponible = True

    # Mostrar información del horario
    def mostrar_horario(self):
        estado = "Disponible" if self.disponible else "No disponible"

        return (
            f"Médico: {self.medico}\n"
            f"Día: {self.dia}\n"
            f"Horario: {self.hora_inicio} - {self.hora_fin}\n"
            f"Estado: {estado}"
        )


def registrar():

    datos = [entrada.get().strip() for entrada in entradas]

    if not all(datos):
        messagebox.showwarning(
            "Campos incompletos",
            "Por favor, completa todos los campos."
        )
        return

    medico, dia, hora_inicio, hora_fin = datos

    dias_validos = [
        "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"
    ]

    if dia.capitalize() not in dias_validos:
        messagebox.showerror(
            "Día inválido",
            "Ingresa: Lun, Mar, Mie, Jue, Vie o Sab."
        )
        return

    try:
        inicio = datetime.strptime(hora_inicio, "%H:%M")
        fin = datetime.strptime(hora_fin, "%H:%M")

        if fin <= inicio:
            messagebox.showerror(
                "Horario inválido",
                "La hora de finalización debe ser posterior "
                "a la hora de inicio."
            )
            return

        horario = Horario(
            medico,
            dia.capitalize(),
            hora_inicio,
            hora_fin
        )

        resultado.config(
            text=horario.mostrar_horario(),
            fg="#67E8F9"
        )

        messagebox.showinfo(
            "Registro exitoso",
            "El horario fue registrado correctamente."
        )

        for entrada in entradas:
            entrada.delete(0, tk.END)

    except ValueError:
        messagebox.showerror(
            "Formato incorrecto",
            "Utiliza el formato de hora HH:MM. Ejemplo: 08:00."
        )


# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Horarios")
ventana.geometry("380x470")
ventana.configure(bg="#0F172A")
ventana.resizable(False, False)


# Título
tk.Label(
    ventana,
    text="HORARIOS MÉDICOS",
    font=("Arial", 16, "bold"),
    bg="#0F172A",
    fg="#38BDF8"
).pack(pady=20)


# Campos de entrada
entradas = []

campos = [
    "Nombre del médico",
    "Día (Lun, Mar, Mie, Jue, Vie, Sab)",
    "Hora de inicio (HH:MM)",
    "Hora de finalización (HH:MM)"
]

for texto in campos:

    tk.Label(
        ventana,
        text=texto,
        font=("Arial", 10),
        bg="#0F172A",
        fg="white"
    ).pack()

    entrada = tk.Entry(
        ventana,
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
        pady=(3, 10)
    )

    entradas.append(entrada)


# Botón de registro
tk.Button(
    ventana,
    text="REGISTRAR HORARIO",
    command=registrar,
    bg="#0284C7",
    fg="white",
    font=("Arial", 10, "bold"),
    relief="flat",
    cursor="hand2"
).pack(pady=12, ipadx=15, ipady=6)


# Resultado
resultado = tk.Label(
    ventana,
    text="Los datos aparecerán aquí",
    bg="#1E293B",
    fg="#94A3B8",
    font=("Arial", 11),
    justify="left",
    anchor="w",
    padx=15,
    pady=12
)

resultado.pack(
    fill="x",
    padx=25,
    pady=5
)


ventana.mainloop()
