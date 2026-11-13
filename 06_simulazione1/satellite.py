from sensore import Sensore

Lettura = {}


class Satellite:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.sensori = {}
        self.letture: list = []

    def aggiungi_sensore(self, sensore: Sensore) -> None:
        if sensore.codice in self.sensori:
            raise ValueError("Codice sensore gia presente")
        self.sensori[sensore.codice] = sensore

    def registra_lettura(self, codice_sensore: str, valore: float) -> None:
        if codice_sensore not in self.sensori:
            raise KeyError("Sensore non registrato: " + codice_sensore)

        sensore = self.sensori[codice_sensore]
        self.letture.append({
            "sensore": codice_sensore,
            "grandezza": sensore.grandezza,
            "valore": valore,
            "unita": sensore.unita,
            "allarme": valore > sensore.soglia_massima,
        })

    def letture_in_allarme(self) -> list:
        allarmi: list = []
        
        for lettura in self.letture:
            if lettura["allarme"]:
                allarmi.append(lettura)
        
        return allarmi

    def riepilogo(self) -> None:
        print("Telemetria satellite:", self.nome)
        
        for lettura in self.letture:
            stato = "ALLARME" if lettura["allarme"] else "OK"
            print(lettura["sensore"], lettura["valore"], lettura["unita"], stato)
