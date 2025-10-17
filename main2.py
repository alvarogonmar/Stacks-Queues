from stacksandqueues2 import Stack
from stacksandqueues2 import Queue

if __name__ == "__main__":
    print("=== Pruebas con la clase Stack ===")
    stack = Stack()

    # Revisar si esta vacia al inicio
    print("¿Está vacío?", stack.is_empty())

    # Probar pop y peek cuando la pila esta vacia
    print("Intentando pop en stack vacio:", stack.pop())
    print("Intentando peek en stack vacio:", stack.peek())

    # Agregar elementos
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Elementos en el stack:", stack.stack)
    print("Tamaño actual:", stack.size())
    print("Elemento superior (peek):", stack.peek())

    # Eliminar elementos
    print("Elemento eliminado (pop):", stack.pop())
