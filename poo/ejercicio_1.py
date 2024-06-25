class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} de {self.edad} años esta estudiando en {self.grado} grado")

class Trabajador(Persona):
    def __init__(self,nombre,edad,trabajo):
        super().__init__(nombre,edad)
        self.trabajo = trabajo

    def trabajar(self):
        print(f"El trabajador {self.nombre} de {self.edad} años esta trabajando en {self.trabajo}")

while True:
    dedicacion = input("\nla persona es un estudiante o un trabajador?\n").lower()
    if dedicacion == "estudiante":
        alumno = Estudiante(input("indica el nombre del estudiante: "),input("indica la edad del estudiante: "),input("indica el grado del estudiante: "))
        estudiara = input("escribe estudiar para poner al estudiante a estudiar: ").lower()
        if estudiara == "estudiar":
            alumno.estudiar()
        elif estudiara == "salir":
            break
        else:
            print("el estudiante no estudiara\n\n")
    elif dedicacion == "trabajador":
        empleado = Trabajador(input("indica el nombre del trabajador: "),input("indica la edad del trabajador: "),input("indica el empleo del trabajador: "))
        trabajara = input("escribe trabajar para poner al empleado a trabajar: ").lower()
        if trabajara == "trabajar":
            empleado.trabajar()
        elif trabajara == "salir":
            break
        else:
            print("el empleado no trabajara\n\n")
    elif dedicacion == "salir":
        break
    else:
        print("escribe alguna de las 2 opciones!!")

