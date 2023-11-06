class GrafoStarWars:
    def __init__(self):
        self.grafo = {}

    def agregar_personaje(self, personaje):
        if personaje not in self.grafo:
            self.grafo[personaje] = []

    def agregar_relacion(self, personaje1, personaje2, episodios_juntos):
        if personaje1 in self.grafo and personaje2 in self.grafo:
            self.grafo[personaje1].append((personaje2, episodios_juntos))
            self.grafo[personaje2].append((personaje1, episodios_juntos))

    def obtener_relaciones(self, personaje):
        if personaje in self.grafo:
            return self.grafo[personaje]
        else:
            return []

    def obtener_aristas(self):
        aristas = []
        for personaje, relaciones in self.grafo.items():
            for relacion in relaciones:
                otro_personaje, episodios = relacion
                aristas.append((personaje, otro_personaje, episodios))
        return aristas

def encontrar_mst_yoda(grafo):
    aristas = grafo.obtener_aristas()
    aristas.sort(key=lambda x: x[2])  

    mst = []
    total_episodios = 0

    for arista in aristas:
        personaje1, personaje2, episodios = arista
        if personaje1 not in mst or personaje2 not in mst:
            mst.append(personaje1)
            mst.append(personaje2)
            total_episodios += episodios

    return mst, total_episodios

def encontrar_max_episodios_compartidos(grafo):
    max_episodios = 0
    personajes_con_max_episodios = []

    for personaje, relaciones in grafo.grafo.items():
        for relacion in relaciones:
            otro_personaje, episodios = relacion
            if episodios > max_episodios:
                max_episodios = episodios
                personajes_con_max_episodios = [(personaje, otro_personaje)]
            elif episodios == max_episodios:
                personajes_con_max_episodios.append((personaje, otro_personaje))

    return max_episodios, personajes_con_max_episodios

grafo = GrafoStarWars()

personajes = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"]
for personaje in personajes:
    grafo.agregar_personaje(personaje)

grafo.agregar_relacion("Luke Skywalker", "Darth Vader", 6)
grafo.agregar_relacion("Luke Skywalker", "Yoda", 5)
grafo.agregar_relacion("Han Solo", "Chewbacca", 4)
grafo.agregar_relacion("Han Solo", "Leia", 6)
grafo.agregar_relacion("R2-D2", "C-3PO", 7)
grafo.agregar_relacion("Rey", "BB-8", 3)
grafo.agregar_relacion("Kylo Ren", "Darth Vader", 4)
grafo.agregar_relacion("Boba Fett", "Darth Vader", 2)

for personaje, relaciones in grafo.grafo.items():
    print(f"Relaciones de {personaje}:")
    for relacion in relaciones:
        otro_personaje, episodios = relacion
        print(f"- {otro_personaje} ({episodios} episodios juntos)")
mst, total_episodios = encontrar_mst_yoda(grafo)

print("Personajes en el MST:")
for personaje in mst:
    print(personaje)

if "Yoda" in mst:
    print("El MST contiene a Yoda.")
else:
    print("El MST no contiene a Yoda.")
max_episodios, personajes_con_max_episodios = encontrar_max_episodios_compartidos(grafo)

print(f"Número máximo de episodios compartidos: {max_episodios}")
print("Personajes que comparten este número de episodios:")
for personaje1, personaje2 in personajes_con_max_episodios:
    print(f"{personaje1} y {personaje2}")