from tabulate import tabulate
import os

liga= {}
fechas={
    '1':{},
    '2':{},
    '3':{},
    '4':{},
    '5':{},
    '6':{},
    '7':{},
    '8':{},
    '9':{},
    '10':{},
    '11':{},
    '12':{}
}

def mayorpartidos():
    os.system('cls')
    titulo="""
++++++++++++++++++++++++++++++++++++++++++
+ ***  EQUIPO QUE MAS PARTIDOS GANO  *** +
+ ***              EN                *** +
+ ***      LA LIGA BETPLAY 2024      *** + 
++++++++++++++++++++++++++++++++++++++++++
"""
    print(titulo)
    totalpartidos=0
    nombre=''
    for i in liga:
        if liga[i]['PG']>totalpartidos:
            totalpartidos=liga[i]['PG']
            nombre=liga[i]['nombre']
    print(f'El equipo que gano mas partidos en la liga es {nombre} con {totalpartidos} partidos.\n')


def mayorgoles():
    os.system('cls')
    titulo=          """
            +++++++++++++++++++++++++++++
            **  GOLEADOR DE LA LIGA *** +
            **     BETPLAY 2024     *** + 
            +++++++++++++++++++++++++++++
            """
    print(titulo)
    totalGoles=0
    nombre=''
    for i in liga:
        if liga[i]['GF']>totalGoles:
            totalGoles=liga[i]['GF']
            nombre=liga[i]['nombre']
    print(f'El equipo goleador de la liga es {nombre} con {totalGoles} goles.')
        
    

def mayorPuntos():
    os.system('cls')
    titulo="""
+++++++++++++++++++++++++++++++++
+  ***  GANADOR DE LA LIGA ***  +
+  ***     BETPLAY 2024    ***  + 
+++++++++++++++++++++++++++++++++
"""
    print(titulo)
    totalPunto=0
    nombre=''
    for i in liga:
        if liga[i]['TP']>totalPunto:
            totalPunto=liga[i]['TP']
            nombre=liga[i]['nombre']
    print(f'El equipo ganador de la liga es {nombre} con {totalPunto} puntos.\n')
        

def golestotal():
    os.system('cls')
    titulo="""
+++++++++++++++++++++++++
+  *** TOTAL GOLES ***  + 
+++++++++++++++++++++++++
"""
    print(titulo)
    totalGol=0
    for i in liga:
        totalGol+=liga[i]['GF']
    print(f'Este es el total de goles {totalGol}.\n')
        

def Promedio():
    os.system('cls')
    titulo="""
+++++++++++++++++++++++
+  *** PROMEDIOS ***  + 
+++++++++++++++++++++++
"""
    print(titulo)
    totalGol=0
    totalpartidos=0
    for i in liga:
        totalGol+=liga[i]['GF']
    for i in fechas:
        totalpartidos+=len(fechas[i])
    prom=(totalGol/totalpartidos)
    print(f'Este es el promedio de goles por partido {prom}\n')
    
        
def agregarEquipo():
    os.system('cls')
    titulo="""
---------------------------
-  * LIGA BETPLAY 2024 *  -
---------------------------
"""
    print(titulo)
    bandera=True
    while bandera:
        equipo = input('Ingrese nombre del equipo:\n\n').upper()
        equipos={
        'nombre': equipo,
        'PJ':0,
        'PG':0,
        'PP':0, 
        'PE':0,
        'GF':0,
        'GC':0,
        'TP':0,
    }
        liga.update({str(len(liga)+1).zfill(3):equipos})

        bandera=bool(input('Desea ingresar otro equipo? enter(no) X(si)\n'))


def fechasJuego():
    os.system('cls')
    titulo="""
------------------------------------
-  *** FECHAS DE LOS PARTIDOS ***  -
------------------------------------
"""
    print(titulo)
    bandera= True
    while bandera:
        fecha = input('Ingrese la fecha del partido:\n\n')
        for i in liga:
            for j in liga[i]:
                if j=='nombre':
                    print(f'{i}. {liga[i][j]}\n')
                    break
                os.system('cls')        
        equipoLocal=str(input('Ingrese el # del equipo que desea para local:\n\n'))
        equipovisitante=str(input('Ingrese el # del equipo que desea para visitante:\n\n'))
        local=liga[equipoLocal]['nombre']
        visitante=liga[equipovisitante]['nombre']
        os.system('cls')
        print(f"{local} vs {visitante}\n")
        golesLocal=int(input('Ingrese el # de goles que desea para el equipo local\n'))
        golesVisitante=int(input('Ingrese el # de goles que desea para el equipo visitante\n'))

        partido={'local':{'nombre':liga[equipoLocal]['nombre'],'goles':golesLocal},'visitante':{'nombre':liga[equipovisitante]['nombre'],'goles':golesVisitante}}
        fechas[str(fecha)].update({fecha:{str(len(fechas[str(fecha)])+1).zfill(2):partido}})

        liga[equipoLocal]['PJ']+=1
        liga[equipoLocal]['GF']+=golesLocal
        liga[equipoLocal]['GC']+=golesVisitante

        liga[equipovisitante]['PJ']+=1
        liga[equipovisitante]['GF']+=golesVisitante
        liga[equipovisitante]['GC']+=golesVisitante

        if golesLocal>golesVisitante:
            liga[equipoLocal]['PG']+=1
            liga[equipoLocal]['TP']+=3
            liga[equipovisitante]['PP']+=1
        elif golesVisitante>golesLocal:
            liga[equipovisitante]['PG']+=1
            liga[equipovisitante]['TP']+=3
            liga[equipoLocal]['PP']+=1
        else: 
            liga[equipovisitante]['PE']+=1
            liga[equipovisitante]['TP']+=1
            liga[equipoLocal]['PE']+=1
            liga[equipoLocal]['TP']+=1
        
        bandera=bool(input('Desea ingresar otra fecha? enter(no) X(si)\n'))
        


      