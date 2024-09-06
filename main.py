import os
from gestion_inventario2 import Inventario

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

inventario_articulo = Inventario()

while True:
    clear_screen()
    print("1: Agregar")
    print("2: Mostrar")
    print("3: Buscar")
    print("4: Actualizar")
    print("5: Eliminar")
    print("6: Salir")

    opcion = input("Elija Opcion: ")
    clear_screen()

    if opcion == "6":
        break

    if opcion == "1":
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        unidad = int(input("Unidad: "))
        inventario_articulo.añadir(nombre, precio, unidad)
        print("Producto agregado correctamente.")
    
    elif opcion == "2":
        inventario_articulo.mostrar()
    
    elif opcion in ["3", "4", "5"]:
        id = input("Ingrese el ID: ")
        if opcion == "3":
            tabla_resultado = inventario_articulo.buscar(id)
            if tabla_resultado:
                print("ID   Nombre  Precio  Cantidad")
                print(f"{tabla_resultado[0]}    {tabla_resultado[1]}    {tabla_resultado[2]}    {tabla_resultado[3]}")
            else:
                print("Producto no encontrado")
        
        elif opcion == "4":
            nuevo_nombre = input("Ingrese nuevo nombre: ")
            nuevo_precio = float(input("Ingrese nuevo precio: "))
            nueva_unidad = int(input("Ingrese nuevas unidades: "))
            inventario_articulo.actualizar(id, nuevo_nombre, nuevo_precio, nueva_unidad)
            print("Producto actualizado correctamente.")
        
        elif opcion == "5":
            inventario_articulo.eliminar(id)
            print("Producto eliminado correctamente.")
    
    input("Presione Enter para continuar...")