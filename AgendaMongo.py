#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

class VentanaInicio:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Inicio")

        self.etiqueta_usuario = tk.Label(ventana, text="Usuario:")
        self.etiqueta_usuario.grid(row=0, column=0)

        self.entry_usuario = tk.Entry(ventana)
        self.entry_usuario.grid(row=0, column=1)

        self.boton_ingresar = tk.Button(ventana, text="Ingresar", command=self.abrir_agenda)
        self.boton_ingresar.grid(row=1, columnspan=2)

        # Conexión a la base de datos MongoDB con usuario no administrador
        # Autenticar en la base de datos "agenda"
        self.cliente = MongoClient("localhost", 27017, username="usuario", password="password_seguro", authSource="agenda")
        self.db = self.cliente["agenda"]
        self.collection = self.db["contactos"]

    def abrir_agenda(self):
        nombre_usuario = self.entry_usuario.get()
        if nombre_usuario:
            ventana_agenda = tk.Toplevel(self.ventana)
            app = AgendaApp(ventana_agenda, nombre_usuario, self.collection)
        else:
            messagebox.showerror("Error", "Por favor, ingrese un nombre de usuario")

class AgendaApp:
    def __init__(self, ventana, nombre_usuario, collection):
        self.ventana = ventana
        self.ventana.title("Agenda")

        self.nombre_usuario = nombre_usuario
        self.collection = collection

        self.etiqueta_nombre = tk.Label(ventana, text="Nombre:")
        self.etiqueta_nombre.grid(row=0, column=0)

        self.etiqueta_telefono = tk.Label(ventana, text="Teléfono:")
        self.etiqueta_telefono.grid(row=1, column=0)

        self.entry_nombre = tk.Entry(ventana)
        self.entry_nombre.grid(row=0, column=1)

        self.entry_telefono = tk.Entry(ventana)
        self.entry_telefono.grid(row=1, column=1)

        self.boton_crear = tk.Button(ventana, text="Crear contacto", command=self.crear_contacto)
        self.boton_crear.grid(row=2, columnspan=2)

        self.boton_consultar = tk.Button(ventana, text="Consultar contacto", command=self.consultar_contacto)
        self.boton_consultar.grid(row=3, columnspan=2)

        self.boton_borrar = tk.Button(ventana, text="Borrar contacto", command=self.borrar_contacto)
        self.boton_borrar.grid(row=4, columnspan=2)

        self.boton_modificar = tk.Button(ventana, text="Modificar teléfono", command=self.modificar_telefono)
        self.boton_modificar.grid(row=5, columnspan=2)

    def crear_contacto(self):
        nombre = self.entry_nombre.get()
        telefono = self.entry_telefono.get()

        contacto_existente = self.collection.find_one({"nombre": nombre, "usuario": self.nombre_usuario})
        if contacto_existente:
            messagebox.showerror("Error", "El contacto ya existe")
        else:
            self.collection.insert_one({"nombre": nombre, "telefono": telefono, "usuario": self.nombre_usuario})
            messagebox.showinfo("Éxito", "Se ha creado el contacto")

    def consultar_contacto(self):
        nombre = self.entry_nombre.get()
        contacto = self.collection.find_one({"nombre": nombre, "usuario": self.nombre_usuario})
        if contacto:
            messagebox.showinfo("Contacto", f"Nombre: {contacto['nombre']}\nTeléfono: {contacto['telefono']}")
        else:
            messagebox.showerror("Error", "No se encontró el contacto")

    def borrar_contacto(self):
        nombre = self.entry_nombre.get()
        contacto_existente = self.collection.find_one({"nombre": nombre, "usuario": self.nombre_usuario})
        if contacto_existente:
            self.collection.delete_one({"nombre": nombre, "usuario": self.nombre_usuario})
            messagebox.showinfo("Éxito", "Se ha borrado el contacto y su teléfono correspondiente")
        else:
            messagebox.showerror("Error", "El contacto no existe")

    def modificar_telefono(self):
        nombre = self.entry_nombre.get()
        nuevo_telefono = self.entry_telefono.get()
        contacto_existente = self.collection.find_one({"nombre": nombre, "usuario": self.nombre_usuario})
        if contacto_existente:
            self.collection.update_one({"nombre": nombre, "usuario": self.nombre_usuario}, {"$set": {"telefono": nuevo_telefono}})
            messagebox.showinfo("Éxito", "Se ha modificado el teléfono del contacto")
        else:
            messagebox.showerror("Error", "El contacto no existe")

    def cerrar_agenda(self):
        self.ventana.destroy()

if __name__ == "__main__":
    ventana_inicio = tk.Tk()
    app = VentanaInicio(ventana_inicio)
    ventana_inicio.mainloop()

