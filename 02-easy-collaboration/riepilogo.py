"""Riepilogo numerico degli stati degli apparati."""


def crea_riepilogo(apparati: dict) -> dict:
    riepilogo = {
        "totale": len(apparati),
        "OK": 0,
        "ATTENZIONE": 0,
        "OFFLINE": 0,
    }
    for apparato in apparati.values():
        riepilogo[apparato["stato"]] += 1
    
    return riepilogo
