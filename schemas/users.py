

def userEntity(item) -> dict:
    return {
        "RUT": str(item["RUT"]),
        "nombre": str(item["nombre"]),
        "numero_copia": str(item["numero_copia"]),
    }



def usersEntity(entity) -> list:
    return[userEntity(item) for item in entity]