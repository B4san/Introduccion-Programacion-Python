# Revisar si una condicion es mayor a
balance = 10
if balance > 0:
    print("PUedes pagar")
else:
    print("No tienes saldo")

#Likes
likes = 199
if likes >= 200:
    print("Excelente, 200 likes")
else:
    print("Casi llegas a los 200")

#IF con texto
lenguaje = "PHP"
if not lenguaje == "Python":
    print ("Excelente Decision")

#Evaluar un Boolean
usuario_autenticado = True

if usuario_autenticado:
    print("Acceso al sistema")
else:
    print("Debes iniciar sesion")

#Evaluar un elemento de una lista
lenguajes = ["Python", "Kotlin", "Java", "JavaScript", "PHP"]
if "PHP" in lenguajes:
    print("PHP existe")
else:
    print("No esta en la lista")

#IF Anidados 
usuario_autenticado = False
usuario_admin = False

if usuario_autenticado:
    if usuario_admin:
        print("ACCESO TOTAL")
    else:
        print("Acceso al sistema")
else:
    print("Debes iniciar sesion")
