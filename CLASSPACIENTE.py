
import tkinter as tk
from tkinter import messagebox


class Paciente:
    ARCHIVO = "Paciente.txt"

    def __init__(self, nombre, identificacion, edad, ciudad):
        self.nombre = nombre
        self.identificacion = identificacion
        self.edad = int(edad)
        self.ciudad = ciudad

    def mostrar_datos(self):
        return (
            f"Nombre: {self.nombre}\n"
            f"Identificación: {self.identificacion}\n"
            f"Edad: {self.edad} años\n"
            f"Ciudad: {self.ciudad}"
        )

    def crear(self):
        with open(self.ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{self.nombre}|{self.identificacion}|"
                f"{self.edad}|{self.ciudad}\n"
            )

    @classmethod
    def consultar(cls):
        pacientes = []

        try:
            with open(cls.ARCHIVO, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    datos = linea.strip().split("|")

                    if len(datos) == 4:
                        nombre, identificacion, edad, ciudad = datos
                        pacientes.append(
                            cls(nombre, identificacion, edad, ciudad)
                        )
        except FileNotFoundError:
            pass

        return pacientes

    @classmethod
    def editar(cls, identificacion, nuevo_paciente):
        pacientes = cls.consultar()
        encontrado = False

        with open(cls.ARCHIVO, "w", encoding="utf-8") as archivo:
            for paciente in pacientes:
                if paciente.identificacion == identificacion:
                    paciente = nuevo_paciente
                    encontrado = True

                archivo.write(
                    f"{paciente.nombre}|{paciente.identificacion}|"
                    f"{paciente.edad}|{paciente.ciudad}\n"
                )

        return encontrado

    @classmethod
    def eliminar(cls, identificacion):
        pacientes = cls.consultar()
        encontrados = [
            p for p in pacientes
            if p.identificacion == identificacion
        ]

        if not encontrados:
            return False

        pacientes = [
            p for p in pacientes
            if p.identificacion != identificacion
        ]

        with open(cls.ARCHIVO, "w", encoding="utf-8") as archivo:
            for paciente in pacientes:
                archivo.write(
                    f"{paciente.nombre}|{paciente.identificacion}|"
                    f"{paciente.edad}|{paciente.ciudad}\n"
                )

        return True


# ---------------- VENTANA PRINCIPAL ----------------

ventana = tk.Tk()
ventana.title("Gestión de Pacientes")
ventana.geometry("480x760")
ventana.configure(bg="#0F172A")
ventana.resizable(False, False)

titulo = tk.Label(
    ventana,
    text="GESTIÓN DE PACIENTES",
    font=("Arial", 18, "bold"),
    bg="#0F172A",
    fg="#67E8F9"
)
titulo.pack(pady=20)

campos = {}

for clave, etiqueta in [
    ("nombre", "Nombre"),
    ("identificacion", "Identificación"),
    ("edad", "Edad"),
    ("ciudad", "Ciudad")
]:
    tk.Label(
        ventana,
        text=etiqueta,
        font=("Arial", 11),
        bg="#0F172A",
        fg="white"
    ).pack(pady=(8, 3))

    entrada = tk.Entry(
        ventana,
        font=("Arial", 12),
        width=32,
        bg="#1E293B",
        fg="white",
        insertbackground="white",
        relief="flat"
    )
    entrada.pack(ipady=7)

    campos[clave] = entrada


def obtener_datos():
    nombre = campos["nombre"].get().strip()
    identificacion = campos["identificacion"].get().strip()
    edad = campos["edad"].get().strip()
    ciudad = campos["ciudad"].get().strip()

    if not nombre or not identificacion or not edad or not ciudad:
        messagebox.showwarning(
            "Campos incompletos",
            "Por favor, complete todos los campos."
        )
        return None

    try:
        edad = int(edad)
        if edad < 0 or edad > 120:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Edad inválida",
            "Ingrese una edad entre 0 y 120 años."
        )
        return None

    return Paciente(nombre, identificacion, edad, ciudad)


