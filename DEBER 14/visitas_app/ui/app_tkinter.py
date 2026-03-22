import tkinter as tk
from tkinter import ttk, messagebox
from modelos.visitante import Visitante

class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Registro de Visitantes")
        self.root.geometry("600x400")

        # ===== FORMULARIO =====
        tk.Label(root, text="Cédula").grid(row=0, column=0)
        self.entry_cedula = tk.Entry(root)
        self.entry_cedula.grid(row=0, column=1)

        tk.Label(root, text="Nombre").grid(row=1, column=0)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=1, column=1)

        tk.Label(root, text="Motivo").grid(row=2, column=0)
        self.entry_motivo = tk.Entry(root)
        self.entry_motivo.grid(row=2, column=1)

        # ===== BOTONES =====
        tk.Button(root, text="Registrar", command=self.registrar).grid(row=3, column=0)
        tk.Button(root, text="Eliminar", command=self.eliminar).grid(row=3, column=1)
        tk.Button(root, text="Limpiar", command=self.limpiar).grid(row=3, column=2)

        # ===== TABLA =====
        self.tree = ttk.Treeview(root, columns=("Cedula", "Nombre", "Motivo"), show="headings")
        self.tree.heading("Cedula", text="Cédula")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Motivo", text="Motivo")

        self.tree.grid(row=4, column=0, columnspan=3, pady=10)

        self.actualizar_tabla()

    # ===== FUNCIONES =====
    def registrar(self):
        cedula = self.entry_cedula.get()
        nombre = self.entry_nombre.get()
        motivo = self.entry_motivo.get()

        if not cedula or not nombre or not motivo:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        visitante = Visitante(cedula, nombre, motivo)

        if self.servicio.registrar_visitante(visitante):
            messagebox.showinfo("Éxito", "Visitante registrado")
            self.actualizar_tabla()
            self.limpiar()
        else:
            messagebox.showerror("Error", "La cédula ya existe")

    def eliminar(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un registro")
            return

        item = self.tree.item(seleccionado)
        cedula = item["values"][0]

        if self.servicio.eliminar_visitante(cedula):
            messagebox.showinfo("Éxito", "Registro eliminado")
            self.actualizar_tabla()

    def limpiar(self):
        self.entry_cedula.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_motivo.delete(0, tk.END)

    def actualizar_tabla(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)

        for v in self.servicio.obtener_visitantes():
            self.tree.insert("", tk.END, values=(v.cedula, v.nombre, v.motivo))