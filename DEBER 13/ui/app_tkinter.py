import tkinter as tk
from tkinter import messagebox
from modelos.vehiculo import Vehiculo
from servicios.garaje_servicio import GarajeServicio


class GarajeApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Garaje")

        self.servicio = GarajeServicio()

        # ----- Título -----
        titulo = tk.Label(root, text="Registro de Vehículos", font=("Arial", 16))
        titulo.pack(pady=10)

        # ----- Frame formulario -----
        frame = tk.Frame(root)
        frame.pack()

        # Placa
        tk.Label(frame, text="Placa").grid(row=0, column=0)
        self.entry_placa = tk.Entry(frame)
        self.entry_placa.grid(row=0, column=1)

        # Marca
        tk.Label(frame, text="Marca").grid(row=1, column=0)
        self.entry_marca = tk.Entry(frame)
        self.entry_marca.grid(row=1, column=1)

        # Propietario
        tk.Label(frame, text="Propietario").grid(row=2, column=0)
        self.entry_propietario = tk.Entry(frame)
        self.entry_propietario.grid(row=2, column=1)

        # ----- Botones -----
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        btn_agregar = tk.Button(frame_botones, text="Agregar Vehículo", command=self.agregar_vehiculo)
        btn_agregar.grid(row=0, column=0, padx=5)

        btn_limpiar = tk.Button(frame_botones, text="Limpiar", command=self.limpiar_campos)
        btn_limpiar.grid(row=0, column=1, padx=5)

        # ----- Lista de vehículos -----
        self.lista = tk.Listbox(root, width=50)
        self.lista.pack(pady=10)

    def agregar_vehiculo(self):

        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        propietario = self.entry_propietario.get()

        if placa == "" or marca == "" or propietario == "":
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        vehiculo = Vehiculo(placa, marca, propietario)

        self.servicio.agregar_vehiculo(vehiculo)

        self.actualizar_lista()

        self.limpiar_campos()

    def actualizar_lista(self):

        self.lista.delete(0, tk.END)

        for v in self.servicio.listar_vehiculos():
            self.lista.insert(tk.END, str(v))

    def limpiar_campos(self):

        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)