def limpiar_campos():
    for entrada in campos.values():
        entrada.delete(0, tk.END)


def registrar():
    paciente = obtener_datos()

    if paciente is None:
        return

    pacientes = Paciente.consultar()

    if any(
        p.identificacion == paciente.identificacion
        for p in pacientes
    ):
        messagebox.showwarning(
            "Registro existente",
            "Ya existe un paciente con esa identificación."
        )
        return

    paciente.crear()
    messagebox.showinfo(
        "Registro exitoso",
        "El paciente fue registrado correctamente."
    )

    limpiar_campos()
    actualizar_lista()


def consultar():
    actualizar_lista()

    pacientes = Paciente.consultar()

    if not pacientes:
        messagebox.showinfo(
            "Consulta",
            "No hay pacientes registrados."
        )


def seleccionar_paciente(event):
    seleccion = lista.curselection()

    if not seleccion:
        return

    paciente = Paciente.consultar()[seleccion[0]]

    limpiar_campos()

    campos["nombre"].insert(0, paciente.nombre)
    campos["identificacion"].insert(0, paciente.identificacion)
    campos["edad"].insert(0, paciente.edad)
    campos["ciudad"].insert(0, paciente.ciudad)


def editar():
    identificacion = campos["identificacion"].get().strip()

    if not identificacion:
        messagebox.showwarning(
            "Identificación",
            "Ingrese o seleccione la identificación del paciente."
        )
        return

    nuevo_paciente = obtener_datos()

    if nuevo_paciente is None:
        return

    if Paciente.editar(identificacion, nuevo_paciente):
        messagebox.showinfo(
            "Actualización",
            "Paciente actualizado correctamente."
        )
        limpiar_campos()
        actualizar_lista()
    else:
        messagebox.showerror(
            "Error",
            "No se encontró el paciente."
        )


def eliminar():
    identificacion = campos["identificacion"].get().strip()

    if not identificacion:
        messagebox.showwarning(
            "Identificación",
            "Ingrese o seleccione la identificación del paciente."
        )
        return

    confirmar = messagebox.askyesno(
        "Confirmar eliminación",
        "¿Está seguro de eliminar este paciente?"
    )

    if confirmar:
        if Paciente.eliminar(identificacion):
            messagebox.showinfo(
                "Eliminación",
                "Paciente eliminado correctamente."
            )
            limpiar_campos()
            actualizar_lista()
        else:
            messagebox.showerror(
                "Error",
                "No se encontró el paciente."
            )


def actualizar_lista():
    lista.delete(0, tk.END)

    pacientes = Paciente.consultar()

    for paciente in pacientes:
        lista.insert(
            tk.END,
            f"{paciente.nombre} - {paciente.identificacion}"
        )


# ---------------- BOTONES ----------------

botones = [
    ("REGISTRAR PACIENTE", registrar),
    ("CONSULTAR PACIENTES", consultar),
    ("EDITAR PACIENTE", editar),
    ("ELIMINAR PACIENTE", eliminar),
]

for texto, funcion in botones:
    tk.Button(
        ventana,
        text=texto,
        command=funcion,
        font=("Arial", 10, "bold"),
        bg="#0891B2",
        fg="white",
        activebackground="#06B6D4",
        activeforeground="white",
        relief="flat",
        width=27,
        pady=8,
        cursor="hand2"
    ).pack(pady=5)


tk.Label(
    ventana,
    text="PACIENTES REGISTRADOS",
    font=("Arial", 12, "bold"),
    bg="#0F172A",
    fg="#67E8F9"
).pack(pady=(15, 8))

lista = tk.Listbox(
    ventana,
    width=48,
    height=9,
    font=("Arial", 10),
    bg="#1E293B",
    fg="white",
    selectbackground="#0891B2",
    relief="flat"
)
lista.pack(padx=15, pady=5)

lista.bind("<<ListboxSelect>>", seleccionar_paciente)

actualizar_lista()

ventana.mainloop()
