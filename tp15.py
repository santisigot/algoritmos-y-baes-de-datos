class Pokemon():
    
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f'{self.nombre} - Nivel: {self.nivel} - Tipo: {self.tipo} - Subtipo: {self.subtipo}'

class EntrenadorPokemon():

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas, pokemons):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = pokemons

    def __str__(self):
        return f'Entrenador: {self.nombre}\nTorneos Ganados: {self.torneos_ganados}\nBatallas Perdidas: {self.batallas_perdidas}\nBatallas Ganadas: {self.batallas_ganadas}\nPokémons:\n{", ".join([str(pokemon) for pokemon in self.pokemons])}'

class Lista():

    def __init__(self):
        self.__elements = []

    def cantidad_pokemons_entrenador(self, nombre_entrenador):
        for entrenador, _ in self.__elements:
            if entrenador.nombre == nombre_entrenador:
                return len(entrenador.pokemons)
        return 0

    def entrenadores_mas_de_tres_torneos_ganados(self):
        entrenadores = []
        for entrenador, _ in self.__elements:
            if entrenador.torneos_ganados > 3:
                entrenadores.append(entrenador.nombre)
        return entrenadores

    def pokemon_de_mayor_nivel_entrenador_con_mas_torneos(self):
        entrenador_mas_torneos = None
        torneos_mas_ganados = -1
        for entrenador, _ in self.__elements:
            if entrenador.torneos_ganados > torneos_mas_ganados:
                entrenador_mas_torneos = entrenador
                torneos_mas_ganados = entrenador.torneos_ganados
        
        if entrenador_mas_torneos is not None:
            mayor_nivel = -1
            pokemon_mayor_nivel = None
            for pokemon in entrenador_mas_torneos.pokemons:
                if pokemon.nivel > mayor_nivel:
                    mayor_nivel = pokemon.nivel
                    pokemon_mayor_nivel = pokemon
            return pokemon_mayor_nivel
        return None

    def mostrar_datos_entrenador_y_pokemons(self, nombre_entrenador):
        for entrenador, _ in self.__elements:
            if entrenador.nombre == nombre_entrenador:
                print(entrenador)

    def entrenadores_porcentaje_batallas_ganadas_mayor_79(self):
        entrenadores = []
        for entrenador, _ in self.__elements:
            porcentaje_ganadas = (entrenador.batallas_ganadas / (entrenador.batallas_ganadas + entrenador.batallas_perdidas)) * 100
            if porcentaje_ganadas > 79:
                entrenadores.append(entrenador.nombre)
        return entrenadores

    def entrenadores_tipos_pokemon_fuego_planta_agua_volador(self):
        entrenadores = []
        for entrenador, _ in self.__elements:
            tiene_fuego_planta = False
            tiene_agua_volador = False
            for pokemon in entrenador.pokemons:
                if (pokemon.tipo == 'fuego' or pokemon.tipo == 'planta') or (pokemon.tipo == 'agua' and pokemon.subtipo == 'volador'):
                    tiene_fuego_planta = True
                    tiene_agua_volador = True
                    break
            if tiene_fuego_planta or tiene_agua_volador:
                entrenadores.append(entrenador.nombre)
        return entrenadores

    def promedio_nivel_pokemons_entrenador(self, nombre_entrenador):
        for entrenador, _ in self.__elements:
            if entrenador.nombre == nombre_entrenador:
                total_nivel = sum([pokemon.nivel for pokemon in entrenador.pokemons])
                return total_nivel / len(entrenador.pokemons)
        return 0

    def entrenadores_con_pokemon(self, nombre_pokemon):
        entrenadores = []
        for entrenador, _ in self.__elements:
            for pokemon in entrenador.pokemons:
                if pokemon.nombre == nombre_pokemon:
                    entrenadores.append(entrenador.nombre)
                    break
        return entrenadores

    def entrenadores_con_pokemons_repetidos(self):
        entrenadores = []
        for entrenador, _ in self.__elements:
            nombres_pokemons = [pokemon.nombre for pokemon in entrenador.pokemons]
            if len(nombres_pokemons) != len(set(nombres_pokemons)):
                entrenadores.append(entrenador.nombre)
        return entrenadores

    def entrenadores_con_pokemons_especificos(self, nombres_pokemons):
        entrenadores = []
        for entrenador, _ in self.__elements:
            for pokemon in entrenador.pokemons:
                if pokemon.nombre in nombres_pokemons:
                    entrenadores.append(entrenador.nombre)
                    break
        return entrenadores

    def entrenador_tiene_pokemon(self, nombre_entrenador, nombre_pokemon):
        for entrenador, _ in self.__elements:
            if entrenador.nombre == nombre_entrenador:
                for pokemon in entrenador.pokemons:
                    if pokemon.nombre == nombre_pokemon:
                        return entrenador, pokemon
        return None, None


