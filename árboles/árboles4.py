def crear_nodo(codigo):
    return {"codigo": codigo, "izq": None, "der": None}

def registrar_codigo(raiz, codigo):
    if raiz is None:
        return crear_nodo(codigo)
    if codigo < raiz["codigo"]:
        raiz["izq"] = registrar_codigo(raiz["izq"], codigo)
    elif codigo > raiz["codigo"]:
        raiz["der"] = registrar_codigo(raiz["der"], codigo)
    return raiz

def consultar_codigo(raiz, codigo):
    if raiz is None:
        return False
    if raiz["codigo"] == codigo:
        return True
    if codigo < raiz["codigo"]:
        return consultar_codigo(raiz["izq"], codigo)
    return consultar_codigo(raiz["der"], codigo)

def listar_codigos(raiz):
    if raiz is not None:
        listar_codigos(raiz["izq"])
        print(raiz["codigo"], end=" ")
        listar_codigos(raiz["der"])

def obtener_minimo(raiz):
    actual = raiz
    while actual["izq"] is not None:
        actual = actual["izq"]
    return actual

def retirar_codigo(raiz, codigo):
    if raiz is None:
        return None

    if codigo < raiz["codigo"]:
        raiz["izq"] = retirar_codigo(raiz["izq"], codigo)
    elif codigo > raiz["codigo"]:
        raiz["der"] = retirar_codigo(raiz["der"], codigo)
    else:
        # Caso 0 o 1 hijo
        if raiz["izq"] is None:
            return raiz["der"]
        elif raiz["der"] is None:
            return raiz["izq"]

        # Caso 2 hijos
        sucesor = obtener_minimo(raiz["der"])
        raiz["codigo"] = sucesor["codigo"]
        raiz["der"] = retirar_codigo(raiz["der"], sucesor["codigo"])

    return raiz