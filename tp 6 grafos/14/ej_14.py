from grafo import Grafo
from random import randint

print ("\nEJERCICIO 14:")
grafo = Grafo(dirigido=False)
print ("\nA")
grafo.insert_vertice("banioUno")
grafo.insert_vertice("banioDos")
grafo.insert_vertice("cochera")
grafo.insert_vertice("cocina")
grafo.insert_vertice("comedor")
grafo.insert_vertice("habitacionUno")
grafo.insert_vertice("habitacionDos")
grafo.insert_vertice("patio")
grafo.insert_vertice("salaDeEstar")
grafo.insert_vertice("terraza")
grafo.insert_vertice("quincho")
print ("Cargados")

print ("\nB:")
grafo.insert_arist("banioUno", "banioDos", randint(1, 30))
grafo.insert_arist("banioUno", "habitacionUno", randint(1, 15))
grafo.insert_arist("banioUno", "salaDeEstar", randint(1, 20))

grafo.insert_arist("banioDos", "habitacionDos", randint(1, 20))
grafo.insert_arist("banioDos", "terraza", randint(1, 10))

grafo.insert_arist("habitacionUno", "salaDeEstar", randint(1, 15))
grafo.insert_arist("habitacionUno", "habitacionDos", randint(1, 30))
grafo.insert_arist("habitacionUno", "comedor", randint(1, 20))
grafo.insert_arist("habitacionUno", "habitacionDos", randint(1, 30))

grafo.insert_arist("habitacionDos", "terraza", randint(1, 15))
grafo.insert_arist("habitacionDos", "quincho", randint(1, 35))
grafo.insert_arist("habitacionDos", "patio", randint(1, 30))

grafo.insert_arist("salaDeEstar", "patio", randint(1, 15))
grafo.insert_arist("patio", "quincho", randint(1, 10))
grafo.insert_arist("quincho", "cochera", randint(1, 30))
grafo.insert_arist("terraza", "cochera", randint(1, 30))
grafo.insert_arist("cochera", "comedor", randint(1, 20))
grafo.insert_arist("cocina", "patio", randint(1, 20))
grafo.insert_arist("cocina", "comedor", randint(1, 10))

print ("Cargados")

print ("\nC:")
number = []
for i in range(1, 31):
    number.append(str(i))

acu = 0
for arbol in grafo.kruskal():
    for nodo in arbol.split(';'):
        acu += int(nodo.split('-')[-1])

print(f"Se necesitarán {acu} metros de cables para conectar todos los ambientes.")

print("\nD: ")
ori = 'habitacionUno'
des = 'salaDeEstar'
origen = grafo.search_vertice(ori)
destino = grafo.search_vertice(des)
camino_mas_corto = None

if origen is not None and destino is not None:
    if grafo.has_path(ori, des):
        camino_mas_corto = grafo.dijkstra(ori, des)
        fin = des
        print("\nD: Camino más corto desde habitación 1 hasta sala de estar:")
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            print(f"{value[0]} - {value[1]} metros")
            fin = value[2]