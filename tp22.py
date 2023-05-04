def usar_la_fuerza(mochila, objetos_sacados=0):
    if not mochila:
        return objetos_sacados, False
    if mochila[0] == "sable de luz":
        return objetos_sacados+1, True
    return usar_la_fuerza(mochila[1:], objetos_sacados+1)
    
mochila = ["Brújula estelar Jedi", "Pistola bláster pesada DL-44", "sable de luz", "Leche Azul", "Han Solo congelado en carbonita"]
objetos_sacados, sable_encontrado = usar_la_fuerza(mochila)
if sable_encontrado:
    print(f"El Jedi encontró el sable de luz después de sacar {objetos_sacados} objetos.")
else:
    print("El Jedi no encontró el sable de luz en la mochila.")