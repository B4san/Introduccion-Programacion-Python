# creando un diccionario simple

cancion = {
    'Artista' : 'Metallica', #llave y valor
    "Cancion" : "Enter Sandman",
    "Lanzamiento" : 1992,
    "likes" : 3000
}
#Acceder a los elementos del diccionario
print(cancion["Artista"])
print(cancion["Lanzamiento"])

#Mezclar con un string
artista = cancion["Artista"]
print(f"Estoy escuchando a {artista}")

print (cancion)

#agregar nuevo valor
cancion["Playlist"] = "heavy metal"
print(cancion)

# Reemplazar valor existente
cancion["Cancion"] = "Seek & Destroy"
print (cancion)

#ELiminar un valor
del cancion["Lanzamiento"]
print (cancion)





