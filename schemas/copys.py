from edition import editionEntity

def copyEntity(item) -> dict:
    return {
        "numero": int(item["numero"]),
        "edicion": editionEntity(item["edicion"])
    }


def copysEntity(entity) -> list:
    return[copyEntity(item) for item in entity]