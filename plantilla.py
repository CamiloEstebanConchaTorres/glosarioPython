# CODIGOS Y ORDEN PARA LA CREACION Y MANIPULACION DE PROYECTOS O PROGRAMAS EN PYTHON #


# Esta es la forma para crear un crud o menu principal en el modulo principal (se importan estos modulos depende de la estructura) #

print("""*************************************************************
                     EJEMPLO
*************************************************************
        CRUD
""")
def menu():
    print("\t1. modulo1")
    print("\t2. modulo2")
    print("\t0. salir \n")
    
bandera = True    # CREAMOS UN WHILE CON UN TRUE PARA PODER ROMPER EL BUCLE CUANDO SEA NECESARIO ROMPERLO #
while (bandera):
    menu()
    opc = int(input("ingrese el numero del modulo al que desea ingresar \n")) # OPCIONAL #
    match(opc):
        case 1:
               # CON CASE ENTRAMOS A CADA SELECCION de modulo
               #DEL USUARIO, YA SEA POR LETRAS O NUMEROS#
   
            with open("Storage/modulo1/dato.json", "r") as f:       # ESTA ES LA FORMA DE LEER O CARGAR EL
                                                                      #CONTENIDO DE UN ARCHIVO JSON (r) # 
                modulo1.dato = json.loads(f.read())
                f.close()                                          
                system("clear")
                modulo1.menu() #
        case 2:
            with open("Storage/modulo2/dato.json", "r") as f:
                modulo2.dato = json.loads(f.read())
                f.close()
                modulo2.menu()                      
        case 0:
            system("clear")
            bandera = False, system("clear") # ROMPER EL BUCLE WHILE
        case _:
            print(menuNoValid(opc))


# validaciones (hay que importar esta opcion =   
            def menuNoValid(opc): 
                print(f"La opcion {opc} no esta disponible") )#
            case _:
            print(menuNoValid(opc))





# EJEMPLOS #
def search():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***************************
        *  Evaluacion del Camper  *
        ***************************
        """)
        for i,val in enumerate(camper):
            print(f"""
________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Apellido: {val.get('Apellido')}
Identificacion: {val.get('Identificacion')}
Direccion: {val.get('Direccion')}
Edad: {val.get('Edad')}
NombreAcudiente: {val.get('NombreAcudiente')}
NumeroAcudiente: {val.get('NumeroAcudiente')}
idAcudiente: {val.get('idAcudiente')}
TelefonoCamper: {val.get('TelefonoCamper')}
Estado: {val.get('Estado')}
________________________
""")
        Codigo = int(input("Ingrese el numero del camper al que desea asignar notas \n"))
        print(f"""
