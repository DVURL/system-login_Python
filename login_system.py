import time
user = ""
password = ""

print("Necesitas tener una cuenta para ingresar")
print(" ")
print("Si no tiene una cuenta registrese")
print("")

while True:
    print("Presione 1 si desea registrarse")
    print("Presione 2 si desea iniciar sesión")

    opcion_general = input("Cual es la opción deseada: ")

    if opcion_general == "1":
        print("Accediendo al sistema...")
        time.sleep(3)
        print()
        print("Vamos a proceder con la creación de su cuenta")
        print()

        while True:
            user = input("Cree su nombre de usuario: ")
            if len(user) >= 5:
                print()
                print("Creando usuario...")
                print()
                time.sleep(3)
                print("¡Usuario creado sin problemas!")
                break
            else:
                print("El usuario debe contener 5 o más caracteres")

        while True:
            password = input("Cree su contraseña: ")
            if len(password) >= 8:
                print()
                print("Creando contraseña...")
                print()
                time.sleep(3)
                print("Contraseña creada sin problemas")
                break
            else:
                print("La contraseña debe contener 8 o más caracteres")

        while True:
            inicio = input("¿Desea regresar?: ").lower()
            if inicio == "si":
                print("Accediendo...")
                time.sleep(3)
                break
            elif inicio == "no":
                print("Acceso denegado")
                break
            else:
                print("Solo coloque si o no")
    elif opcion_general == "2":
        if user == "" or password == "":
            print("Primero debe registrarse y crear usuario y contraseña")
            print()
            continue

        print("Accediendo...")
        time.sleep(3)
        print("Vamos a proceder con el inicio de sesión")
        print()

        intentos = 3

        while intentos > 0:
            acceder_usuario = input("Ingrese su usuario = ")
            acceder_contraseña = input("Ingrese su contraseña = ")

            if acceder_usuario == user and acceder_contraseña == password:
                print("Inicio de sesión correcto ✅")
                break
            else:
                intentos -= 1

                if intentos > 0:
                    if intentos == 1:
                        print("Incorrecto. Te queda", intentos, "intento")
                    else:
                        print("Incorrecto. Te quedan", intentos, "intentos")
                else:
                    print("Cuenta bloqueada 💀")
                    break

    else:
        print("Opción no válida")
        print()

        
