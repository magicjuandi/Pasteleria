import PasteleriaFactory
import PastelChocolate
import PastelVainilla

class SucursalPasteleria(PasteleriaFactory):
    def crear_pastel(self, tipo):
        if tipo == "chocolate":
            return PastelChocolate()
        elif tipo == "vainilla":
            return PastelVainilla()