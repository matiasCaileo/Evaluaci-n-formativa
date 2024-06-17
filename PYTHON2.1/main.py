import funciones as funcion

while True:
    print("1. Registrar Empleado")
    print("2. Listar Empleados")
    print("3. Imprimir Planilla De Sueldos")
    print("4. Salir")

    opcion = input("Ingrese opción: ")

    if opcion == '1':
        funcion.registrar_empleado()
    elif opcion == '2':
        funcion.lista_empleados()
    elif opcion == '3':
        funcion.imprimir_planilla()
    elif opcion == '4':
        print("Saliendo del programa")
        break
    else:
        print("Opción inválida. Ingrese un número entre 1 y 4.")



#Nelson oyarsun
#Diego Benitez
#Matias caileo
