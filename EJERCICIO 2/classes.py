from datetime import datetime

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

# Modelo de Proyecto de Construcción
class ProyectoDeConstruccion:
    class EstadoProyecto:
        DISENO = "Diseño"
        CONSTRUCCION = "Construcción"
        MANTENIMIENTO = "Mantenimiento"

    def __init__(self, estado, fecha_inicio, fecha_finalizacion):
        self.estado = estado
        self.fecha_inicio = fecha_inicio
        self.fecha_finalizacion = fecha_finalizacion
        self.edificio = None
        self.equipo_proyecto = []
        self.fases_proyecto = []
