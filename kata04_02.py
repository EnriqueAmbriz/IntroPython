# Datos con los que vas a trabajar
nombre = "Moon"
gravedad = 0.00162 # in kms
planeta = "Earth"

# Creamos el título
titulo = f'datos de gravedad sobre {nombre}'

# Creamos la plantilla
hechos = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 
"""

# Unión de ambas cadenas
plantilla = f"""{titulo.title()} 
{hechos} 
""" 
print(plantilla)


# Nuevos datos muestra
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

print(hechos)

plantilla_2 = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(plantilla_2.format(nombre=nombre, planeta=planeta, gravedad=gravedad))

# Pista: print(nueva_plantilla.format(variables))
print(plantilla_2.format(nombre=nombre, planeta=planeta, gravedad=gravedad*1000))