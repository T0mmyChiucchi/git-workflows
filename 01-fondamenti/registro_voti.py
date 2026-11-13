class RegistroVoti:
    def __init__(self) -> None:
        self.voti = []

    def aggiungi(self, voto: float) -> None:
        if not 0 <= voto <= 10:
            raise ValueError("Il voto deve essere compreso tra 0 e 10")
        self.voti.append(voto)

    def media(self) -> float:
        if not self.voti:
            return 0
        return sum(self.voti) / len(self.voti)

    def esito(self) -> str:
        if self.media() >= 6:
            return "sufficiente"
        return "da recuperare"


if __name__ == "__main__":
    registro = RegistroVoti()
    for voto in (7, 5, 8):
        registro.aggiungi(voto)
    print(f"Voti: {registro.voti}")
    print(f"Media: {registro.media():.2f} ({registro.esito()})")
