from grafo import Grafo

from random import randint

grafo = Grafo()

grafo.insert_vertice('Luke Skywalker')
grafo.insert_vertice('Darth Vader')
grafo.insert_vertice('Kylo Ren')
grafo.insert_vertice('Leia')
grafo.insert_vertice('Boba Fett')
grafo.insert_vertice('C-3PO')
grafo.insert_vertice('Rey')
grafo.insert_vertice('Chewbacca')
grafo.insert_vertice('Han Solo')
grafo.insert_vertice('R2-D2')
grafo.insert_vertice('BB-8')
grafo.insert_vertice('Yoda')

grafo.insert_arist('Luke Skywalker', 'Darth Vader', randint(1, 7))
grafo.insert_arist('Luke Skywalker', 'Kylo Ren', randint(1, 7))
grafo.insert_arist('Luke Skywalker', 'Leia', randint(1, 7))

grafo.insert_arist('Darth Vader', 'Kylo Ren', randint(1, 7))
grafo.insert_arist('Darth Vader', 'Leia', randint(1, 7))

grafo.insert_arist('Kylo Ren', 'Leia', randint(1, 7))

grafo.insert_arist('Leia', 'Boba Fett', randint(1, 7))
grafo.insert_arist('Leia', 'C-3PO', randint(1, 7))
grafo.insert_arist('Leia', 'Rey', randint(1, 7))

grafo.insert_arist('Boba Fett', 'C-3PO', randint(1, 7))
grafo.insert_arist('Boba Fett', 'Rey', randint(1, 7))

grafo.insert_arist('C-3PO', 'Rey', randint(1, 7))

grafo.insert_arist('Chewbacca', 'Han Solo', randint(1, 7))

grafo.insert_arist('R2-D2', 'BB-8', randint(1, 7))

grafo.insert_arist('Yoda', 'Chewbacca', randint(1, 7))

arbol_expansion_minimo = grafo.kruskal()
print('Árbol de Expansión Mínimo:')
for arista in arbol_expansion_minimo:
    print(arista)

contiene_yoda = False
for arista in arbol_expansion_minimo:
    if 'Yoda' in arista:
        contiene_yoda = True
        break
if contiene_yoda:
    print('El árbol de expansión mínimo contiene a Yoda.')
else:
    print('El árbol de expansión mínimo no contiene a Yoda.')

max_peso, personajes_max_episodios = grafo.max_episodios_compartidos()

if max_peso > 0:
    print(f'El número máximo de episodios compartidos es {max_peso}, y los personajes son:')
    for i in range(0, len(personajes_max_episodios), 2):
        personaje1 = personajes_max_episodios[i]
        personaje2 = personajes_max_episodios[i + 1]
        print(f'{personaje1} y {personaje2}')
else:
    print('No se encontraron personajes que compartan episodios.')
   
#punto extra del recuperatorio

pri = 'yoda'
ult = 'rey'
principio = grafo.search_vertice(pri)
final = grafo.search_vertice(ult)
camino_mas_corto = None
if(principio is not None and final is not None):
    if(grafo.has_path(pri, ult)):
        camino_mas_corto = grafo.dijkstra(pri, ult)
        fin = ult
        while camino_mas_corto.size() > 0:
            value = camino_mas_corto.pop()
            if fin == value[0]:
                print(value[0], value[1])
                fin = value [2]

