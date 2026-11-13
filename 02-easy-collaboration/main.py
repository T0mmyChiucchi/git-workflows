"""Punto di ingresso della soluzione del laboratorio 2."""

from apparati import APPARATI, aggiorna_stato
from report import filtra_per_bus, filtra_per_stato
from riepilogo import crea_riepilogo


def main() -> None:
    print("Registro apparati:")
    for codice, apparato in APPARATI.items():
        print(f"- {codice}: {apparato['nome']} | {apparato['bus']} | {apparato['stato']}")

    print("\nApparati offline:")
    print(filtra_per_stato(APPARATI, "OFFLINE"))
    print("\nApparati collegati a BUS-A:")
    print(filtra_per_bus(APPARATI, "BUS-A"))
    print("\nRiepilogo:")
    print(crea_riepilogo(APPARATI))

    aggiorna_stato("NAV-01", "attenzione")
    print("\nRiepilogo dopo l'aggiornamento di NAV-01:")
    print(crea_riepilogo(APPARATI))


if __name__ == "__main__":
    main()
