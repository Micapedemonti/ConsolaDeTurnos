def numeros_perfumeria():
    for numero in range(1,10000):
        yield f"P - {numero}"

def numeros_farmacia():
    for numero in range(1,10000):
        yield f"F - {numero}"

def numeros_cosmetica():
    for numero in range(1,10000):
        yield f"C - {numero}"

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador(rubro):
    print("\n" + "*" * 23)
    print("Su numero es:")
    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))

    print("Aguarde y sera atendido")
    print("\n" + "*" * 23 + "\n")