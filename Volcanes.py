def registrar():
    while True:
        nombre=input('Ingrese Nombre del Volcán: ')
        if nombre.isalpha():
            if nombre in volcanes:
                print('Nombre del Volcán ya existe')
            else:
                break
        else:
            print('Sólo Letras')
    while True:
        pais=input('Ingrese Nombre del País: ') 
        if pais.isalpha():
            break
        else:
            print('Sólo Letras')
    while True:
        try:
            altura=int(input('Ingrese Altura del Volcán: '))
            if altura>0:
                break
            else:
                print('Debe ser un entero mayor que cero')
        except:
            print('La altura del volcán debe ser un entero')
    while True:        
        agno=input('Ingrese Año Última Erupción: ')
        if agno.isdigit():
            agno=int(agno)
            if 1500<=agno<=2025:
                break   
            else:
               print('El año debe estar entre 1500 y 2025') 
        else:
            print('El año debe ser un entero')
    volcanes[nombre]=[pais,altura,agno]  

def buscar():
    nombre=input('Ingrese Nombre del Volcán: ')
    if nombre in volcanes:
        pais,altura,agno=volcanes[nombre]
        print('Pais: ',pais)
        print('Altura: ',altura)
        print('Año: ',agno)
    else:
        print('Volcán NO Encontrado')

def eliminar():
    nombre=input('Ingrese Nombre del Volcán: ')
    if nombre in volcanes:
 #       print(volcanes.pop(nombre))
        del volcanes[nombre]
        print('Volcán Eliminado Exitosamente!!!!!')
    else:
        print('Volcán NO Encontrado')

def actualizar():
    nombre=input('Ingrese Nombre del Volcán: ')
    if nombre in volcanes:
        pais,altura,agno=volcanes[nombre]
        print('Pais: ',pais)
        print('Altura: ',altura)
        print('Año: ',agno)
        print('===============================')
        pais=input('Ingrese Nombre del País: ') 
        altura=int(input('Ingrese Altura del Volcán: '))  
        agno=int(input('Ingrese Año Última Erupción: '))   
        volcanes[nombre]=pais,altura,agno
    else:
        print('Volcán NO Encontrado')

def mostrar():    
    print('Volcán           País   Altura   Año')
    for clave,valor in volcanes.items():
        print(f'{clave}           {valor[0]}    {valor[1]}     {valor[2]}')  

# Programa Principal

volcanes = {
    "Villarrica": ["Chile", 2847, 2020],
    "Llaima": ["Chile", 3125, 2009],
    "Osorno": ["Chile", 2652, 1835],
    "Calbuco": ["Chile", 2015, 2015],
    "Nevados de Chillán": ["Chile", 3212, 2022]
}

while True:
    print('Menú Principal')
    print('''
        1. Registrar volcán
        2. Buscar volcán
        3. Actualizar volcán
        4. Eliminar volcán
        5. Mostrar todos los volcanes
        6. Salir
    ''')
    opc=input('Ingrese Opción: ')
    if opc=='1':
        registrar()
    elif opc=='2':
        buscar()
    elif opc=='3':
        actualizar()
    elif opc=='4':
        eliminar()
    elif opc=='5':
        mostrar()
    elif opc=='6':
        print('Hasta la vista Baby.....')
        break
    else:
        print('Opción Incorrecta')