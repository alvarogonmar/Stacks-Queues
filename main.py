from stack import Stack


def use_stack():
    print('=== Demo: Stack ===')
    s = Stack(10)
    print(f'Se creó el stack con el elemento inicial: {s.peek()}')


    # Agregar elementos
    print('\n-- Operaciones push --')
    s.push(20)
    print(f'Se agregó 20 (número en el top ahora: {s.peek()})')
    s.push(30)
    print(f'Se agregó 30 (número en el top ahora: {s.peek()})')

    print(f'Tamaño actual: {s.size()}')

    # Consultar top
    print('\n-- Operación peek --')
    print(f'Top (peek): {s.peek()}')

    # Remover elementos
    print('\n-- Operaciones pop --')
    removed = s.pop()
    if removed is None:
        print('No se pudo remover: el stack está vacío')
    else:
        print(f'Se removió {removed.value}')
        print(f'Top después de remover: {s.peek()}')

    # Remover hasta vaciar 
    while not s.is_empty():
        removed = s.pop()
        print(f'Se removió {removed.value} (Size: {s.size()})')
