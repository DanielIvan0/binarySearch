import copy

def obtenerDatos(f):
    return open(f).read().split('\n')

def criterio(e):
    e = e.split(' ', 3)[:-1]
    m, d, h = e[0], e[1], e[2]
    return int(f'{month[m]}' + (f'0{e[1]}' if int(e[1]) < 10 else e[1]) + h.replace(':', ''))

def ordenarDatos(l):
    l.sort(key = criterio)

def busqBinaria(l, v):
    return 'holi'

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
lista = [(lambda e : int(f'{month[e[0]]}' + (f'0{e[1]}' if int(e[1]) < 10 else e[1]) + e[2].replace(':', '')))(el.split(' ', 3)[:-1]) for el in bitacora]
print(lista)
try:
    # Solicitar fechas al usuario en formato Jen|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec día
    print('Formato Jen|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec día')
    print('Ejemplo: Sep 16')
    fechas = [
        input('Fecha de inicio: ').split(' '),
        input('Fecha de final: ').split(' ')
    ]

    # Realizar búsqueda
    i = busqBinaria(lista, fechas[0])
    j = busqBinaria(lista, fechas[1])

    print(bitacora[i:j])
except:
    print('Con todo respeto: Usted acaba de hacer una tontería, señor.')