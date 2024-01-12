from __future__ import annotations
from abc import ABC, abstractmethod
import copy

# Interfaz abstracta para la fábrica de edificios
class EdificioFactory(ABC):
    @abstractmethod
    def crear_edificio_residencial(self) -> Edificio:
        pass

    @abstractmethod
    def crear_edificio_comercial(self) -> Edificio:
        pass

    @abstractmethod
    def crear_edificio_industrial(self) -> Edificio:
        pass

    @abstractmethod
    def crear_edificio_educativo(self) -> Edificio:
        pass

    @abstractmethod
    def crear_edificio_gubernamental(self) -> Edificio:
        pass


# Interfaz abstracta para el producto Edificio
class Edificio(ABC):
    @abstractmethod
    def mostrar_informacion(self) -> str:
        pass

    @abstractmethod
    def duplica(self) -> Edificio:
        pass

# Clase FabricaEdificios que utiliza prototipos para crear nuevos edificios
class FabricaEdificios:
    def __init__(self):
        self.prototipo_residencial = EdificioResidencial()
        self.prototipo_comercial = EdificioComercial()
        self.prototipo_industrial = EdificioIndustrial()
        self.prototipo_educativo = EdificioEducativo()
        self.prototipo_gubernamental = EdificioGubernamental()

    def crear_edificio(self, tipo: str, estilo: str) -> Edificio:
        if tipo == "residencial":
            prototipo = self.prototipo_residencial
        elif tipo == "comercial":
            prototipo = self.prototipo_comercial
        elif tipo == "industrial":
            prototipo = self.prototipo_industrial
        elif tipo == "educativo":
            prototipo = self.prototipo_educativo
        elif tipo == "gubernamental":
            prototipo = self.prototipo_gubernamental
        else:
            raise ValueError("Tipo de edificio no válido")
        if estilo == "moderno":
            return prototipo.duplica("moderno")
        elif estilo == "clasico":
            return prototipo.duplica("clasico")
        elif estilo == "futurista":
            return prototipo.duplica("futurista")
        elif estilo == "minimalista":
            return prototipo.duplica("minimalista")
        elif estilo == "organico":
            return prototipo.duplica("organico")


