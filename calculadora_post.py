import math

# 1: Imprime lo que es la bienvenida y mis datos personales.
mensaje = "Bienvenido a la calculadora ONE PIECE"
espacio = " "
nombre = "implementado por: Carlos Samuel Santos Oriz"
carnet = "carnet: 26008387"
seccion= "Seccio: CN"
NO_Grupo= "NO_Grupo: 14"
print((mensaje + espacio + "\n" + nombre + "\n" + carnet + "\n" + seccion + "\n" + NO_Grupo))

# 2: seccion de mensajes de salida y de error.
mensaj = "Saliendo..."
agra = "Gracias por usar nuestra calculadora."
mensaje_2 = "ERROR! Expresion no valida"


# 3: funcion calculadora
def calculadora():
    # 3.1:Entrada de información en la consola
    entrada = input("calculadora_p >> ")
    c = entrada.strip()

    # 3.2:comando de salida
    if c == "quit"or "QUIT" or "Quit":
        print(mensaj + "\n" + agra)
        return
    try:
        # 3.3: restriccion de parentesis
        if "(" not in c and ")" not in c:
            val = float(c)
            if val.is_integer():
                print("respuesta >>", int(val))
            else:
                print("respuesta >>", val)
            return calculadora()

        # 3.4: Restricción de anidación para div, % y fact! usando un contador manual
        if "div" in c or "%" in c or "fact!" in c:
            conteo = 0
            for caracter in c:
                if caracter == "(":
                    conteo = conteo + 1
            if conteo > 1:
                print("respuesta >>", mensaje_2)
                return calculadora()

        def resolver_anidado(expresion):
            while "(" in expresion:
                inicio = expresion.rfind("(")
                fin = expresion.find(")", inicio)

                # 3.5_1: Validacion de espacios
                interior = expresion[inicio + 1: fin]
                if interior.startswith(" ") or interior.endswith(" ") or "  " in interior:
                    return mensaje_2

                # 3.5_2: Usamos el strip y split sobre la variable original
                    # .strip() tiene una función clave: limpiar los espacios sobrantes en los extremos de lo que el usuario escribe
                    # .split() sirve para picar o dividir una cadena de texto en pedazos más pequeños y guardarlos en una lista.
                partes = interior.strip().split()

                # 3.5_3: Límite de operandos
                if len(partes) == 2:  # 3.4_3.a:Funciones: (60 sen), (5 fact!)
                    n = float(partes[0])
                    op = partes[1]
                    if op == "sqroot":
                        if n < 0: return "ERROR! Raiz cuadrada negativa"
                        res = math.sqrt(n)
                    elif op == "sqr":
                        res = n ** 2
                    elif op == "sen":
                        res = math.sin(math.radians(n))
                    elif op == "cos":
                        res = math.cos(math.radians(n))
                    elif op == "tan":
                        res = math.tan(math.radians(n))
                    elif op == "fact!":
                        res = math.factorial(int(n))
                    else:
                        return mensaje_2

                elif len(partes) == 3:  # 3.5_4.b:Operaciones: (4 5 +), (10 2 div)
                    n1 = float(partes[0])
                    n2 = float(partes[1])
                    op = partes[2]
                    if op == "+":
                        res = n1 + n2
                    elif op == "-":
                        res = n1 - n2
                    elif op == "*":
                        res = n1 * n2
                    elif op == "/":
                        if n2 == 0: return "ERROR! Division entre cero"
                        res = n1 / n2
                    elif op == "div":
                        if n2 == 0: return "ERROR! Division entre cero"
                        res = int(n1) // int(n2)
                    elif op == "%":
                        if n2 == 0: return "ERROR! Division entre cero"
                        res = int(n1) % int(n2)
                    else:
                        return mensaje_2
                else: # 3.5:finaliza el bucle while e imprime el error sei se ingresa una expresion indevida
                    return mensaje_2

                # 3.5: Reemplaza un paréntesis ya resuelto por su resultado numérico
                expresion = expresion[:inicio] + str(res) + expresion[fin + 1:]
            return expresion # 3.5:reemplazar un paréntesis ya resuelto por su resultado numérico

        resultado = resolver_anidado(c)

        #4: Formato de respuesta final
        if "ERROR!" in str(resultado):
            print("respuesta >>", resultado)
        else:
            final = float(resultado)
            if final.is_integer():
                print("respuesta >>", int(final))
            else:
                print("respuesta >>", final)
    # 5: Es un atrapa-errores
    except:
        print("respuesta >>", mensaje_2)

    return calculadora()

calculadora()
