lenguajes = ["Python", "Kotlin", "Java", "JavaScript"]

print (lenguajes)

#Los array (lists) comienzan en la posicion 0
print(lenguajes[0]) #python

#Ordenar los elementos alfabeticamente
lenguajes.sort()
print(lenguajes)

#acceder a un elemento dentro de un texto
aprendiendo = f"estoy aprendiendo {lenguajes[3]}"
print(aprendiendo)

#modificando valores de un array (list)
lenguajes[2] = "PHP"
print(lenguajes)

#Agregar elementos a un array (list)
lenguajes.append("ruby")
print(lenguajes)

#Eliminar un elemento de un array (list)
del lenguajes[1]
print(lenguajes)

#eliminar el ultimo elemento de un array(list)
lenguajes.pop()
print(lenguajes)

#Eliminar con pop una posicion en especifico
lenguajes.pop(0)
print(lenguajes)    

#Eliminar por nombre
lenguajes.remove("PHP")
print(lenguajes)