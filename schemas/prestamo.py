def loanEntity(item) -> dict:
    return {
        "rut_usuario": str(item["rut_usuario"]),
        "numero_copia_libro": str(item["numero_copia_libro"]),
        "isbn_editorial": str(item["isbn_editorial"]),
        "fecha_prestamo": str(item["fecha_prestamo"]),
        "fecha_devolucion": str(item["fecha_devolucion"]),
        
    }

def loansEntity(entity) -> list:
    return [loanEntity(item) for item in entity]