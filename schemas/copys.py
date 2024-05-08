
def copyEntity(item) -> dict:
    return {
        "numero_copia": int(item["numero_copia"]),
        "isbn": str(item["isbn"]),
    }


def copysEntity(entity) -> list:
    return[copyEntity(item) for item in entity]