# Clases concretas para los productos Edificio
class EdificioResidencial(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio residencial"

    def duplica(self, estilo: str) -> Edificio:
        nuevo_edificio = copy.copy(self)
        nuevo_edificio.estilo = estilo
        return nuevo_edificio


class EdificioComercial(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio comercial"

    def duplica(self, estilo: str) -> Edificio:
        nuevo_edificio = copy.copy(self)
        nuevo_edificio.estilo = estilo
        return nuevo_edificio


class EdificioIndustrial(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio industrial"

    def duplica(self, estilo: str) -> Edificio:
        nuevo_edificio = copy.copy(self)
        nuevo_edificio.estilo = estilo
        return nuevo_edificio


class EdificioEducativo(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio educativo"

    def duplica(self, estilo: str) -> Edificio:
        nuevo_edificio = copy.copy(self)
        nuevo_edificio.estilo = estilo
        return nuevo_edificio


class EdificioGubernamental(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio gubernamental"

    def duplica(self, estilo: str) -> Edificio:
        nuevo_edificio = copy.copy(self)
        nuevo_edificio.estilo = estilo
        return nuevo_edificio
    
# Fábricas concretas que implementan la interfaz de la fábrica de edificios
class FabricaEdificiosEstiloArquitectonico(EdificioFactory):
    def __init__(self, estilo: str):
        self.estilo = estilo

    def crear_edificio_residencial(self) -> Edificio:
        if self.estilo == "moderno":
            return EdificioResidencialModerno()
        elif self.estilo == "clasico":
            return EdificioResidencialClasico()
        elif self.estilo == "futurista":
            return EdificioResidencialFuturista()
        elif self.estilo == "minimalista":
            return EdificioResidencialMinimalista()
        elif self.estilo == "organico":
            return EdificioResidencialOrganico()

    def crear_edificio_comercial(self) -> Edificio:
        if self.estilo == "moderno":
            return EdificioComercialModerno()
        elif self.estilo == "clasico":
            return EdificioComercialClasico()
        elif self.estilo == "futurista":
            return EdificioComercialFuturista()
        elif self.estilo == "minimalista":
            return EdificioComercialMinimalista()
        elif self.estilo == "organico":
            return EdificioComercialOrganico()

    def crear_edificio_industrial(self) -> Edificio:
        if self.estilo == "moderno":
            return EdificioIndustrialModerno()
        elif self.estilo == "clasico":
            return EdificioIndustrialClasico()
        elif self.estilo == "futurista":
            return EdificioIndustrialFuturista()
        elif self.estilo == "minimalista":
            return EdificioIndustrialMinimalista()
        elif self.estilo == "organico":
            return EdificioIndustrialOrganico()

    def crear_edificio_educativo(self) -> Edificio:
        if self.estilo == "moderno":
            return EdificioEducativoModerno()
        elif self.estilo == "clasico":
            return EdificioEducativoClasico()
        elif self.estilo == "futurista":
            return EdificioEducativoFuturista()
        elif self.estilo == "minimalista":
            return EdificioEducativoMinimalista()
        elif self.estilo == "organico":
            return EdificioEducativoOrganico()

    def crear_edificio_gubernamental(self) -> Edificio:
        if self.estilo == "moderno":
            return EdificioGubernamentalModerno()
        elif self.estilo == "clasico":
            return EdificioGubernamentalClasico()
        elif self.estilo == "futurista":
            return EdificioGubernamentalFuturista()
        elif self.estilo == "minimalista":
            return EdificioGubernamentalMinimalista()
        elif self.estilo == "organico":
            return EdificioGubernamentalOrganico()


# Clases concretas para las fábricas de edificios con estilos arquitectónicos
# Edificios Residenciales
class EdificioResidencialModerno(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio residencial moderno"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioResidencialClasico(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio residencial clásico"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioResidencialFuturista(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio residencial futurista"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioResidencialMinimalista(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio residencial minimalista"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioResidencialOrganico(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio residencial organico"

    def duplica(self) -> Edificio:
        return copy.copy(self)


# Edificios Comerciales
class EdificioComercialModerno(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio comercial moderno"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioComercialClasico(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Comercial clásico"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioComercialFuturista(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Comercial futurista"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioComercialMinimalista(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Comercial minimalista"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioComercialOrganico(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Comercial organico"

    def duplica(self) -> Edificio:
        return copy.copy(self)


# Edificios Industriales
class EdificioIndustrialModerno(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Industria moderno"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioIndustrialClasico(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Industrial clásico"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioIndustrialFuturista(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Industrial futurista"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioIndustrialMinimalista(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Industrial minimalista"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioIndustrialOrganico(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Industrial organico"

    def duplica(self) -> Edificio:
        return copy.copy(self)


# Edificios Educativos
class EdificioEducativoModerno(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Educativo moderno"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioEducativoClasico(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Educativo clásico"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioEducativoFuturista(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Educativo futurista"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioEducativoMinimalista(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Educativo minimalista"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioEducativoOrganico(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Educativo organico"

    def duplica(self) -> Edificio:
        return copy.copy(self)


# Edificio Gubernamental
class EdificioGubernamentalModerno(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Gubernamental moderno"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioGubernamentalClasico(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Gubernamental clásico"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioGubernamentalFuturista(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Gubernamental futurista"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioGubernamentalMinimalista(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Gubernamental minimalista"

    def duplica(self) -> Edificio:
        return copy.copy(self)


class EdificioGubernamentalOrganico(Edificio):
    def mostrar_informacion(self) -> str:
        return "Edificio Gubernamental organico"

    def duplica(self) -> Edificio:
        return copy.copy(self)


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

if __name__ == "__main__":
    print("App: Launched with estilo arquitectónico 'moderno'.")
    client_code(FabricaEdificiosEstiloArquitectonico("moderno"),"residencial")
    print("\n")

    print("App: Launched with estilo arquitectónico 'clasico'.")
    client_code(FabricaEdificiosEstiloArquitectonico("clasico"),"comercial")
    print("\n")

    print("App: Launched with estilo arquitectónico 'futurista'.")
    client_code(FabricaEdificiosEstiloArquitectonico("futurista"),"industrial")
    print("\n")

    print("App: Launched with estilo arquitectónico 'minimalista'.")
    client_code(FabricaEdificiosEstiloArquitectonico("minimalista"),"educativo")
    print("\n")

    print("App: Launched with estilo arquitectónico 'organico'.")
    client_code(FabricaEdificiosEstiloArquitectonico("organico"),"gubernamental")
    print("\n")

    fabrica_edificios = FabricaEdificios()

    # Crear diferentes edificios con estilos arquitectónicos específicos
    edificio_moderno_residencial = fabrica_edificios.crear_edificio("residencial", "moderno")
    print(edificio_moderno_residencial.mostrar_informacion())

    edificio_clasico_comercial = fabrica_edificios.crear_edificio("comercial", "clasico")
    print(edificio_clasico_comercial.mostrar_informacion())

    edificio_futurista_industrial = fabrica_edificios.crear_edificio("industrial", "futurista")
    print(edificio_futurista_industrial.mostrar_informacion())

    edificio_minimalista_educativo = fabrica_edificios.crear_edificio("educativo", "minimalista")
    print(edificio_minimalista_educativo.mostrar_informacion())

    edificio_organico_gubernamental = fabrica_edificios.crear_edificio("gubernamental", "organico")
    print(edificio_organico_gubernamental.mostrar_informacion())