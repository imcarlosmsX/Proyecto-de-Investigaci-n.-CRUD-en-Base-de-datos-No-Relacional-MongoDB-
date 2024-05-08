

def editionEntity(item) -> dict:
    return {
        "isbn": str(item["isbn"]),
        "year": int(item["year"]),
        "idioma": str(item["idioma"]),
    }

def editionsEntity(entity) -> list:
    return [editionEntity(item) for item in entity]