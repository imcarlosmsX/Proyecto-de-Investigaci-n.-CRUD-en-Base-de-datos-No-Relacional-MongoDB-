from edition import editionEntity

def loanEntity(item) -> dict:
    return {
        "fecha_prestamo": str(item["fecha_prestamo"]),
        "fecha_devolucion": str(item["id_prestamo"]),
        "isbn": editionEntity(item["edicion"]),
    }

def loansEntity(entity) -> list:
    return [editionEntity(item) for item in entity]