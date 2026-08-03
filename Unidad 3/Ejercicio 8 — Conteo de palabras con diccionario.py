#8 contar cuantas veces se repite una palabra con diccionario
#e imprimir el resultado
sentence = "españa es el campeon y messi el lloron"
counts = {}
for word in sentence.split():
    counts[word] = counts.get(word,0)+1
print(counts)