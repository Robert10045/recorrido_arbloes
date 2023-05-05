class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def evaluar_arbol(nodo):
    if nodo is None:
        return 0

    valor_izq = evaluar_arbol(nodo.izquierda)
    valor_der = evaluar_arbol(nodo.derecha)

    if nodo.valor == '+':
        return valor_izq + valor_der
    elif nodo.valor == '-':
        return valor_izq - valor_der
    elif nodo.valor == '*':
        return valor_izq * valor_der
    elif nodo.valor == '/':
        return valor_izq / valor_der
    else:
        return float(nodo.valor)

# Creamos el árbol con la expresión (2+4)*3/(1+5-2)
arbol = Nodo('/')
arbol.izquierda = Nodo('*')
arbol.izquierda.izquierda = Nodo('+')
arbol.izquierda.izquierda.izquierda = Nodo('2')
arbol.izquierda.izquierda.derecha = Nodo('4')
arbol.izquierda.derecha = Nodo('3')
arbol.derecha = Nodo('-')
arbol.derecha.izquierda = Nodo('+')
arbol.derecha.izquierda.izquierda = Nodo('1')
arbol.derecha.izquierda.derecha = Nodo('5')
arbol.derecha.derecha = Nodo('2')

resultado = evaluar_arbol(arbol)
print(resultado) # Debería imprimir 4.5

