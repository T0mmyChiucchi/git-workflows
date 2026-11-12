class Brano:
    def __init__(self, titolo: str, autore: str, durata: int) -> None:
        self.titolo = titolo
        self.autore = autore
        self.durata = durata

    @property
    def titolo(self) -> str:
        return self.titolo

    @property
    def autore(self) -> str:
        return self.autore

    @property
    def durata(self) -> int:
        return self.durata

    @titolo.setter
    def titolo(self, nuovo: str) -> None:
        if not nuovo:
            raise ValueError("Il titolo non può essere vuoto")
        self.titolo = nuovo

    @autore.setter
    def autore(self, nuovo: str) -> None:
        if not nuovo:
            raise ValueError("L'autore non può essere vuoto")
        self.autore = nuovo

    @durata.setter
    def durata(self, nuovo: int) -> None:
        if nuovo <= 0:
            raise ValueError("La durata non può essere 0 o negativa")
        self.durata = nuovo

    def __str__(self) -> str:
        return f"{self.titolo} - {self.autore} ({self.durata} sec)"

    def shortSong(self) -> bool:
        return self.durata <= 100
