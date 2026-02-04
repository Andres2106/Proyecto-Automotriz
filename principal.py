from Empleado_Modelo2 import Empleado_Modelo2
from bd_modelo import Api_BD
from Api_BD_maquinas import Api_BD_maquinas

#Codigo principal
obj_Api = Api_BD()
obj_Api_maquina = Api_BD_maquinas()
obj_Api_maquina.imprimir_info()
obj_empleado = Empleado_Modelo2("Andrés", "Jaime", "1230987482", "312-7890456")
obj_empleado2 = Empleado_Modelo2("Maria", "Perez", "1238902837", "362-8281992")
obj_empleado3 = Empleado_Modelo2("Juan", "Lopez", "1882992909", "315-7890876")
obj_Api.guardar_empleado(obj_empleado)
obj_Api.guardar_empleado(obj_empleado2)
obj_Api.guardar_empleado(obj_empleado3)
obj_Api.imprimir_Api()