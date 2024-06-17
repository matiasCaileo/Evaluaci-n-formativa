empleados = []

def registrar_empleado():
    nombre = input("Nombre: ")
    print("Escriba su cargo: ")
    print("Ceo")
    print("Desarrollador")
    print("Analista de datos")
    cargo = input("Cargo: ")
    sueldo = float(input("Sueldo: "))
    trabajadores={"Nombre": nombre, "Cargo": cargo, "Sueldo": sueldo, "Sueldo Neto": sueldo * 0.83}
    empleados.append(trabajadores)
    print("Empleado registrado!")

def lista_empleados():
    for empleado in empleados:
        print(empleado)

def imprimir_planilla():
    empleados = lista_empleados()
    
    with open('PYTHON2.1/Archivo nuevo.txt', 'w', encoding='utf-8') as archivo:
        for empleado in empleados:
            nombre = empleado['Nombre']
            cargo = empleado['Cargo']
            sueldo_bruto = empleado['Sueldo']
            sueldo_neto = empleado['Sueldo Neto']
            archivo.write(f"{nombre} {cargo} {sueldo_bruto} {sueldo_neto}\n")
    
    print("Planilla de sueldos completa generada correctamente en planilla_sueldos_completa.txt")
