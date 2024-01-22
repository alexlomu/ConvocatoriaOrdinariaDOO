from edificio import *
from tiposedifios import *


def client_code(factory: EdificioFactory, tipo: str) -> None:
    if tipo == "residencial":
        edificio_residencial = factory.crear_edificio_residencial()
        edificio_clon = edificio_residencial.duplica()
        print(f"Original: {edificio_residencial.mostrar_informacion()}")
        print(f"Clon: {edificio_clon.mostrar_informacion()}")
    
    elif tipo == "comercial":
        edificio_comercial = factory.crear_edificio_comercial()
        edificio_clon = edificio_comercial.duplica()
        print(f"Original: {edificio_comercial.mostrar_informacion()}")
        print(f"Clon: {edificio_clon.mostrar_informacion()}")
    
    elif tipo == "industrial":
        edificio_industrial = factory.crear_edificio_industrial()
        edificio_clon = edificio_industrial.duplica()
        print(f"Original: {edificio_industrial.mostrar_informacion()}")
        print(f"Clon: {edificio_clon.mostrar_informacion()}")
    
    elif tipo == "educativo":
        edificio_educativo = factory.crear_edificio_educativo()
        edificio_clon = edificio_educativo.duplica()
        print(f"Original: {edificio_educativo.mostrar_informacion()}")
        print(f"Clon: {edificio_clon.mostrar_informacion()}")
    
    elif tipo == "gubernamental":
        edificio_gubernamental = factory.crear_edificio_gubernamental()
        edificio_clon = edificio_gubernamental.duplica()
        print(f"Original: {edificio_gubernamental.mostrar_informacion()}")
        print(f"Clon: {edificio_clon.mostrar_informacion()}")
