def bookEntity(item) -> dict:
    return {
        
        "titulo_libro": str(item["titulo_libro"]),
        "isbn": str(item["isbn"]),
    }


def booksEntity(entity) -> list:
    return[bookEntity(item) for item in entity]