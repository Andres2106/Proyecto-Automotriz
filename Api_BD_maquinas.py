class Api_BD_maquinas:
    def __init__(self):
        self.Api_maquinas = [
            ["Código", "Nombre Maquina", "Modelo", "Estado Maquina"],
            ["Cod 1921", "Brazo mecanico", "x102", "Apagada"],
            ["Cod 1234", "Cinta transportadora", "zx400", "Requiere mantenimiento"],
            ["Cod 5564", "Monobrazo", "j102", "Encendida"],
        ]
    
    def imprimir_info(self):
        for i in range(len(self.Api_maquinas)):
            print(self.Api_maquinas[i])
    
    def buscar_info(self):
        return self.Api_maquinas[0][1]