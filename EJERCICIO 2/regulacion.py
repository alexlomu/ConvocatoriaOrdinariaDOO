# Modelo de Regulaciones Locales
class RegulacionLocal:
    def __init__(self, nombre, descripcion, fecha_vigencia):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_vigencia = fecha_vigencia

    def validar_cumplimiento(self, proyecto_construccion):
        # Lógica para validar el cumplimiento con las regulaciones locales
        if self.nombre == "Altura Máxima" and proyecto_construccion.edificio.altura > 5:
            raise Exception(f"Error: El edificio '{proyecto_construccion.edificio.nombre}' excede la altura máxima permitida.")