________________________
Codigo: {Codigo}
Nombre: {camper[Codigo].get('Nombre')}
Apellido: {camper[Codigo].get('Apellido')}
Identificacion: {camper[Codigo].get('Identificacion')}
Direccion: {camper[Codigo].get('Direccion')}
Edad: {camper[Codigo].get('Edad')}
NombreAcudiente: {camper[Codigo].get('NombreAcudiente')}
NumeroAcudiente: {camper[Codigo].get('NumeroAcudiente')}
idAcudiente: {camper[Codigo].get('idAcudiente')}
TelefonoCamper: {camper[Codigo].get('TelefonoCamper')}
Estado: {camper[Codigo].get('Estado')}
________________________
        """)
        print("¿Este es el camper al que desea asignar nota? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir\n")
        opc = int(input("Seleccione su opcion \n"))
        if (opc == 1):
            Nota_teorica = int(input("ingrese el valor de la nota teorica \n"))
            Nota_Practica = int(input("ingrese el valor de la nota practica \n"))
            Promedio = (Nota_teorica + Nota_Practica) / 2
            if Promedio <= 59:
                print("! LO SENTIMOS EL CAMPER NO HA SUPERADO LA PRUEBA ! \n")
                info2 = {
                    "Nombre": camper[Codigo].get('Nombre'),
                    "Apellido": camper[Codigo].get('Apellido'),
                    "Identificacion": camper[Codigo].get('Identificacion'),
                    "Direccion": camper[Codigo].get('Direccion'),
                    "Edad": camper[Codigo].get('Edad'),
                    "NombreAcudiente": camper[Codigo].get('NombreAcudiente'),
                    "NumeroAcudiente": camper[Codigo].get('NumeroAcudiente'),
                    "idAcudiente": camper[Codigo].get('idAcudiente'),
                    "TelefonoCamper": camper[Codigo].get('TelefonoCamper'),
                    "Estado": int(input("Asigne el nuevo estado del camper:\n\t"+"\t".join([f"{Estados.index(i)+1}. {i}\n" for i in (Estados)])))
                }
                if info2["Estado"] == 4:
                    En_riesgo.append(info2)
                    with open("Storage/Campers/En_riesgo.json", "w") as f:
                        datos = json.dumps(En_riesgo, indent=4)
                        f.write(datos)
                        f.close()
                else:
                    if info2["Estado"] == 3:
                        Aprobado.append(info2)
                        with open("Storage/Campers/Aprobados.json", "w") as f:
                            datos = json.dumps(Aprobado, indent=4)
                            f.write(datos)
                            f.close()
                    else:
                        if info2["Estado"] == 2:
                            Inscrito.append(info2)
                            with open("Storage/Campers/Inscritos.json", "w") as f:
                                datos = json.dumps(Inscrito, indent=4)
                                f.write(datos)
                                f.close()
                        else:
                            if info2["Estado"] == 1:
                                print("EL CAMPER NO SUPERO LA PRUEBA Y SE QUEDA COMO PREINSCRITO PARA NUEVAS PRUEBAS")
                            else:
                                if info2["Estado"] == 5:
                                    Filtrado.append(info2)
                                    with open("Storage/Campers/Filtrados.json", "w") as f:
                                        datos = json.dumps(Filtrado, indent=4)
                                        f.write(datos)
                                        f.close()
                return "Sucessfully Camper"
            else:
                print("! EL CAMPER HA SUPERADO LA PRUEBA !")
                info = {
                    "Nombre": camper[Codigo].get('Nombre'),
                    "Apellido": camper[Codigo].get('Apellido'),
                    "Identificacion": camper[Codigo].get('Identificacion'),
                    "Direccion": camper[Codigo].get('Direccion'),
                    "Edad": camper[Codigo].get('Edad'),
                    "NombreAcudiente": camper[Codigo].get('NombreAcudiente'),
                    "NumeroAcudiente": camper[Codigo].get('NumeroAcudiente'),
                    "idAcudiente": camper[Codigo].get('idAcudiente'),
                    "TelefonoCamper": camper[Codigo].get('TelefonoCamper'),
                    "Estado": int(input("Asigne el nuevo estado del camper:\n\t"+"\t".join([f"{Estados.index(i)+1}. {i}\n" for i in (Estados)])))            
                }
                if info["Estado"] == 4:
                    En_riesgo.append(info)
                    with open("Storage/Campers/En_riesgo.json", "w") as f:
                        datos = json.dumps(En_riesgo, indent=4)
                        f.write(datos)
                        f.close()
                else:
                    if info["Estado"] == 3:
                        Aprobado.append(info)
                        with open("Storage/Campers/Aprobados.json", "w") as f:
                            datos = json.dumps(Aprobado, indent=4)
                            f.write(datos)
                            f.close()
                    else:
                        if info["Estado"] == 2:
                            Inscrito.append(info)
                            with open("Storage/Campers/Inscritos.json", "w") as f:
                                datos = json.dumps(Inscrito, indent=4)
                                f.write(datos)
                                f.close()
                        else:
                            if info["Estado"] == 1:
                                print("EL CAMPER NO SUPERO LA PRUEBA Y SE QUEDA COMO PREINSCRITO PARA NUEVAS PRUEBAS")
                            else:
                                if info["Estado"] == 5:
                                    Filtrado.append(info)
                                    with open("Storage/Campers/Filtrados.json", "w") as f:
                                        datos = json.dumps(Filtrado, indent=4)
                                        f.write(datos)
                                        f.close()
                return print(f"Camper successfully ")            
        elif (opc == 2):
            bandera = False
        elif (opc == 3):
            system("clear")
            bandera = False


# EJEMPLO DE REGISTRO #

    edad = int(input("ingrese la edad del camper \n"))
    N_Acudiente = ""
    Numero_Acu = ""
    Acudiente = ""
    if edad <=15:
        return print("! No puede ingresar a Campuslands, ya que no cumple con la edad necesaria ! \n")
    elif edad >=16 and edad <=17:
        print(" ! CAMPER MENOR DE EDAD !")
        N_Acudiente = input("Porfavor ingrese el Nombre del acudiente \n")
        Numero_Acu =  (int(input("Porfavor ingrese el Numero del acudiente \n")))
        Acudiente = (int(input("Porfavor ingrese el numero de identificacion del acudiente \n")))
    info = {
        "Nombre": input("Ingrese los nombres del camper\n"),
        "Apellido": input("Ingrese los apellidos del camper\n"),
        "Identificacion": int(input("Ingrese el numero de identificacion del camper\n")),
        "Direccion": input("Ingrese la direccion del camper\n"),
        "Edad": edad,
        "NombreAcudiente": N_Acudiente,
        "NumeroAcudiente": Numero_Acu,
        "idAcudiente": Acudiente,
        "TelefonoCamper":[
            {
            f"{'Fijo' if(int(input('1. Numero Fijo  0. Numero de Celular:  '))) else 'Celular'}":
            int(input(f'Numero de contacto {x+1}: '))
            }
            for x in range(int(input("Cuantos numeros de telefono tiene el camper?:  ")))
        ],          
        "Estado": int(input("Asigne el Estado del camper:\n\t"+"\t".join([f"{Estados.index(i)+1}. {i}\n" for i in (Estados)]))),

    }
    if info["Estado"] == 1:
        camper.append(info)
        with open("Storage/Campers/camper.json", "w") as f:
            datos = json.dumps(camper, indent=4)
            f.write(datos)
            f.close()
        Preinscritos.append(info)
        with open("Storage/Campers/Preinscritos.json", "w") as f:
            datos = json.dumps(Preinscritos, indent=4)
            f.write(datos)
            f.close()
    return "Sucessfully Camper"


# ACTUALZIZAR DATOS O EDITAR #

def Actualizar():
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ***************************
        * Acualizacion del camper *
        ***************************
        """)
        codigo = int(input("Ingrese el codigo del camper que desea actualizar \n"))
        print(f"""
________________________
Codigo: {codigo}
Nombre: {camper[codigo].get('Nombre')}
Apellido: {camper[codigo].get('Apellido')}
Identificacion: {camper[codigo].get('Identificacion')}
Direccion: {camper[codigo].get('Direccion')}
Edad: {camper[codigo].get('Edad')}
________________________
        """)
        print("¿Este es el camper que deseas actualizar? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir")
        opc = int(input())
        if(opc == 1):
            info = {
                "Nombre": input("Ingrese el nombre del camper\n"),
                "Apellido": input("Ingrese el apellido del camper\n"),
                "Identificacion": int(input("Ingrese la Identificacion del camper\n")),
                "Direccion": int(input("Ingrese la Direccion del camper\n")),
                "Edad": int(input("Ingrese la Edad del camper\n")),
            }
            camper[codigo] = info
            with open("Storage/Campers/camper.json", "w") as f:
                data = json.dumps(camper, indent=4)
                f.write(data)
                f.close()
            bandera == False
        elif(opc == 3):
            bandera == False
    #return "Actualizado"


