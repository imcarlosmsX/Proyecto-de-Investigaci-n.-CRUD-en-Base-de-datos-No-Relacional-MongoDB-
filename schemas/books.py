def bookEntity(item) -> dict:
    return {
        
        "titulo": str(item["titulo"]),
        "isbn": str(item["isbn"]),
    }


def booksEntity(entity) -> list:
    return[bookEntity(item) for item in entity]