import tkinter as tk
from tkinter import messagebox


class Paciente:
    def __init__(self, nombre, identificacion, edad, ciudad):
        self.nombre = nombre
        self.identificacion = identificacion
        self.edad = edad
        self.ciudad = ciudad

    def mostrar_datos(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Identificación: {self.identificacion}\n"
            f"Edad: {self.edad} años\n"
            f"Ciudad: {self.ciudad}"
        )

    # Guardar paciente en archivo de texto
    def guardar(self):
        with open("Paciente.txt", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{self.nombre}|{self.identificacion}|"
                f"{self.edad}|{self.ciudad}\n"
            )


def registrar():
    n = nombre.get().strip()
    i = identificacion.get().strip()
    e = edad.get().strip()
    c = ciudad.get().strip()

    if not n or not i or not e or not c:
        messagebox.showwarning(
            "Campos incompletos",
            "Por favor, completa todos los campos."
        )
        return

    try:
        e = int(e)

        if e < 0 or e > 120:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Edad inválida",
            "Ingresa una edad entre 0 y 120 años."
        )
        return

    paciente = Paciente(n, i, e, c)

    # Guardar información en el archivo TXT
    try:
        paciente.guardar()

        resultado.config(
            text=paciente.mostrar_datos(),
            fg="#67E8F9"
        )

        messagebox.showinfo(
            "Registro exitoso",
            "El paciente fue registrado y guardado correctamente."
        )

        # Limpiar campos
        nombre.delete(0, tk.END)
        identificacion.delete(0, tk.END)
        edad.delete(0, tk.END)
        ciudad.delete(0, tk.END)

    except OSError as error:
        messagebox.showerror(
            "Error al guardar",
            f"No se pudo guardar el paciente:\n{error}"
        )


# Ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Pacientes")
ventana.geometry("380x500")
ventana.configure(bg="#0F172A")
ventana.resizable(False, False)


# Título
tk.Label(
    ventana,
    text="✚ GESTIÓN DE PACIENTES",
    font=("Arial", 16, "bold"),
    bg="#0F172A",
    fg="#38BDF8"
).pack(pady=20)


# Campos de entrada
campos = {}

for texto in ("Nombre", "Identificación", "Edad", "Ciudad"):
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

    campos[texto] = entrada


nombre = campos["Nombre"]
identificacion = campos["Identificación"]
edad = campos["Edad"]
ciudad = campos["Ciudad"]


# Botón de registro
tk.Button(
    ventana,
    text="REGISTRAR PACIENTE",
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


