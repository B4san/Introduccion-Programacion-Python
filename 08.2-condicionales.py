#EJemplo con elif
ocupacion = "Obrero"

if ocupacion == "Estudiante":
    print("Tienes 50% de descuento")
elif ocupacion == "Jubilado":
    print("Tienes un 75% de descuento")
elif ocupacion == "Desempleado":
    print("Tienes un 10% de descuento")
else:
    print("Debes pagar el 100%")