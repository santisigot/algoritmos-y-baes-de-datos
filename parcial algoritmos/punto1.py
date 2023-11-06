pokemon_data = {
    "nombre": {},
    "numero": {},
    "tipo": {}
}

pokemon_list = [
    {"nombre": "Pikachu", "numero": 25, "tipo": ["Eléctrico"]},
    {"nombre": "Charizard", "numero": 6, "tipo": ["Fuego", "Volador"]},
    {"nombre": "bulbasaour", "numero": 1, "tipo": ["planta"]},
    {"nombre": "vaporeon", "numero": 134, "tipo": ["agua"]},
    {"nombre": "mewtwo", "numero": 150, "tipo": ["psiquico"]},
    {"nombre": "Jolteon", "numero": 135, "tipo": ["Eléctrico"]},
    {"nombre": "Lycanroc", "numero": 745, "tipo": ["roca"]},
]

for pokemon in pokemon_list:
    nombre = pokemon["nombre"]
    pokemon_data["nombre"][nombre] = pokemon
    numero = pokemon["numero"]
    pokemon_data["numero"][numero] = pokemon
    tipos = pokemon["tipo"]
    for tipo in tipos:
        if tipo not in pokemon_data["tipo"]:
            pokemon_data["tipo"][tipo] = []
        pokemon_data["tipo"][tipo].append(pokemon)
def buscar_pokemon_por_nombre(nombre):
    resultados = []
    for pokemon_nombre, pokemon_info in pokemon_data["nombre"].items():
        if nombre.lower() in pokemon_nombre.lower():
            resultados.append(pokemon_info)
    return resultados
def buscar_pokemon_por_tipo(tipo):
    if tipo in pokemon_data["tipo"]:
        return pokemon_data["tipo"][tipo]
    else:
        return []
def listar_pokemon_orden_numero():
    pokemon_por_numero = sorted(pokemon_data["numero"].values(), key=lambda x: x["numero"])
    
    print("Listado de Pokémon en orden ascendente por número:")
    for pokemon in pokemon_por_numero:
        print(f"{pokemon['numero']}: {pokemon['nombre']}")
def listar_pokemon_orden_nombre():
    pokemon_por_nombre = sorted(pokemon_data["nombre"].values(), key=lambda x: x["nombre"])
    
    print("Listado de Pokémon en orden ascendente por nombre:")
    for pokemon in pokemon_por_nombre:
        print(f"{pokemon['nombre']} ({pokemon['numero']})")
def listar_pokemon_por_tipo():
    tipos_pokemon = sorted(pokemon_data["tipo"].keys())
    print("Listado de Pokémon por tipo y nombre:")
    for tipo in tipos_pokemon:
        print(f"Tipo: {tipo}")
        for pokemon in pokemon_data["tipo"][tipo]:
            print(f"{pokemon['nombre']} ({pokemon['numero']})")
def contar_pokemon_por_tipo(tipo):
    if tipo in pokemon_data["tipo"]:
        return len(pokemon_data["tipo"][tipo])
    else:
        return 0
nombres_a_buscar = ["Jolteon", "Lycanroc", "Tyrantrum"]

tipos_a_contar = ["Eléctrico", "Acero"]

for nombre_pokemon in nombres_a_buscar:
    resultados_nombre = buscar_pokemon_por_nombre(nombre_pokemon)
    if resultados_nombre:
        print(f"Datos de Pokémon con nombre '{nombre_pokemon}':")
        for pokemon in resultados_nombre:
            print(f"Nombre: {pokemon['nombre']}")
            print(f"Número: {pokemon['numero']}")
            print(f"Tipo(s): {', '.join(pokemon['tipo'])}")
            print()  
    else:
        print(f"No se encontraron Pokémon con nombre '{nombre_pokemon}'")
for tipo_pokemon in tipos_a_contar:
    cantidad = contar_pokemon_por_tipo(tipo_pokemon)
    print(f"Cantidad de Pokémon de tipo '{tipo_pokemon}': {cantidad}")
listar_pokemon_orden_numero()
listar_pokemon_orden_nombre()
listar_pokemon_por_tipo()
