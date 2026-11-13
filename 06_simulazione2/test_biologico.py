class TestBiologico:
    def __init__(self, codice: str, campione: str, parametro: str, valore: float, limite_massimo: float, unita: str) -> None:
        self.codice = codice
        self.campione = campione
        self.parametro = parametro
        self.valore = valore
        self.limite_massimo = limite_massimo
        self.unita = unita

    def esito(self) -> str:
        if self.valore <= self.limite_massimo:
            return "CONFORME"
        return "FUORI SPECIFICA"