

def userEntity(item) -> dict:
    return {
        "rut": str(item["rut"]),
        "nombre": str(item["nombre"]),
    }



def usersEntity(entity) -> list:
    return[userEntity(item) for item in entity]