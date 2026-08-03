#9 dos encuestas de lenguages de programcion
#se compara, se imprime lo siguiente
#lo que aparece en ambas
#intersection y diferencia
set1 = ["python","C","Java","c++"]
set2 = ["c++","C","rubi","go"]
s1 = set(set1)
s2 = set(set2)
print("Ambas listas:", sorted(s1 & s2))
print("Valores unicos:", sorted((s1-s2)|(s2-s1)))