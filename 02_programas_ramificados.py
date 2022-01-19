def run():
    num_1 = int(input("Escribe un entero: "))
    num_2 = int(input("Escribe otro entero: "))

    if num_1 > num_2:
        print("El primer número es mayor que el segundo")
    elif num_1 < num_2:
        print("El segundo número es mayor que el primero")
    else:
        print("Los dos números son iguales")


if __name__ == '__main__':
    run()