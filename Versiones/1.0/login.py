import tkinter as tk
from tkinter import ttk
import sys
from tkinter import *
import os

# from Bicicletas import *

class login1:
    
    def login():

        print("Bienvenido")
        global window
        window = tk.Tk()
        window.title('Login')
        window.geometry('250x150')

        menu = Menu(window)

        item1 = Menu(menu)
        item2 = Menu(menu)
        item3 = Menu(menu)
 
        item1 = Menu(menu, tearoff=0)
        item1.add_command(label='Nuevo',command=login1.login)
        item1.add_command(label="Salir", command=window.destroy)

        item1.add_separator()

        item2.add_command(label='Editar')

        menu.add_cascade(label='Archivo', menu=item1)
        #menu.add_cascade(label='Configurar', menu=item2)
    
        window.config(menu=menu)


        window.configure(bg='black')
        label = tk.Label(window, text='Login', font=('Arial bold', 17),bg="black",fg="yellow")
        #label1 = tk.Label(window, text='', font=('Arial bold', 17),bg="black",fg="yellow")
        label.grid(column = 0, row = 0)
        #label1.grid(column = 2, row = 0)
        
        entrada1 = tk.Entry(window, width=10)
        entrada2 = tk.Entry(window, width=10)

        entrada1.grid(column = 1, row = 1)
        entrada2.grid(column = 1, row = 2)

        label_entrada1 = tk.Label(window, text = 'Usuario:', font=('Arial bold',12),bg="black",fg="red")
        label_entrada1.grid(column=0, row=1)
        label_entrada2 = tk.Label(window, text ='Contraseña: ', font=('Arial bold', 12),bg="black",fg="red")
        label_entrada2.grid(column=0, row=2)

        v1 = entrada1.get()
        v2 = entrada2.get()

        boton = tk.Button(window, text="Aceptar",command= login1.acceder)
        boton.grid(column = 1 , row = 3 ) 
        
        window.mainloop()

    def comprobar():
        print("ok")
        #leerArchivo()

    def acceder():
        #print("1")
        a = 0
        #entrada1.get()
        #entrada2.get()
        a = login1.leerArchivo()
        if a == 1:
            window.destroy()
        else:
            label_resultado = tk.Label(window, text='Error', font=('Arial bold',12) ,bg="black",fg="blue")
            label_resultado.grid(column = 0, row = 3)
        
    
    def leerArchivo():
        n = int(1)
        print("0")
        
        #archivo= os.getcwd()
        #print (archivo)
        archivo = "C:/Users/USUARIO/Desktop/login.txt"
        usuario = []
        contraseña = []
        existencia = os.path.isfile(archivo)
        print(existencia)
        if existencia == True:
            print("existe")
        else:
            print("no existe")
            login1.crear(archivo)
        with open(archivo, mode ="r", encoding= " utf-8" ) as fileReader:
            texto = fileReader.read()
            usuario1 = texto.split(";")
        while n in usuario1:
            usuario.append(n)
            contraseña.append(n+1)
            n += 1
        #print(usuario)
        print("1")
        return 0
        
        #login1.validar(v1,v2,usuario)
       
    def validar(v1,v2,usuario):
            e = 0
            if usuario == v1 :
                if usuario ==v2:
                    e = 0
    def crear(archivo):
        archivo1 = open(archivo, "w")
        archivo1.write("Usuario" + ";")
        archivo1.write("Contrasena"+";")
        archivo1.close()
log = login1()      
login1.login()