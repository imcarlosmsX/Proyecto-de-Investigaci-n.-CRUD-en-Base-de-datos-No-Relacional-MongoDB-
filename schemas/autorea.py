def aautoreaEntity(item) -> dict:
    return { 
        "titulo_libro": str(item["titulo_libro"]),
        "nombre_autor": str(item["nombre_autor"])}

def aautoreasEntity(entity) -> list:
    return[aautoreaEntity(item) for item in entity]