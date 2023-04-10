import tkinter

def saludar():                                  #Definimos las funciones que vamos a usar
    texto['text'] = 'Hola Amigo'

def despedir():
    texto['text'] = 'Adios, Suerte!'

#ventana principal
principal = tkinter.Tk()

#Titulo de la ventana 
principal.wm_title("Testing Tkinter")

#texto que mostramos
texto = tkinter.Label(principal, text= "Hey!")

#botones 
#(En que ventana va, Que texto tiene, Que sucede si el usuario da click)
boton_saludar = tkinter.Button(principal, text= 'Hola', command = saludar)
boton_despedir = tkinter.Button(principal, text= 'Adios', command= despedir)

#empaquetamos
texto.pack()
boton_saludar.pack()
boton_despedir.pack()

#mainloop
principal.mainloop()
