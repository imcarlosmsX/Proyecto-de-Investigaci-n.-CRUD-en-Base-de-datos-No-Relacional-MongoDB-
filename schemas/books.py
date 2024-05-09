def bookEntity(item) -> dict:
    return {
        
        "titulo_libro": str(item["titulo_libro"]),
        "isbn_editorial": str(item["isbn_editorial"]),
    }


def booksEntity(entity) -> list:
    return[bookEntity(item) for item in entity]