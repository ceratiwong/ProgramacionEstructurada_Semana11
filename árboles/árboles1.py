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

def preorden(raiz):
    if raiz is not None:
        print(raiz["valor"], end=" ")
        preorden(raiz["izq"])
        preorden(raiz["der"])

def postorden(raiz):
    if raiz is not None:
        postorden(raiz["izq"])
        postorden(raiz["der"])
        print(raiz["valor"], end=" ")

# Construcción del árbol
raiz = None
for numero in [50, 30, 70, 20, 40, 60, 80]:
    raiz = insertar(raiz, numero)
print("Preorden: ", end="")
preorden(raiz)

print("\nPostorden:", end=" ")
postorden(raiz)