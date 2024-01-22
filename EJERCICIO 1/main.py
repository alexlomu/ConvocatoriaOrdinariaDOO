from fabrica import FabricaEdificiosEstiloArquitectonico, FabricaEdificios
from clientcode import client_code

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