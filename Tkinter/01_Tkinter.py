import tkinter                                          #importamos la libreria

principal = tkinter.Tk()                                #creamos el gestor de ventana

texto = tkinter.Label(principal, text="Hola Tkinter")   #Label nos permite crear una etiqueta de texto

texto.pack()                                            #que luego empaquetamos en la ventana

principal.mainloop()                                    #mainloop inicializa la ventana y la mantiene en bucle recibiendo inputs (hasta que el usuario salga)


