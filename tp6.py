class personajes:
    def _init_(self, nombre, estatura, edad, genero, especie, planeta, episodio):
        self.nombre = nombre
        self.estatura = estatura
        self.edad = edad
        self.genero = genero
        self.especie = especie
        self.planeta = planeta
        self.episodio = episodio
    
    def _str_(self):
        return f'{self.nombre} - {self.estatura} - {self.edad} - {self.genero} - {self.especie} - {self.planeta} - {self.episodio}'
    
J1 = personajes('a', 68, 1, 'femenino', 'droide', 'a',  [1, 2, 3, 4, 5, 6])
J2 = personajes('b', 69, 2, 'femenino', 'droide', 'b', [5])
J3 = personajes('Han solo', 72, 852, 'masculino', 'droide', 'b', [6] )
J4 = personajes('Darth Vader', 71, 851, 'masculino', 'droide', 'b', [9] )
J5 = personajes('Chewbacca', 2.0, 70, 'masculino', 'humana', 'Alderaan', [10] )

lista = Lista()

lista.insert(J1, 'nombre')
lista.insert(J2, 'nombre')
lista.insert(J3, 'nombre')
lista.insert(J4, 'nombre')
lista.insert(J5, 'nombre')
lista.barrido()
print()

#1

for i in range(lista.size()):
    if lista.get_element_by_index(i).genero == 'femenino':
        print ('Los personajes femeninos son: ', lista.get_element_by_index(i))
print()
    
#2
episodio = [1, 2, 3, 4, 5, 6]
for i in range(lista.size()):
    if (lista.get_element_by_index(i).episodio == episodio) and (lista.get_element_by_index(i).especie == 'droide'):
        print ('Droide: ', lista.get_element_by_index(i))
print()

#3
for i in range(lista.size()):
    if lista.get_element_by_index(i).nombre == 'Darth Vader':
        print ('La información de Darth Vader es: ', lista.get_element_by_index(i))
    elif lista.get_element_by_index(i).nombre == 'Han solo':
        print ('La información de Han solo es: ', lista.get_element_by_index(i))
print()

#4
episodios = ['4', '5', '6', '7']
for i in range(lista.size()):
    if lista.get_element_by_index(i).episodio in episodios:
        print ('El personaje aparece desde el episodio 4 al 7: ', lista.get_element_by_index(i).nombre)
print()

#5
mayor = 0
posicion = -1
for i in range(lista.size()):
    if lista.get_element_by_index(i).edad > 850:
        print (lista.get_element_by_index(i).nombre, ' tiene más de 850 años.')
        if lista.get_element_by_index (i).edad > mayor:
            mayor = lista.get_element_by_index(i).edad
            posicion = i
if posicion != -1:
    print ('El mayor es: ', lista.get_element_by_index(posicion).nombre)
else:
    print ('No hay nadie mayor de 850 años.')
print()

#6
episodiosDelete = [4, 5, 6]
pos = 0
for i in range(lista.size()):
    control = True
    espisodespresonaje = lista.get_element_by_index(pos).episodio
    for episode in episodiosDelete:
        if episode not in espisodespresonaje:
            control = False
            break
    if control:
        lista.delete(lista.get_element_by_index(pos).nombre, 'nombre')
        pos -= 1
    pos += 1
lista.barrido()
print()

#7
for i in range (lista.size()):
    if (lista.get_element_by_index(i).planeta == 'Alderaan') and (lista.get_element_by_index(i).especie == 'humana'):
        print (lista.get_element_by_index(i), 'Es humano y habita en el planeta Alderaan.')
print()

#8
for i in range (lista.size()):
    if lista.get_element_by_index(i).estatura < 70:
        print (lista.get_element_by_index(i), ' es más alto que 70 centimetros.')
print ()

#9
buscado = lista.search('Chewbacca', 'nombre')
if buscado != -1:
    print ('Chewbacca aparece en el capítulo: ', lista.get_element_by_index(buscado).episodio, ' y el resto de su información es: ', lista.get_element_by_index(buscado))
else:
    print ('Chewbacca no se encuentra en la lista.')
print()