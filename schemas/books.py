def bookEntity(item) -> dict:
    return {
        
        "titulo": str(item["titulo"]),
        "nombre_autor": str(item["nombre_autor"]),
        "isbn": str(item["isbn"]),
    }


def booksEntity(entity) -> list:
    return[bookEntity(item) for item in entity]