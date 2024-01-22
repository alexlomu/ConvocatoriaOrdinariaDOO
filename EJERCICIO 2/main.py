from edificio import Edificio
from proyectoconstr import ProyectoDeConstruccion
from regulacion import RegulacionLocal
from datetime import datetime

if __name__ == "__main__":
    try:
        # Crear instancias de los modelos
        edificio_residencial = Edificio("Residencial A", "Ciudad X", datetime(2023, 1, 1), 6 , "Residencial")
        regulacion_local_altura = RegulacionLocal("Altura Máxima", "Altura máxima permitida de 5 pisos.", datetime(2020, 1, 1))
        proyecto_construccion_residencial = ProyectoDeConstruccion(ProyectoDeConstruccion.EstadoProyecto.DISENO, datetime(2023, 1, 1), None)

        # Asociar objetos
        edificio_residencial.proyecto_construccion = proyecto_construccion_residencial
        proyecto_construccion_residencial.edificio = edificio_residencial

        # Validar cumplimiento con regulaciones locales
        regulacion_local_altura.validar_cumplimiento(proyecto_construccion_residencial)

        # El edificio cumple con las regulaciones, se puede continuar con la creación.
        print(f"El edificio '{edificio_residencial.nombre}' ha sido creado exitosamente.")

    except Exception as e:
        # Capturar y mostrar mensajes de error
        print(f"Error: {e}")