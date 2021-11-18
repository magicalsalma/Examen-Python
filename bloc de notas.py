
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from os import *
from os import mkdir
from shutil import rmtree

try:
    import tkinter as tk
except:
    import tkinter as tk

#Funciones
def copiar():
    editor.clipboard_clear()
    editor.clipboard_append(editor.selection_get())
def pegar():
    editor.insert(INSERT, editor.clipboard_get())
def cortar():
    editor.clipboard_clear()
    editor.clipboard_append(editor.selection_get())
    editor.delete("sel.first", "sel.last")
def deshacer():
    editor.edit_undo()
def nuevo():
    editor.delete(1.0,END)
def abrir():
    documento = askopenfile(filetypes=[("Archivo de texto","*.txt")])
    if documento != None:
        editor.insert(1.0, documento.read())
def guardar():
    documento = asksaveasfile(filetypes=[("Archivo de texto","*.txt")])
    print(documento.write(editor.get(1.0, END)))
def acerca():
    messagebox.showinfo("About Notepad", "This Notepad was developed by Salma Gómez for the Junior Year Exam.")
def amonos(): 
    ventana.destroy()
def crearcarpeta():
    mkdir("Nueva carpeta")
    mkdir(r"C:\Users\Laboratorio Inglés\Desktop\Programming Salma\Nueva carpeta")
def eliminarcarpeta(): 
    rmtree("Nueva carpeta")
def eliminararchivo():
    remove("documento") 

#Lo visual xddd

if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.configure(bg="blue")
    menubar = Menu(ventana)
    archivo = Menu(menubar, tearoff=0, bg="pink2")
    archivo.add_command(label="Crear Archivo", command=nuevo)
    archivo.add_command(label="Ver Archivo", command=abrir)
    archivo.add_command(label="Guardar Archivo ", command=guardar)
    archivo.add_command(label="Eliminar Archivo    ", command=eliminararchivo)
    archivo.add_command(label="Salir    ", command=amonos)
    menubar.add_cascade(label="Archivo", menu=archivo)

    editar = Menu(menubar, tearoff=0, bg="pink2")
    editar.add_command(label="Deshacer", command=deshacer)
    editar.add_separator()
    editar.add_command(label="Copiar", command=copiar)
    editar.add_command(label="Pegar", command=pegar)
    editar.add_command(label="Cortar", command=cortar)
    menubar.add_cascade(label="Modificar Archivo", menu=editar)
    
    carpeta = Menu(menubar, tearoff=0, bg="pink2")
    carpeta.add_command(label="Crear Carpeta", command=crearcarpeta)
    carpeta.add_command(label="Eliminar Carpeta", command=eliminarcarpeta)

    carpeta.add_separator()
    menubar.add_cascade(label="Carpeta", menu=carpeta)

    ayuda = Menu(menubar, tearoff=0, bg="pink2")
    ayuda.add_command(label="Acerca de Bloc de notas ", command=acerca)
    menubar.add_cascade(label="Ayuda", menu=ayuda)

    editor = Text(ventana, undo="true", bg="pink1")
    editor.pack(side=TOP, fill=BOTH, expand=1)

    ventana.title("Notepad :) ")
    ventana.geometry("695x424")
    ventana.config(menu=menubar)
    
    ventana.mainloop()

