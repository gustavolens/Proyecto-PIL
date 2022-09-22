# Sistema gestor de base de datos con alumnos.

# No lo hice complejo, procuré plasmar los conceptos de clase.

lista_estudiante = []
class Estudiante:
    # Constructor:
    def __init__(self, nombre, dni, edad, curso):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad 
        self.curso = curso

    def agregar(self, Nombre, Dni, Edad, Curso):
        """Crear objeto y agregarlo a lista_estudiante.
        """
        estudiante = Estudiante(Nombre, Dni, Edad, Curso)
        lista_estudiante.append(estudiante)

    def mostrar(self, estudiante):
        """Mostrar los datos del objeto o estudiante.
        """
        print("\nNombre: ", estudiante.nombre)
        print("DNI: ", estudiante.dni)
        print("Edad: ", estudiante.edad)
        print("Curso: ", estudiante.curso)

    def buscar_por_dni(self, dni):
        """Recorrer lista_estudiante que contiene los objetos y retornar el índice del objeto en la lista,
        de acuerdo con el DNI.
        """
        for i in range(lista_estudiante.__len__()):
            if dni == lista_estudiante[i].dni:
                return i

    def eliminar(self, dni):
        """Eliminar objeto de lista_estudiante aprovechando buscar_por_dni que retorna el índice.
        """
        clave = instanciar.buscar_por_dni(dni)
        del lista_estudiante[clave]

instanciar = Estudiante('', '', 00, '')    

def menu_estudiante():
    print("\n-----------Seleccione una opción-----------")
    print("\n1. Agregar estudiante.\n2. Mostrar listado de estudiante.\n3. Eliminar entrada de estudiante.\n4. Salir.\n")
    return int(input('Ingresar opción: '))

opcion = 0

while opcion != 4:
    opcion = menu_estudiante()
    match opcion:
        case 1:
            nombre = input('Ingrese nombre: ')
            dni = int(input('Ingrese DNI: '))
            edad = int(input('Ingrese edad: '))
            curso = input('Ingrese curso: ')
            instanciar.agregar(nombre, dni, edad, curso)
            print("***Entrada exitosa.***")
        case 2:
            # Mostrar todos:
            if lista_estudiante != []:
                print("--------Listado--------")
                for i in range(len(lista_estudiante)):
                    instanciar.mostrar(lista_estudiante[i])
            else:
                print("*** No hay registros. ***")
        case 3:
            # Eliminar por dni:
            if lista_estudiante != []:
                while True:
                    try:
                        dni = int(input('Ingrese el DNI para eliminar entrada de estudiante: '))
                        instanciar.eliminar(dni)
                        print("\n *** Ha eliminado la entrada. ***")
                        break
                    except BaseException:
                        print("Ingrese un DNI válido.")
            else:
                print("*** No hay registros. ***")
        case 4:
            break
        case _:
            print("Ingresar una opción válida.")
print("Gracias, vuelva prontos.")