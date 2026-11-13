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
        self.brani = brani if brani is not None else [] # condizione ternaria: se i brani passati non sono None allora assegna a self.brani brani (valore destra), se no (else) assegna None (valore sinistra)

    def aggiungi_brano(self, b: Brano) -> None:
        self.brani.append(b)

    @property
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

class Playlist:
    def __init__(self, nome: str, brani: Optional[List[Brano]] = None) -> None:
        self.nome = nome
        self.brani = brani if brani is not None else []

    def aggiungi_brano(self, brano: Brano) -> None:
        if brano not in self.brani:
            self.brani.append(brano)

    def rimuovi_brano(self, titolo: str) -> bool:
        for brano in self.brani:
            if brano.titolo.lower() == titolo.lower():
                self.brani.remove(brano)
                return True
        return False

    def brani_brevi(self) -> List[Brano]:
        return [brano for brano in self.brani if brano.short_song()]

    def durata_totale(self) -> int:
        return sum(brano.durata for brano in self.brani)

    def __str__(self) -> str:
        if not self.brani:
            return f"Playlist '{self.nome}' (vuota)"
        elenco = [str(brano) for brano in self.brani]
        return f"Playlist: {self.nome} ({len(self.brani)} brani)\n- " + "\n- ".join(elenco) # \n va a capo
        
class CollezioneCD:
    def __init__(self, proprietario: str, cds: Optional[List[CD]] = None) -> None:
        self.proprietario = proprietario
        self.cds = cds if cds is not None else []

    def aggiungi_cd(self, cd: CD) -> None:
        self.cds.append(cd)

    def filtra_cd_per_autore(self, autore: str) -> List[CD]:
        return [cd for cd in self.cds if cd.autore.lower() == autore.lower()]

    def cerca_brano_in_collezione(self, titolo_brano: str) -> List[CD]:
        # Restituisce la lista dei CD che contengono quel brano
        cd_trovati = []
        for cd in self.cds:
            for brano in cd.brani:
                if brano.titolo.lower() == titolo_brano.lower():
                    cd_trovati.append(cd)
                    break  # Passa al CD successivo appena lo trova
        return cd_trovati

    @property
    def durata_complessiva(self) -> int:
        # Somma le durate totali di ogni singolo CD
        return sum(cd.durata_complessiva for cd in self.cds)

    def __str__(self) -> str:
        if not self.cds:
            return f"Collezione di {self.proprietario}: nessun CD presente."
        elenco = [f"{cd.titolo} di {cd.autore} ({len(cd.brani)} brani)" for cd in self.cds]
        return f"Collezione di {self.proprietario}:\n* " + "\n* ".join(elenco)

if __name__ == "__main__":
    Brano1 = Brano("Oblivion", "M83", 357)
    Brano2 = Brano("Proi Proi", "Honkai: Star Rail", 238)
    Brano3 = Brano("I don't like people", "Boston Manor", 216)

    print(Brano1)
    print(f"{Brano2.titolo} è un brano corto? {Brano2.short_song()}")

    cd = CD("Brani vari", "Autori vari", [Brano1, Brano2, Brano3])

    print(cd)
    print(f"Durata totale: {cd.durata_complessiva} secondi")

    # Test Playlist
    mia_playlist = Playlist("Preferiti Rock", [Brano1, Brano2])
    mia_playlist.aggiungi_brano(Brano3)
    mia_playlist.rimuovi_brano("Proi Proi")
    print("\n" + str(mia_playlist))
    print(f"Durata playlist: {mia_playlist.durata_totale()} secondi")

    # Test CollezioneCD
    collezione = CollezioneCD("Marco", [cd])
    print("\n" + str(collezione))
    print(f"Durata intera collezione: {collezione.durata_complessiva} secondi")
