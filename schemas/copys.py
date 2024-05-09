
def copyEntity(item) -> dict:
    return {
        "numero_copia": int(item["numero_copia"]),
        "isbn_editorial": str(item["isbn_editorial"]),
    }


def copysEntity(entity) -> list:
    return[copyEntity(item) for item in entity]