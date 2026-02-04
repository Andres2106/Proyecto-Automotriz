class empleado_modelo:
    def __init__(self):
        self.hora_fin = 0
        self.hora_inicio = 0
        self.maquina_asignada = ""
        self.cod_empleado = ""
        self.nom_empleado = ""

    def set_codigo(self, nuevo_codigo):
        self.cod_empleado = nuevo_codigo

    def get_codigo(self):
        return self.cod_empleado

    def set_nombre(self, nuevo_nombre):
        self.nom_empleado = nuevo_nombre

    def get_nombre(self):
        return self.nom_empleado

    def set_hora_fin(self, nueva_hora_fin):
        self.hora_fin = nueva_hora_fin

    def get_hora_fin(self):
        return self.hora_fin

    def set_hora_inicio(self, nueva_hora_inico):
        self.hora_inicio = nueva_hora_inico

    def get_hora_inicio(self):
        return self.hora_inicio

    def set_maquina_asignada(self, nueva_maquina_asignada):
        self.maquina_asignada = nueva_maquina_asignada

    def get_maquina_asignada(self):
        return self.maquina_asignada

    def operar_maquina(self, nombre_maquina):
        texto = "maquina asignada" + nombre_maquina
        texto = texto + self.nom_empleado
        return texto

    def visualizar_producto(self):
        producto = "Producto revisado"
        return producto

    def visualizar_maquina(self):
        maquina = "la cantidad de maquina son:"
        return maquina

    def registro_horas_laborales(self):
        horas = "horas registradas:"
        return horas