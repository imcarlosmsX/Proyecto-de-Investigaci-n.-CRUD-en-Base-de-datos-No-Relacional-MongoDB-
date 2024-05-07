from edition import editionEntity

def loanEntity(item) -> dict:
    return {
        "fecha_prestamo": str(item["fecha_prestamo"]),
        "fecha_devolucion": str(item["fecha_devolucion"]),
        "rut": str(item["rut"]),
        "numero_copia": str(item["numero_copia"]),
    }

def loansEntity(entity) -> list:
    return [editionEntity(item) for item in entity]