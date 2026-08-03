#20 empleados.csv = juan=1000
#nombre, sueldo y fila por empleado
#Lo que queremos: calcular la suma de todos los sueldos
import csv

with open("empleados.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["nombre", "sueldo"])
    w.writerow(["njaen", 1000])
    w.writerow(["ana", 500])
    w.writerow(["jorge", 700])
    w.writerow(["rodrigo", 10000])
    w.writerow(["didier", 600])

total = 0
with open ("empleados.csv","r") as f:
    for fila in csv.DictReader(f):
        total = total + int(fila["sueldo"])
print(total)