from stack import Stack


def use_stack():
    print('=== Demo: Stack ===')
    s = Stack(10)
    print(f'Se creó el stack con el elemento inicial: {s.peek()}')


    # Agregar elementos
    print('\n-- Operaciones push --')
    s.push(20)
