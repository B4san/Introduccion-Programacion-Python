# Operadores and y Or

usuario_logueado = False
usuario_admin = False

if usuario_logueado and usuario_admin:
    print("Administrador")
elif usuario_logueado:
    print("Acceso al sistema")
else:
    print("Debes iniciar Sesion")


if usuario_logueado or usuario_admin:
    print("Administrador")
elif usuario_logueado:
    print("Acceso al sistema")
else:
    print("Debes iniciar Sesion")