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
