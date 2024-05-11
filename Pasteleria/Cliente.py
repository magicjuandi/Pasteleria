class Cliente:
    def __init__(self, pasteleria_factory):
        self.pasteleria_factory = pasteleria_factory
    
    def tomar_orden(self, tipo_pastel):
        pastel = self.pasteleria_factory.crear_pastel(tipo_pastel)
        pastel.preparar()
        pastel.hornear()
        pastel.decorar()
        pastel.empacar()