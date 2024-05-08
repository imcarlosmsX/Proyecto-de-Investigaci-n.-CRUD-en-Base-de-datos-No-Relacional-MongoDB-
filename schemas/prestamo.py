def loanEntity(item) -> dict:
    return {
        "rut": str(item["rut"]),
        "numero_copia": str(item["numero_copia"]),
        "isbn": str(item["isbn"]),
        "fecha_prestamo": str(item["fecha_prestamo"]),
        "fecha_devolucion": str(item["fecha_devolucion"]),
        
    }

def loansEntity(entity) -> list:
    return [loanEntity(item) for item in entity]