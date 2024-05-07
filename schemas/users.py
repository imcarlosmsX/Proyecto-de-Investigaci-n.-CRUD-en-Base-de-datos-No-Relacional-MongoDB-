from prestamo import loansEntity

def userEntity(item) -> dict:
    return {
        "RUT": str(item["RUT"]),
        "nombre": str(item["nombre"]),
        "prestamos": loansEntity(item["prestamos"])
    }



def usersEntity(entity) -> list:
    return[userEntity(item) for item in entity]