class Celular:
    def __init__(self,marca,modelo,camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print(f"iniciaste una llamada con un {self.marca} modelo {self.modelo}")

    def colgar(self):
        print("colgaste la llamada")

celular_1 = Celular("samsumg","s23","48MP")
celular_1.llamar()