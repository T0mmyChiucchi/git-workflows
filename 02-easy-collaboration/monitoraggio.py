"""
Soluzione per il monitoraggio flotta del laboratorio 2 bis.
La soglia concordata per le ore di volo è di 1.000 ore.
"""

SOGLIA_ORE = 1000

# Elenco degli aeromobili della flotta
aeromobili = [
    {"codice": "I-ABC", "modello": "A320", "ore_volo": 1240, "controlli_ok": True},
    {"codice": "I-DEF", "modello": "B737", "ore_volo": 860, "controlli_ok": False},
    {"codice": "I-GHI", "modello": "A220", "ore_volo": 1035, "controlli_ok": True},
    {"codice": "I-JKL", "modello": "ATR72", "ore_volo": 540, "controlli_ok": True},
]


def stampa_riepilogo(aeromobili) -> None:
    """Stampa tutte le informazioni sugli aeromobili."""
    print("Riepilogo flotta:")

    for aeromobile in aeromobili:
        print(
            f"- {aeromobile['codice']} ({aeromobile['modello']}), "
            f"{aeromobile['ore_volo']} ore di volo, "
            f"controlli {'OK' if aeromobile['controlli_ok'] else 'non validi'}"
        )


def filtra_controlli_non_validi(aeromobili: list) -> list[dict]:
    """Restituisce gli aeromobili con controlli non validi."""

    # ALTERNATIVA 1: LIST COMPREHENSION
    return [
        aeromobile
        for aeromobile in aeromobili
        if aeromobile["controlli_ok"] is False
    ]

    # ALTERNATIVA 2: CICLO FOR SENZA LIST COMPREHENSION
    # risultato = []
    #
    # for aeromobile in aeromobili:
    #     if aeromobile["controlli_ok"] is False:
    #         risultato.append(aeromobile)
    #
    # return risultato


def filtra_oltre_soglia(aeromobili: list, soglia: int) -> list:
    """Restituisce gli aeromobili che superano la soglia di ore di volo."""

    # ALTERNATIVA 1: LIST COMPREHENSION
    return [
        aeromobile
        for aeromobile in aeromobili
        if isinstance(aeromobile["ore_volo"], int)
        and aeromobile["ore_volo"] > soglia
    ]

    # ALTERNATIVA 2: CICLO FOR SENZA LIST COMPREHENSION
    # risultato = []
    #
    # for aeromobile in aeromobili:
    #     if (
    #         isinstance(aeromobile["ore_volo"], int)
    #         and aeromobile["ore_volo"] > soglia
    #     ):
    #         risultato.append(aeromobile)
    #
    # return risultato


def stampa_segnalazioni(titolo: str, segnalazioni: list) -> None:
    """Stampa le segnalazioni oppure un messaggio se non ce ne sono."""
    print(f"\n{titolo}:")

    if not segnalazioni:
        print("Nessuna segnalazione.")
        return

    for aeromobile in segnalazioni:
        print(f"- {aeromobile['codice']} ({aeromobile['modello']})")


def main() -> None:
    """Esegue tutte le operazioni di monitoraggio della flotta."""

    stampa_riepilogo(aeromobili)
    stampa_segnalazioni("Aeromobili con controlli non validi", filtra_controlli_non_validi(aeromobili))
    stampa_segnalazioni(f"Aeromobili oltre la soglia di {SOGLIA_ORE} ore", filtra_oltre_soglia(aeromobili, SOGLIA_ORE))

if __name__ == "__main__":
    main()

