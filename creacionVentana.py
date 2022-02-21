from tkinter import Frame 

class MiVentana(Frame): 
    # Cada widget tiene un primer parámetro de constructor 
    # que es su widget 'maestro', es decir, el que lo 
    # contiene. Si no se especifica este parámetro, y si el 
    # widget en cuestión es un frame, entonces este estará 
    # contenido automáticamente en la ventana de la aplicación. 
    def __init __ (self, master = None):
       # Llamamos al constructor de la clase madre 
       # de MiVentana, es decir, Frame. Además del widget maestro, 
       # especificamos las dimensiones de la ventana, es decir, un 
       # ancho de 320 píxeles y un alto de 240. 
       super(MiVentana, self).__init__(master, width=320, 
                                       height=240) 
 
       # La ventana que contiene el frame está referenciada por 
       # el atributo master. Entonces es él el que debe usar 
       # para modificar el título de la ventana mostrada 
       # por el sistema operativo. 
       self.master.title ("Mi Aplicación gráfica") 
 
       # pack() permite consolidar la geometría del frame 
       # en la ventana. Sin esta llamada, el dimensionamiento 
       # dado en el constructor de Frame no tendría lugar. 
       self.pack() 
 
mi_ventana = MiVentana() 
mi_ventana.mainloop()