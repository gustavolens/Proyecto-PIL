# Sistema gestor de base de datos con alumnos y profesores.

# No lo hice complejo, procuré plasmar los conceptos: clases y herencia.

lista_estudiante = []
class Estudiante:
    # Constructor:
    def __init__(self, nombre, dni, edad):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad 
    def agregar(self, Nombre, Dni, Edad):
        estudiante = Estudiante(Nombre, Dni, Edad)
        lista_estudiante.append(estudiante)
    def mostrar(self, estudiante):
        print("Nombre: ", estudiante.nombre)
        print("DNI: ", estudiante.dni)
        print("Edad: ", estudiante.edad)
        print("\n")
    def buscar_por_dni(self, dni):
        for i in range(lista_estudiante.__len__()):
            if dni == lista_estudiante[i].dni:
                return i
    def eliminar(self, dni):
        clave = instanciar.buscar_por_dni(dni)
        del lista_estudiante[clave]
    
# print("\nSeleccione la opción:")
# print("\n1. Agregar estudiante.\n2. Mostrar listado de estudiante.\n3. Eliminar detalles de estudiante.\n4. Actualizar detalle de estudiante.\n5. Salir.")
# opcion = input()

instanciar = Estudiante('', '', 00)
# Agregar
# nombre = input('Ingrese nombre: ')
# dni = int(input('Ingrese DNI: '))
# edad = int(input('Ingrese edad: '))
# instanciar.agregar(nombre, dni, edad)

instanciar.agregar('Jose', 2332324, 19)
instanciar.agregar('Juan', 2, 14)
instanciar.agregar('Raul', 4324324, 16)

# Mostrar todos:
for i in range(len(lista_estudiante)):
    instanciar.mostrar(lista_estudiante[i])

# Eliminar por dni:
dni = int(input('Ingrese el DNI para eliminar entrada de estudiante: '))
instanciar.eliminar(dni)
