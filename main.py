def obtenerDatos(f):
    return open(f).read().split('\n')

def ordenarDatos(l):
    l.sort(key = lambda e : valorFecha(*e.split(' ', 3)[:-1]))

def busqBinaria(l, v, L, U):
    if L < U:
        index = (L + U) // 2
        print(f"""
        L = {L}
        U = {U}
        v = {v}
        index = {index}
        l[index] = {l[index]}
        """)
        if v > l[index]:
            return busqBinaria(l, v, index + 1, U)
        elif v < l[index]:
            return busqBinaria(l, v, L, index - 1)
        else:
            print(f'Final: {index}')
            return index
    return -1

valorFecha = lambda m = 'Jan', d = '1', h = '00:00:00' : int(f'{month[m]}' + (f'0{d}' if int(d) < 10 else d) + h.replace(':', ''))

month = {
    'Jan': 1,
    'Feb': 2,
    'Mar': 3,
    'Apr': 4,
    'May': 5,
    'Jun': 6,
    'Jul': 7,
    'Aug': 8,
    'Sep': 9,
    'Oct': 10,
    'Nov': 11,
    'Dec': 12
}

# Obtener datos en lista
bitacora = obtenerDatos('bitacora.txt')

# Ordenar datos
ordenarDatos(bitacora)

# Crear copia de lista con datos más fáciles de manejar
#lista = [(lambda e : int(f'{month[e[0]]}' + (f'0{e[1]}' if int(e[1]) < 10 else e[1]) + e[2].replace(':', '')))(el.split(' ', 3)[:-1]) for el in bitacora]
lista = [valorFecha(*el.split(' ', 3)[:-1]) for el in bitacora]
try:
    # Solicitar fechas al usuario en formato Jen|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec día
    print('Formato Jen|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec día')
    print('Ejemplo: Sep 16')
    fechas = [
        input('Fecha de inicio: ').split(' '),
        input('Fecha de final: ').split(' ')
    ]
    valor1 = valorFecha(fechas[0][0], fechas[0][1])
    valor2 = valorFecha(fechas[1][0], fechas[1][1])
    print(valor1, valor2)
    # Realizar búsqueda
    i = busqBinaria(lista, valor1, 0, len(lista) - 1)
    print(f'i => {i}')
    j = busqBinaria(lista, valor2, 0, len(lista) - 1)
    print(f'j => {j}')

    #print(bitacora[i:j])
except:
    print('Con todo respeto: Usted acaba de hacer una tontería, señor.')