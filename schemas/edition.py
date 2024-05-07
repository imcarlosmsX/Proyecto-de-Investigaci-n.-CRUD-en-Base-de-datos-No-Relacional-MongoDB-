

def editionEntity(item) -> dict:
    return {
        "isbn": str(item["isbn"]),
        "year": int(item["year"]),
        "idioma": str(item["idioma"]),
        "titulo_libro": str(item["titulo_libro"]),
    }

def editionsEntity(entity) -> list:
    return [editionEntity(item) for item in entity]