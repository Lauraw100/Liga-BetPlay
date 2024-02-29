import modulos.Registros as Re
import os

op="0"
def Menu():
    os.system('cls')
    titulo="""
    ----------------------
    -  *** Reportes ***  - 
    ----------------------
    """
    bandera= True
    global op 
    while op!="F":
        os.system('cls')
        print(titulo)
        print( "A. Nombre del equipo que más goles anotó: \n",
               "B. Nombre del equipo que más puntos tiene: \n",
               "C. Nombre del equipo que más partidos ganó: \n",
               "D. Total de goles anotados por todos los equipos:\n",
               "E. Promedio de goles anotados en el torneo: \n",
               "F. Regresar al menú principal: \n")
        op=input()
        op=op.upper()
        if op == "A":
            Re.mayorgoles()
        elif op == "B":
            Re.mayorPuntos()      
        elif op == "C":
            Re.mayorpartidos()
        elif op == "D":
            Re.golestotal()
        elif op == "E":
            Re.Promedio()
        elif op =="F":
            print("adios")
        else:
            print('Valor no encontrado\n')
        bandera=bool(input('Desea revisar otro reporte? enter(no) X(si)\n'))
        