def authorEntity(item) -> dict:
    return {
        "nombre_autor": str(item["nombre_autor"]),
        "titulo_libro": bookEntity(item["libros"]),    }

def bookEntity(item) -> dict:
    return {
        "isbn": str(item["isbn"]),
        "titulo": str(item["titulo"]),
        "year": int(item["year"]),
        "idioma": str(item["idioma"]),
        "nombre_autor": authorEntity(item["autores"]),
    }


def booksEntity(entity) -> list:
    return[bookEntity(item) for item in entity]