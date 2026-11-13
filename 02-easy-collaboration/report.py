"""Filtri di report per gli apparati avionici."""

RegistroApparati = {}


def filtra_per_stato(apparati: dict, stato: str) -> list:
    stato_normalizzato = stato.upper()
    return [apparato for apparato in apparati.values() if apparato["stato"] == stato_normalizzato]


def filtra_per_bus(apparati: dict, bus: str) -> list:
    return [apparato for apparato in apparati.values() if apparato["bus"] == bus]
