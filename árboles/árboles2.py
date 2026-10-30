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

# --- Funciones solicitadas ---

def contar_nodos(raiz):
    if raiz is None:
        return 0
    return 1 + contar_nodos(raiz["izq"]) + contar_nodos(raiz["der"])

def contar_hojas(raiz):
    if raiz is None:
        return 0
    # Es hoja si no tiene hijo izquierdo ni derecho
    if raiz["izq"] is None and raiz["der"] is None:
        return 1
    return contar_hojas(raiz["izq"]) + contar_hojas(raiz["der"])

def altura(raiz):
    if raiz is None:
        return -1
    return 1 + max(altura(raiz["izq"]), altura(raiz["der"]))

# --- Pruebas ---

# 1. Árbol vacío
arbol_vacio = None

# 2. Árbol de un nodo
arbol_un_nodo = crear_nodo(50)

# 3. Árbol de 7 nodos
arbol_siete_nodos = None
for numero in [50, 30, 70, 20, 40, 60, 80]:
    arbol_siete_nodos = insertar(arbol_siete_nodos, numero)

# Resultados
print("--- Árbol Vacío ---")
print("Nodos :", contar_nodos(arbol_vacio))
print("Hojas :", contar_hojas(arbol_vacio))
print("Altura:", altura(arbol_vacio))

print("\n--- Árbol de 1 Nodo ---")
print("Nodos :", contar_nodos(arbol_un_nodo))
print("Hojas :", contar_hojas(arbol_un_nodo))
print("Altura:", altura(arbol_un_nodo))

print("\n--- Árbol de 7 Nodos ---")
print("Nodos :", contar_nodos(arbol_siete_nodos))
print("Hojas :", contar_hojas(arbol_siete_nodos))
print("Altura:", altura(arbol_siete_nodos))