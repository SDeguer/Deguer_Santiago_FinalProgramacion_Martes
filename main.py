"""
Programa principal de Gestor de Gastos.

Este programa permite llevar un control de gastos personales
de forma simple y funcional.
"""

import task_manager


def mostrar_menu():
    """
    Muestra el menu principal del programa.
    """
    print("\n" + "="*40)
    print("   GESTOR DE GASTOS")
    print("="*40)
    print("1. Agregar gasto")
    print("2. Ver todos los gastos")
    print("3. Ver total gastado")
    print("4. Ver gastos por categoria")
    print("5. Eliminar gasto")
    print("6. Salir")
    print("="*40)


def main():
    """
    Funcion principal que ejecuta el programa.
    """
    print("Iniciando programa...")
    
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opcion: ")
        
        if opcion == "1":
            print("\n--- AGREGAR GASTO ---")
            descripcion = input("Descripcion: ")
            monto = input("Monto: ")
            categoria = input("Categoria: ")
            task_manager.agregar_gasto(descripcion, monto, categoria)
        
        elif opcion == "2":
            task_manager.ver_todos_gastos()
        
        elif opcion == "3":
            task_manager.ver_total()
        
        elif opcion == "4":
            task_manager.ver_por_categoria()
        
        elif opcion == "5":
            task_manager.eliminar_gasto()
        
        elif opcion == "6":
            print("\nGracias por usar el Gestor de Gastos!")
            break
        
        else:
            print("\nOpcion invalida. Intenta de nuevo.")


main()