class Sensore:
    def __init__(self, codice, grandezza, unita, soglia_massima):
        self.codice = codice
        self.grandezza = grandezza
        self.unita = unita
        self.soglia_massima = soglia_massima


class Satellite:
    def __init__(self, nome):
        self.nome = nome
        self.sensori = {}
        self.letture = []

    def aggiungi_sensore(self, sensore):
        if sensore.codice in self.sensori:
            raise ValueError("Codice sensore gia presente")
        self.sensori[sensore.codice] = sensore

    def registra_lettura(self, codice_sensore, valore):
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

    def letture_in_allarme(self):
        allarmi = []
        for lettura in self.letture:
            if lettura["allarme"]:
                allarmi.append(lettura)
        return allarmi

    def riepilogo(self):
        print("Telemetria satellite:", self.nome)
        for lettura in self.letture:
            stato = "ALLARME" if lettura["allarme"] else "OK"
            print(lettura["sensore"], lettura["valore"], lettura["unita"], stato)


if __name__ == "__main__":
    satellite = Satellite("CubeSat Aurora")
    satellite.aggiungi_sensore(Sensore("TMP-01", "temperatura", "C", 45))
    satellite.aggiungi_sensore(Sensore("BAT-01", "tensione batteria", "V", 8.4))
    satellite.aggiungi_sensore(Sensore("GYR-01", "velocita angolare", "deg/s", 12))

    satellite.registra_lettura("TMP-01", 31.5)
    satellite.registra_lettura("BAT-01", 8.6)
    satellite.registra_lettura("GYR-01", 4.2)
    satellite.riepilogo()
    print("Letture in allarme:", satellite.letture_in_allarme())

    try:
        satellite.registra_lettura("GPS-99", 1.0)
    except KeyError as errore:
        print(errore)