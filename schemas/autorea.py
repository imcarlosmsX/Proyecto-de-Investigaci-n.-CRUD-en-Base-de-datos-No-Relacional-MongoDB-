def autoreaEntity(item) -> dict:
    return { 
        "titulo_libro_autorea": str(item["titulo_libro_autorea"]),
        "nombre_autor_autorea": str(item["nombre_autor_autorea"])}

def aautoreasEntity(entity) -> list:
    return[autoreaEntity(item) for item in entity]