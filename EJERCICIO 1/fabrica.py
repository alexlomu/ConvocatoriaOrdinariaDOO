from edificio import *
from tiposedifios import *
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