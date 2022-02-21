#----------------------------------------------   
# FUNCIONES   
#----------------------------------------------   

#Empleo de una tupla para la configuración de la aplicación   
#Nombre del robot, tiempo en minutos para limpiar un metro cuadrado   
parametros = ("robot_aspirador",2)   
   
# Empleo de diccionarios para crear las zonas   
zona1={"largo":500,"ancho":150}   
zona2={"largo":309,"ancho":480}   
zona3={"largo":101,"ancho":480}   
zona4={"largo":90,"ancho":220}  
   
# Empleo de una lista que permite guardar las zonas   
zonas = []   
zonas.append(zona1)   
zonas.append(zona2)   
zonas.append(zona3)   
zonas.append(zona4)   
def calculoDeLaSuperficieALimpiar(listaDeZonas):   
   superficieALimpiar = 0   
   for zona in zonas:   
       largo = zona.get("largo")/100   
       ancho = zona.get("ancho")/100   
       calculo = largo*ancho   
       print (str(largo)+" x "+str(ancho)+"= "+str(calculo))   
       superficieALimpiar = superficieALimpiar +calculo   
   return (superficieALimpiar)   
  