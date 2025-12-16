"""
Módulo para gestionar los gastos.

Este módulo contiene las funciones principales para agregar,
mostrar y eliminar gastos.
"""

from datetime import datetime
import storage


def agregar_gasto(descripcion, monto, categoria):
    """
    Agrega un nuevo gasto a la lista.
    
    descripcion: texto que describe el gasto
    monto: cantidad de dinero gastado
    categoria: tipo de gasto (comida, transporte, etc)
    """
    gastos = storage.cargar_gastos()
    
    nuevo_gasto = {
        'descripcion': descripcion,
        'monto': float(monto),
        'categoria': categoria,
        'fecha': datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    
    gastos.append(nuevo_gasto)
    storage.guardar_gastos(gastos)
    print("\nGasto agregado correctamente!")


def ver_todos_gastos():
    """
    Muestra todos los gastos registrados.
    """
    gastos = storage.cargar_gastos()
    
    if len(gastos) == 0:
        print("\nNo hay gastos registrados.")
        return
    
    print("\n=== TODOS LOS GASTOS ===")
    for i in range(len(gastos)):
        gasto = gastos[i]
        print(f"{i+1}. {gasto['descripcion']} - ${gasto['monto']} - {gasto['categoria']} - {gasto['fecha']}")


def ver_total():
    """
    Muestra el total de todos los gastos.
    """
    gastos = storage.cargar_gastos()
    
    if len(gastos) == 0:
        print("\nNo hay gastos registrados.")
        return
    
    total = 0
    for gasto in gastos:
        total = total + gasto['monto']
    
    print(f"\nTOTAL GASTADO: ${total:.2f}")


def ver_por_categoria():
    """
    Muestra el total gastado por cada categoria.
    """
    gastos = storage.cargar_gastos()
    
    if len(gastos) == 0:
        print("\nNo hay gastos registrados.")
        return
    
    categorias = {}
    
    for gasto in gastos:
        cat = gasto['categoria']
        if cat in categorias:
            categorias[cat] = categorias[cat] + gasto['monto']
        else:
            categorias[cat] = gasto['monto']
    
    print("\n=== GASTOS POR CATEGORIA ===")
    for categoria, total in categorias.items():
        print(f"{categoria}: ${total:.2f}")


def eliminar_gasto():
    """
    Elimina un gasto seleccionado por el usuario.
    """
    gastos = storage.cargar_gastos()
    
    if len(gastos) == 0:
        print("\nNo hay gastos para eliminar.")
        return
    
    print("\n=== SELECCIONA EL GASTO A ELIMINAR ===")
    for i in range(len(gastos)):
        gasto = gastos[i]
        print(f"{i+1}. {gasto['descripcion']} - ${gasto['monto']}")
    
    opcion = int(input("\nIngresa el numero del gasto a eliminar: "))
    
    if opcion >= 1 and opcion <= len(gastos):
        gastos.pop(opcion - 1)
        storage.guardar_gastos(gastos)
        print("\nGasto eliminado correctamente!")
    else:
        print("\nOpcion invalida.")