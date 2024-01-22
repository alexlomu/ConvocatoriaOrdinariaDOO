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