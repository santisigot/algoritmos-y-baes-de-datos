personajes_mcu = [
    ("Iron Man", 10),
    ("Viuda Negra", 8),
    ("Thor", 7),
    ("Rocket Raccoon", 6),
    ("Groot", 5),
    ("Hulk", 4),
    ("Doctor Strange", 3),
    ("Capitán América", 6),
    ("Ant-Man", 4)
]


posicion_rocket = None
posicion_groot = None

for i, personaje in enumerate(personajes_mcu, start=1):
    if personaje[0] == "Rocket Raccoon":
        posicion_rocket = i
    elif personaje[0] == "Groot":
        posicion_groot = i

print("Posición de Rocket Raccoon:", posicion_rocket)
print("Posición de Groot:", posicion_groot)

personajes_mas_de_5 = [(personaje[0], personaje[1]) for personaje in personajes_mcu if personaje[1] > 5]
print("Personajes que participaron en más de 5 películas:", personajes_mas_de_5)

peliculas_viuda_negra = next(personaje[1] for personaje in personajes_mcu if personaje[0] == "Viuda Negra")
print("Número de películas en las que participó la Viuda Negra:", peliculas_viuda_negra)

iniciales = ["C", "D", "G"]
personajes_iniciales = [personaje[0] for personaje in personajes_mcu if personaje[0][0] in iniciales]
print("Personajes cuyos nombres empiezan con C, D o G:", personajes_iniciales)