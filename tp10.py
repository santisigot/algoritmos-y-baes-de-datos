from collections import deque
from typing import List, Tuple

Notificacion = Tuple[str, str, str]

def eliminar_notificaciones_facebook(cola: deque) -> None:
    cola_temporal = deque()
    for notificacion in cola:
        if notificacion[1] != 'Facebook':
            cola_temporal.append(notificacion)
    cola.clear()
    cola.extend(cola_temporal)

def mostrar_notificaciones_twitter_python(cola: deque) -> None:
    cola_temporal = deque()
    for notificacion in cola:
        if notificacion[1] == 'Twitter' and 'Python' in notificacion[2]:
            print(notificacion)
        cola_temporal.append(notificacion)
    cola.clear()
    cola.extend(cola_temporal)

def almacenar_notificaciones_temporales(cola: deque) -> List[Notificacion]:
    pila = []
    cola_temporal = deque()
    for notificacion in cola:
        hora = int(notificacion[0].replace(':', ''))
        if 1143 <= hora <= 1557:
            pila.append(notificacion)
        cola_temporal.append(notificacion)
    cola.clear()
    cola.extend(cola_temporal)
    return pila