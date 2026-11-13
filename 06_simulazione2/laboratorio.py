from test_biologico import TestBiologico


class LaboratorioBiotecnologico:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.test_biologici: list[TestBiologico] = []
        self.esiti: dict[str, str] = {}

    def registra_test(self, test: TestBiologico) -> None:
        if test.codice in self.esiti:
            raise ValueError(f"Codice test gia presente: {test.codice}")
        self.test_biologici.append(test)
        self.esiti[test.codice] = test.esito()

    def cerca_per_campione(self, campione: str) -> list[TestBiologico]:
        return [test for test in self.test_biologici if test.campione.lower() == campione.lower()]

    def riepilogo(self) -> None:
        conformi = 0
        fuori_specifica = 0

        print(f"Controllo qualita: {self.nome}")
        for test in self.test_biologici:
            esito = self.esiti[test.codice]
            print(
                test.codice,
                test.campione,
                test.parametro,
                test.valore,
                test.unita,
                esito,
            )
            if esito == "CONFORME":
                conformi += 1
            else:
                fuori_specifica += 1

        print("Risultati conformi:", conformi)
        print("Risultati fuori specifica:", fuori_specifica)
