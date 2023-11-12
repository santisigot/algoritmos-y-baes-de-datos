class Pelicula:
    def __init__(self, titulo, estudio, año_estreno):
        self.titulo = titulo
        self.estudio = estudio
        self.año_estreno = año_estreno


class PilaPeliculas:
    def __init__(self):
        self.peliculas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def peliculas_estrenadas_en_2014(self):
        peliculas_2014 = [p.titulo for p in self.peliculas if p.año_estreno == 2014]
        return peliculas_2014

    def cantidad_peliculas_estrenadas_en_2018(self):
        peliculas_2018 = len([p for p in self.peliculas if p.año_estreno == 2018])
        return peliculas_2018

    def peliculas_marvel_estrenadas_en_2016(self):
        peliculas_marvel_2016 = [p.titulo for p in self.peliculas if p.estudio == 'Marvel Studios' and p.año_estreno == 2016]
        return peliculas_marvel_2016


pila_peliculas = PilaPeliculas()

pila_peliculas.agregar_pelicula(Pelicula('Como entrenar a tu Dragón 2', 'DreamWorks Animation', 2014))
pila_peliculas.agregar_pelicula(Pelicula('Transformers: la era de la extinción', 'Paramount Pictures', 2014))
pila_peliculas.agregar_pelicula(Pelicula('Pacific Rim: Uprising', 'Legendary Pictures', 2018))
pila_peliculas.agregar_pelicula(Pelicula('Captain America: Civil War', 'Marvel Studios', 2016))
pila_peliculas.agregar_pelicula(Pelicula('Doctor Strange', 'Marvel Studios', 2016))

print('Películas estrenadas en 2014:')
peliculas_2014 = pila_peliculas.peliculas_estrenadas_en_2014()
for pelicula in peliculas_2014:
    print(pelicula)

cantidad_peliculas_2018 = pila_peliculas.cantidad_peliculas_estrenadas_en_2018()
print('Cantidad de películas estrenadas en 2018:', cantidad_peliculas_2018)

print('Películas de Marvel Studios estrenadas en 2016:')
peliculas_marvel_2016 = pila_peliculas.peliculas_marvel_estrenadas_en_2016()
for pelicula in peliculas_marvel_2016:
    print(pelicula)