text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""


# Dividir en oraciones
frases = text.split('. ')

# Define las palabras pista: average, temperature y distance suenan bien
palabras_pista = ["average", "temperature", "distance","about"]

# Cree un bucle para imprimir solo datos sobre la Luna que estén relacionados con las palabras clave definidas anteriormente:
for frase in frases:
    for palabra in palabras_pista:
        if palabra in frase:
            print(frase)
            break

print("\n \n")
# Finalmente, actualiza el bucle(ciclo) para cambiar C a Celsius:
for frase in frases:
    for palabra in palabras_pista:
        if palabra in frase:
            print(frase.replace(' C', ' Celsius'))
            break

