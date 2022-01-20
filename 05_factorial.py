def factorial(n):
    """Calcula el factorial de n.
    
    n int > 0
    returns n!
    """

    if n == 1:
        return 1
    
    return n * factorial(n -1)

def run():
    numero = int(input("Escribe un número: "))
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")

if __name__ == '__main__':
    run()