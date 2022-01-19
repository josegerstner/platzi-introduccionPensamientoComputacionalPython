# Escribe un programa que compare las edades de dos usuarios
def run():
    usuario1 = {"nombre":"", "edad":0}
    usuario2 = {"nombre":"", "edad":0}
    usuario1["nombre"] = input("Escribe el nombre del usuario 1: ")
    usuario1["edad"] = int(input("Escribe la edad del usuario 1: "))
    usuario2["nombre"] = input("Escribe el nombre del usuario 2: ")
    usuario2["edad"] = int(input("Escribe la edad del usuario 2: "))

    if usuario1["edad"] > usuario2["edad"]:
        print(usuario1["nombre"] + " es mayor que " + usuario2["nombre"])
    elif usuario1["edad"] < usuario2["edad"]:
        print(usuario2["nombre"] + " es mayor que " + usuario1["nombre"])
    else:
        print(usuario1["nombre"] + " y " + usuario2["nombre"] + " tienen la misma edad")


if __name__ == '__main__':
    run()