import SucursalPasteleria
import Cliente

class Main:
    @staticmethod
    def ejecutar():
        # Crear una sucursal de pastelería
        sucursal_pasteleria = SucursalPasteleria()
        
        # Crear un cliente y asignarle la sucursal de pastelería
        cliente = Cliente(sucursal_pasteleria)
        
        # Tomar una orden de pastel de chocolate
        cliente.tomar_orden("chocolate")
        
        # Tomar una orden de pastel de vainilla
        cliente.tomar_orden("vainilla")

# Ejecutar el programa
if __name__ == "__main__":
    Main.ejecutar()