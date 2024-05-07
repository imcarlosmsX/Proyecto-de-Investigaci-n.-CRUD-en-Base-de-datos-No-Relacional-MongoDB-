def authorEntity(item) -> dict:
    return {
        "nombre_autor": str(item["nombre_autor"]),
        "titulo_libro": str(item["titulo_libro"])    }