from books import bookEntity

def editionEntity(item) -> dict:
    return {
        "ISBN": str(item["ISBN"]),
        "ano": int(item["ano"]),
        "idioma": str(item["idioma"]),
        "libro": bookEntity(item["libro"])
    }

def editionsEntity(entity) -> list:
    return [editionEntity(item) for item in entity]