pokemon1 = Pokemon('Charizard', 50, 'fuego', 'volador')
pokemon2 = Pokemon('Venusaur', 52, 'planta', 'veneno')
pokemon3 = Pokemon('Blastoise', 48, 'agua', 'agua')
pokemon4 = Pokemon('Pidgeot', 45, 'normal', 'volador')
pokemon5 = Pokemon('Tyrantrum', 55, 'dragón', 'roca')


entrenador1 = EntrenadorPokemon('Ash', 5, 10, 15, [pokemon1, pokemon2, pokemon3])
entrenador2 = EntrenadorPokemon('Misty', 3, 8, 12, [pokemon4, pokemon5])
entrenador3 = EntrenadorPokemon('Brock', 4, 12, 10, [pokemon1, pokemon2])

lista_entrenadores = Lista()
lista_entrenadores.insert(entrenador1, 'nombre')
lista_entrenadores.insert(entrenador2, 'nombre')
lista_entrenadores.insert(entrenador3, 'nombre')

# a
cantidad_pokemons = lista_entrenadores.cantidad_pokemons_entrenador('Ash')
print(f'Ash tiene {cantidad_pokemons} Pokémons.')

# b
entrenadores_mas_de_tres_torneos = lista_entrenadores.entrenadores_mas_de_tres_torneos_ganados()
print('Entrenadores con más de tres torneos ganados:', entrenadores_mas_de_tres_torneos)

# c
pokemon_mayor_nivel = lista_entrenadores.pokemon_de_mayor_nivel_entrenador_con_mas_torneos()
if pokemon_mayor_nivel:
    print(f'El Pokémon de mayor nivel del entrenador con más torneos ganados es: {pokemon_mayor_nivel.nombre}')
else:
    print('No se encontró ningún entrenador con torneos ganados.')

# d
lista_entrenadores.mostrar_datos_entrenador_y_pokemons('Ash')

# e
entrenadores_porcentaje_ganadas_mayor_79 = lista_entrenadores.entrenadores_porcentaje_batallas_ganadas_mayor_79()
print('Entrenadores con porcentaje de batallas ganadas mayor al 79 %:', entrenadores_porcentaje_ganadas_mayor_79)

# f
entrenadores_tipos_especificos = lista_entrenadores.entrenadores_tipos_pokemon_fuego_planta_agua_volador()
print('Entrenadores con Pokémons de tipo fuego/planta o agua/volador:', entrenadores_tipos_especificos)

# g
promedio_nivel = lista_entrenadores.promedio_nivel_pokemons_entrenador('Ash')
print(f'El promedio de nivel de los Pokémons de Ash es: {promedio_nivel}')

# h
cantidad_entrenadores_charizard = len(lista_entrenadores.entrenadores_con_pokemon('Charizard'))
print(f'Cantidad de entrenadores con Charizard: {cantidad_entrenadores_charizard}')

# i
entrenadores_pokemons_repetidos = lista_entrenadores.entrenadores_con_pokemons_repetidos()
print('Entrenadores con Pokémons repetidos:', entrenadores_pokemons_repetidos)

# j
pokemons_buscados = ['Tyrantrum', 'Terrakion', 'Wingull']
entrenadores_con_pokemons_buscados = lista_entrenadores.entrenadores_con_pokemons_especificos(pokemons_buscados)
print(f'Entrenadores con uno de los siguientes Pokémons: {", ".join(pokemons_buscados)}:', entrenadores_con_pokemons_buscados)

# k
nombre_entrenador = 'Ash'
nombre_pokemon = 'Charizard'
entrenador, pokemon = lista_entrenadores.entrenador_tiene_pokemon(nombre_entrenador, nombre_pokemon)
if entrenador and pokemon:
    print(f'El entrenador {entrenador.nombre} tiene al Pokémon {pokemon.nombre}.')
elif entrenador:
    print(f'El entrenador {entrenador.nombre} no tiene al Pokémon {nombre_pokemon}.')
else:
    print(f'El entrenador {nombre_entrenador} no se encontró en la lista.')