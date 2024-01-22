# Modelo de Tipo de Edificios
class Edificio:
    def __init__(self, nombre, ubicacion, fecha_construccion, altura, tipo_uso):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.fecha_construccion = fecha_construccion
        self.altura = altura
        self.tipo_uso = tipo_uso
        self.diseño_arquitectonico = None
        self.diseño_estructural = None
        self.proyecto_construccion = None
