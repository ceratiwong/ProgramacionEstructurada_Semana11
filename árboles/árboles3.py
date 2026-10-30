def crear_nodo(valor):
    return {"valor": valor, "izq": None, "der": None}

def insertar(raiz, valor):
    if raiz is None:
        return crear_nodo(valor)
    if valor < raiz["valor"]:
        raiz["izq"] = insertar(raiz["izq"], valor)
    elif valor > raiz["valor"]:
        raiz["der"] = insertar(raiz["der"], valor)
    return raiz

def inorden(raiz):
    if raiz is not None:
        inorden(raiz["izq"])
        print(raiz["valor"], end=" ")
        inorden(raiz["der"])

def obtener_minimo(raiz):
    actual = raiz
    while actual["izq"] is not None:
        actual = actual["izq"]
    return actual

def eliminar(raiz, valor):
    if raiz is None:
        return None

    # Busqueda del nodo a eliminar
    if valor < raiz["valor"]:
        raiz["izq"] = eliminar(raiz["izq"], valor)
    elif valor > raiz["valor"]:
        raiz["der"] = eliminar(raiz["der"], valor)
    else:
        # CASO 1: Hoja (0 hijos) o CASO 2: Nodo con 1 hijo
        if raiz["izq"] is None:
            return raiz["der"]
        elif raiz["der"] is None:
            return raiz["izq"]

        # CASO 3: Nodo con 2 hijos
        # 1. Obtener el menor del subárbol derecho (sucesor inorden)
        sucesor = obtener_minimo(raiz["der"])
        # 2. Reemplazar el valor por el del sucesor
        raiz["valor"] = sucesor["valor"]
        # 3. Eliminar el sucesor de su posición original
        raiz["der"] = eliminar(raiz["der"], sucesor["valor"])

    return raiz

# --- Verificación ---

# Creación del árbol de prueba
raiz = None
elementos = [50, 30, 70, 20, 40, 60, 80]
for num in elementos:
    raiz = insertar(raiz, num)

print("Árbol inicial (Inorden):")
inorden(raiz)
print("\n")

# 1. Prueba: Eliminar Hoja (0 hijos) -> Nodo 20
raiz = eliminar(raiz, 20)
print("1. Tras eliminar 20 (hoja):")
inorden(raiz)
print("\n")

# 2. Prueba: Eliminar Nodo con 1 hijo -> Nodo 30 (quedó solo con su hijo 40 tras borrar el 20)
raiz = eliminar(raiz, 30)
print("2. Tras eliminar 30 (1 hijo):")
inorden(raiz)
print("\n")

# 3. Prueba: Eliminar Nodo con 2 hijos -> Raíz 50 (se sustituye por el menor del subárbol derecho: 60)
raiz = eliminar(raiz, 50)
print("3. Tras eliminar 50 (2 hijos):")
inorden(raiz)
print()