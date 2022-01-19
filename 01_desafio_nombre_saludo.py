# Escribir un programa que le pida al usuario el nombre
# y responda saludandolo y diciendo el nombre y el largo del saludo

def run():
    nombre = input("Escribe tu nombre: ")
    saludo = "Hola " + nombre
    print(saludo)
    print("El saludo mide " + str(len(saludo)) + " caracteres")


if __name__ == '__main__':
    run()