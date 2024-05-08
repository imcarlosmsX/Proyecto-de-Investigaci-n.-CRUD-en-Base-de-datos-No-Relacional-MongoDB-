def authorEntity(item) -> dict:
    return {
        "nombre_autor": str(item["nombre_autor"]) }

def authorsEntity(entity) -> list:
    return[authorEntity(item) for item in entity]