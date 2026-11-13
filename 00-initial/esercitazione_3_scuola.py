from typing import List


class Studente:
    def __init__(self, nome: str, cognome: str, eta: int, citta: str) -> None:
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.citta = citta

    def classificazione(self) -> str:
        if 14 <= self.eta <= 16:
            return "Biennio"
        if 17 <= self.eta <= 19:
            return "Triennio"
        return "Altro"

    def __str__(self) -> str:
        return f"{self.nome} {self.cognome}, {self.eta} anni, residente a {self.citta}"


class Scuola:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.studenti = []

    def aggiungi_studente(self, studente: Studente) -> None:
        self.studenti.append(studente)

    def cerca_per_cognome(self, cognome: str) -> List[Studente]:
        cognome = cognome.lower()
        return [studente for studente in self.studenti if studente.cognome.lower() == cognome]

    def cerca_per_eta(self, eta: int) -> List[Studente]:
        return [studente for studente in self.studenti if studente.eta == eta]

    def conta_studenti(self) -> int:
        return len(self.studenti)

    def __len__(self) -> int:
        return self.conta_studenti()


class Classe:
    def __init__(self, sezione: str, anno: int) -> None:
        self.sezione = sezione
        self.anno = anno
        self.studenti = []

    def aggiungi_studente(self, studente: Studente) -> None:
        self.studenti.append(studente)

    def elenco(self) -> List[Studente]:
        return self.studenti


if __name__ == "__main__":
    scuola = Scuola("Istituto Tecnico")

    scuola.aggiungi_studente(Studente("Luca", "Rossi", 16, "Roma"))
    scuola.aggiungi_studente(Studente("Anna", "Verdi", 18, "Milano"))
    scuola.aggiungi_studente(Studente("Marco", "Rossi", 15, "Napoli"))

    print(f"Numero studenti: {scuola.conta_studenti()}")

    for studente in scuola.cerca_per_cognome("rossi"):
        print(studente)
        print(f"Classificazione: {studente.classificazione()}")

    print("Studenti di 18 anni:")
    for studente in scuola.cerca_per_eta(18):
        print(f"- {studente.nome} {studente.cognome}")

    quinta = Classe("5A", 2025)
    quinta.aggiungi_studente(scuola.studenti[1])
    print(f"Classe {quinta.sezione}: {len(quinta.elenco())} studenti")