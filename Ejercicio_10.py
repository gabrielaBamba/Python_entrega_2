nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''
notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]
notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10]

def generar_diccionario(nombres,notas_1,notas_2):
    """Esta funcion recibe un texto y dos listas de enteros y genera un diccionario usando como clave los nombres 
    que obtiene del texto y como valor una tupla con las dos notas de cada alumno """
    nombres=nombres.replace("'","") 
    nombres=[nombre.strip() for nombre in nombres.split(",")] 

    alumnos={}
    for nombre,nota1,nota2 in zip(nombres,notas_1,notas_2):
        alumnos[nombre]=(nota1,nota2)
    return alumnos


def obtener_promedios(alumnos):
    """ esta funcion retorna una lista con el promedio de todos los alumnos a partir del diccionario generado en el inciso a"""
    prom=map(lambda x:(x[0]+ x[1])/2, alumnos.values())
    return list(prom)


def obtener_promedio_general(alumnos):
    """Retorna el promedio general de todos los alumnos"""
    prom=sum(map(lambda x:(x[0]+ x[1])/2, alumnos.values()))/len(alumnos)
    return prom

def prom_miximo(alumnos):
     """Retorna el nombre del alumno con el promedio mas alto y su promedio """
     key_max,value_max = max(alumnos.items(), key =lambda x: x[1][0] + x[1][1])
    
     return key_max,sum(value_max)/2


def nota_minima(alumnos):
    """Retorna el nombre del alumn con la nota mas baja y su nota"""
    key_min,value_min = min(alumnos.items(), key =lambda x: min(x[1]))
    print()
    return key_min,min(value_min)






alumnos=generar_diccionario(nombres,notas_1,notas_2)
print(alumnos)
print()
promedios=obtener_promedios(alumnos)
print(f"Los promedios de los alumnos son {promedios}")
print()
prom_general=obtener_promedio_general(alumnos)
print(f"El promedio general es  {prom_general}")
print()
alu_min,nota_min=nota_minima(alumnos)

print(f"El alumno con la nota minima es {alu_min}, con una nota de {nota_min} ")

alu_max,nota_max=prom_miximo(alumnos)

print(f"El alumno con el promedio mas alto  es {alu_max}, con un promedio de {nota_max} ")

 