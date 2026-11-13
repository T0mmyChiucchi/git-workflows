from test_biologico import TestBiologico

class LaboratorioBiotecnologico:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.test_biologici: list[TestBiologico] = []
        self.esiti: dict[str, str] = {}

    def registra_test(self, test: TestBiologico) -> None:
        if test.codice in self.esiti:
            raise ValueError(f"Test con codice {test.codice} già registrato")
        self.test_biologici.append(test)
        self.esiti[test.codice] = test.esito()

    def cerca_per_campione(self, campione: str) -> list[TestBiologico]:
        return [test for test in self.test_biologici if test.campione.lower() == campione.lower()]