# BUSCAR UN DATO #
    bandera=True
    while (bandera):
        system("clear")
        print("""
        ************************
        *  Filtro del trainer  *
        ************************
        """)
        for i,val in enumerate(trainer):
            print(f"""
________________________
Codigo: {i}
Nombre: {val.get('Nombre')}
Apellido: {val.get('Apellido')}
Identifiacion: {val.get('Identifiacion')}
Edad: {val.get('Edad')}
Telefono: {val.get('Telefono')}
Disponibilidad: {val.get('Disponibilidad')}
Campers: {val.get('Campers')}
________________________
""")
        Codigo = int(input("Ingrese el Codigo del trainer especifico que desea filtrar \n"))
        system("clear")
        print(f"""
________________________
Codigo: {Codigo}
Nombre: {trainer[Codigo].get('Nombre')}
Apellido: {trainer[Codigo].get('Apellido')}
Identifiacion: {trainer[Codigo].get('Identifiacion')}
Edad: {trainer[Codigo].get('Edad')}
Telefono: {trainer[Codigo].get('Telefono')}
Disponibilidad: {trainer[Codigo].get('Disponibilidad')}
Campers: {trainer[Codigo].get('Campers')}
________________________
        """)
        print("¿Desea filtrar otro Trainer? \n")
        print("1. Si")
        print("2. No")
        print("3. Salir\n")
        opc = int(input("Seleccione su opcion \n"))
        if (opc == 1):
            system("clear")
            bandera = True
        if (opc == 2):
            system("clear")
            menu()
        if (opc == 3):
            bandera = False
            system("clear")







