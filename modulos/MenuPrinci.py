import os
import modulos.Registros as Re
import modulos.MenuRepor as Mr
from tabulate import tabulate
os.system("cls")

titulo =["LIGA BETPLAY 2024"]
op="0"
while op!="4":
    os.system("cls")
    print(tabulate(titulo,tablefmt="double_grid"))
    op=input("1. Registrar equipo.\n2. Registrar fecha.\n3. Reportes.\n4. Salir.\n\n")
    if op == "1":
        Re.agregarEquipo()
    elif op == "2":
        Re.fechasJuego()      
    elif op == "3":
        Mr.Menu()
    elif op == "4":
        print("Adios")    
    else:
        print("Valor no encontrado")