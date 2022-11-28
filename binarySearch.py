import time
import random

def busquedaBinariaConTiempo(rango):
    lista = []
    num = (random.randint(1, 1000))
    print("Numero a buscar: ", num)

    inicioSort = time.time()
    for i in range(rango):
        lista.append(i)
    iteraciones = 0
    finSort = time.time()

    inicio = time.time()

    busqueda_binaria(lista, 0, len(lista)-1, num, iteraciones)
    fin = time.time()
    print(f"""
    Rango: {rango}
    Tiempo total: {(fin-inicio)-(inicioSort-finSort)}
    """)


def busqueda_binaria(lista, comienzo, final, objetivo, iteraciones):
    iteraciones = iteraciones + 1
    #print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        print("Iteraciones: ", iteraciones)
        return True

    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, iteraciones)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, iteraciones)
