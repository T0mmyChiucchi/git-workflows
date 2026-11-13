from typing import List, Optional

class Brano:
    def __init__(self, titolo: str, autore: str, durata: int) -> None:
        self.titolo = titolo
        self.autore = autore
        self.durata = durata

    @property
    def titolo(self) -> str:
        return self._titolo

    @property
    def autore(self) -> str:
        return self._autore

    @property
    def durata(self) -> int:
        return self._durata

    @titolo.setter
    def titolo(self, nuovo: str) -> None:
        if not nuovo:
            raise ValueError("Il titolo non può essere vuoto")
        self._titolo = nuovo

    @autore.setter
    def autore(self, nuovo: str) -> None:
        if not nuovo:
            raise ValueError("L'autore non può essere vuoto")
        self._autore = nuovo

    @durata.setter
    def durata(self, nuovo: int) -> None:
        if nuovo <= 0:
            raise ValueError("La durata non può essere 0 o negativa")
        self._durata = nuovo

    def __str__(self) -> str:
        return f"{self.titolo} - {self.autore} ({self.durata} sec)"

    def short_song(self) -> bool:
        return self.durata <= 100

class CD:
    def __init__(self, titolo: str, autore: str, brani: Optional[List[Brano]] = None) -> None:
        self.titolo = titolo
        self.autore = autore
        self.brani = brani if brani is not None else []

    def aggiungi_brano(self, b: Brano) -> None:
        self.brani.append(b)

    def durata_complessiva(self) -> int:
        # durataTotale = 0
        # for b in self.brani:
        #     durataTotale += b.duration
        # return durataTotale
        return sum(brano.durata for brano in self.brani)

    def filtra_brani_per_autore(self, autore: str) -> List[Brano]:
        # newList = []
        # for b in self.brani:
        #     if autore == b.autore:
        #         newList.append(b)
        # return newList
        return [brano for brano in self.brani if autore == brano.autore]

    def copia_brani(self) -> List[str]:
        return [str(brano) for brano in self.brani]

    def __str__(self) -> str:
        descrizione = [str(brano) for brano in self.brani] #richiamo str che è il ToString() del brano così descrizione è una lista dei tostring dei vari brani
        return f"CD: {self.titolo} di {self.autore}\n- " + "\n- ".join(descrizione) #va a capo e poi fa il join dei brani con l'a capo 