from arbol_binario import BinaryTree

'''1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:
a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
b) mostrar todos los datos de un Pokémon a partir de su número y nombre para este
último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres;
c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
además un listado por nivel por nombre;
e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;
f) Determina cuantos Pokémons hay de tipo eléctrico y acero.'''

pokemon_data = [
    {'name': 'Pikachu', 'number': 25, 'type': ['Electric']},
    {'name': 'Bulbasaur', 'number': 1, 'type': ['Grass', 'Poison']},
    {'name': 'Charizard', 'number': 6, 'type': ['Fire', 'Flier']},
    {'name': 'Jolteon', 'number': 135, 'type': ['Electric']},
    {'name': 'Lycanroc', 'number': 745, 'type': ['Stone']},
    {'name': 'Tyrantrum', 'number': 697, 'type': ['Stone', 'Dragon']},
    {'name': 'Steelix', 'number': 208, 'type': ['steel']}
]

name_tree = BinaryTree()
number_tree = BinaryTree()
type_tree = BinaryTree()

for pokemon in pokemon_data:
    name_tree.insert_node(pokemon['name'], {'number': pokemon['number'],'type': pokemon['type']})
    number_tree.insert_node(pokemon['name'], {'number': pokemon['number'],'type': pokemon['type']})
    type_tree.insert_node(pokemon['name'], {'number': pokemon['number'],'type': pokemon['type']})

number = 25
number_tree.inorden(number)
name = 'Bul'
name_tree.search_by_coincidence(name)
type = 'Electric'
type_tree.inorden(type)

def listar_nombres_por_tipo(self, root, tipo):
    if root is not None:
        if tipo in root.value['type']:
            print(root.value['name'])
        self.listar_nombres_por_tipo(root.left, tipo)
        self.listar_nombres_por_tipo(root.right, tipo)

tipos_a_buscar = ["water","Fire", "plant","Electric"]
print("Nombres de Pokémon de tipo agua:")
type_tree.listar_nombres_por_tipo(type_tree.root, tipos_a_buscar)

print("Listado de Pokémon en orden ascendente por numero:")
number_tree.inorden()
print("\nListado de Pokémon en orden ascendente por nombre:")
name_tree.inorden()
print("Listado de Pokémon por nivel nombre")
name_tree.by_level()

print("Datos de Pokémon Jolteon:")
name_tree.search_pokemon_by_name('Jolteon')
print("\nDatos de Pokémon Lycanroc:")
name_tree.search_pokemon_by_name('Lycanroc')
print("\nDatos de Pokémon Tyrantrum:")
name_tree.search_pokemon_by_name('Tyrantrum')

print(f"Total de Pokémon de tipo 'Eléctrico': {type_tree.contar('Eléctrico')}")
print(f"Total de Pokémon de tipo 'Acero': {type_tree.contar('Acero')}")