# FORMA DE ASIGNAR #

import json
import module.ruta as ruta
import module.modulo as modulo
from module.data import modulos, rutas

rutas = ruta.carga()
modulos = modulo.carga()


print("CRUD de rutas")
print("1. Asignar modulos a las ruta")
print("2. Buscar")
print("3. Actualizar")
print("4. Eliminar")
opc = int(input())

def plantilla(data):
    lista = []
    for i,val in enumerate(data):
        lista.append(f"\n\t\t{i+1} - {val}")
    return "".join(lista)

def asignarModulos():
    selecion = set()
    nuevaLista = []
    while(True):
        for val in modulos:
            print(f"""
            ________________
            Codigo: {val.get("codigo")}
            Nombre: {val.get("nombre_modulo")}
            Prioridad: {val.get("prioridad")}
            Temario: {plantilla(val.get("temario"))}
            ________________
            """)

        selecion.add(input("¿Selecione el modulo que deseas ingresando el codigo?\n"))
        if(not int(input("¿Deseas agregar otro modulo?\n1.SI\n0.NO\n"))):
            for i in selecion:
                for val in modulos:
                   if(val.get("codigo") == i):
                        nuevaLista.append(val)
            break
    return nuevaLista
match(opc):
    case 1:
        Myruta = {
            "codigo": f"R{len(rutas)+1}",
            "nombre_ruta": input("Ingrese el nombre de la ruta: "),
            "modulo": asignarModulos()
        }
        rutas.append(Myruta)
        path = "module/storage/"
        with open(path+"rutas.json", "w") as f:
            f.write(json.dumps(rutas, indent=4))
            f.close()
    case _:
        print("La opcion no esta habilitada")

        # RECORDAR QUE HAY QUE CREAR 2 ODULOS EN ESTE CASO PARA CARGAR LOS 2 JSON #

        #MODULO RUTA#
        import json

path = "module/storage/"
def carga():
    with open(path+"rutas.json", "r") as f:
        return json.loads(f.read())
    
     #MODULO MODULOS#
    import json

path = "module/storage/"
def carga():
    with open(path+"modulos.json", "r") as f:
        return json.loads(f.read())
       
