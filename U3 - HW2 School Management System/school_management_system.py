usuarios = {
    'jperez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'alumno', 'nombre': 'Ana Martín'},
    'lsantos': {'password': '1234', 'rol': 'alumno', 'nombre': 'Luis Santos'},
    'kgomez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Karla Gómez'},
    'dtorres': {'password': '1234', 'rol': 'alumno', 'nombre': 'Diego Torres'},
    'vherrera': {'password': '1234', 'rol': 'alumno', 'nombre': 'Valeria Herrera'},
    'mlopez': {'password': '1234', 'rol': 'maestro', 'nombre': 'María López'},
    'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
}

materias = ('Matemáticas', 'Programación', 'Inglés')

calificaciones = {
    'jperez': {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'amartin': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'lsantos': {'Matemáticas': 6.5, 'Programación': 7.0, 'Inglés': 8.0},
    'kgomez': {'Matemáticas': 9.5, 'Programación': 9.5, 'Inglés': 9.0},
    'dtorres': {'Matemáticas': 7.0, 'Programación': 6.5, 'Inglés': 7.0},
    'vherrera': {'Matemáticas': 8.0, 'Programación': 8.5, 'Inglés': 6.0}
}

# INPUT
usuario = input("Usuario: ")
clave = input("Contraseña: ")

# PROCESS
while usuario not in usuarios or usuarios[usuario]['password'] != clave:
    print("Usuario o contraseña incorrectos")
    usuario = input("Usuario: ")
    clave = input("Contraseña: ")

nombre = usuarios[usuario]['nombre']
rol = usuarios[usuario]['rol']

# OUTPUT
print("Bienvenido,", nombre, "(" + rol + ")")

if rol == 'alumno':
    print("Boleta de", nombre)
    aprobadas = set()
    pendientes = set()
    for materia in materias:
        calif = calificaciones[usuario][materia]
        print(materia + ":", calif)
        if calif >= 8.0:
            aprobadas.add(materia)
        else:
            pendientes.add(materia)
    print("Materias aprobadas:", aprobadas)
    print("Materias pendientes:", pendientes)

elif rol == 'maestro':
    print("Lista de alumnos:")
    for user in usuarios:
        if usuarios[user]['rol'] == 'alumno':
            print(user, "-", usuarios[user]['nombre'])

    alumno = input("Alumno: ")
    materia = input("Materia: ")
    nueva_calificacion = float(input("Nueva calificación: "))
    calificaciones[alumno][materia] = nueva_calificacion
    print("Calificación actualizada.")

else:
    print("Lista de maestros:")
    for user in usuarios:
        if usuarios[user]['rol'] == 'maestro':
            print(user, "-", usuarios[user]['nombre'])

    print("Lista de materias:")
    for materia in materias:
        print(materia)

    print("Lista de alumnos y calificaciones:")
    for user in calificaciones:
        print(usuarios[user]['nombre'])
        for materia in materias:
            print(" ", materia + ":", calificaciones[user][materia])