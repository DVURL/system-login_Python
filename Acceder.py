import time

print("Vas a crearte una cuenta para que puedas acceder a tu cuenta de manera más fácil")
print(" ")

while True:
    user = input("Crea tu username = ")
    print(" ")

    if len(user) >= 5:
        break
    else:
        print("El username debe tener 5 o más dígitos, intente de nuevo")
        print(" ")

while True:
    password = input("Crea una contraseña = ")
    print(" ")

    if len(password) >= 5:
        break
    else:
        print("La contraseña debe tener 5 o más dígitos, intente de nuevo")
        print(" ")

while True:
    acceder = input("¿Deseas acceder ya? = ").lower()

    if acceder == "si":
        print("Accediendo...")
        time.sleep(3)
        print("¡Bienvenido!")
        break
    elif acceder == "no":
        print("Acceso denegado, intenta otra vez")
    else:
        print("Solo se permite escribir 'si' o 'no'")

while True:
    print("")
    acceder_usuario = input("Ingrese su usuario = ")
    print("")
    acceder_contraseña = input("Ingrese su contraseña = ")

    while acceder_contraseña == "":
        print("Por favor ingrese algo")
        acceder_contraseña = input("Ingrese su contraseña = ")

    if acceder_usuario == user and acceder_contraseña == password:
        print("Inicio de sesión correcto")
        break
    else:
        print("Usuario o contraseña incorrectos, intente otra vez")
