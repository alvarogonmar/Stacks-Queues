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
    print("Después de hacer pop:", stack.stack)
    print("¿Está vacío?", stack.is_empty())
    print("Tamaño final:", stack.size())

    print("\n=== Pruebas con la clase Queue ===")
    queue = Queue()

    # Revisar si esta vacia al inicio
    print("¿Está vacía?", queue.is_empty())

    # Probar dequeue y front cuando la cola esta vacia
    print("Intentando dequeue en cola vacia:", queue.dequeue())
    print("Intentando front en cola vacia:", queue.front())
