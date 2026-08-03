pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

# INPUT
try:
    verbo = input("Ingrese verbo: ").lower()

    # PROCESS
    raiz = verbo[:-2]
    terminacion_verbo = verbo[-2:]

    if terminacion_verbo not in terminaciones:
        raise ValueError

    lista_terminaciones = terminaciones[terminacion_verbo]

    # OUTPUT
    for i in range(len(pronombres)):
        print(pronombres[i], raiz + lista_terminaciones[i])

except ValueError:
    print("Error: Debe ingresar un verbo regular terminado en ar, er o ir.")