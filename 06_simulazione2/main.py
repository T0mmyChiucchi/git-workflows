from laboratorio import LaboratorioBiotecnologico
from test_biologico import TestBiologico


def main() -> None:
    laboratorio = LaboratorioBiotecnologico("BioLab - Controllo Qualita")
    
    test_esempio = [
        TestBiologico("QC-01", "BIO-24A", "endotossine", 0.8, 1.0, "EU/mL"),
        TestBiologico("QC-02", "BIO-24A", "DNA residuo", 4.2, 10.0, "ng/mL"),
        TestBiologico("QC-03", "BIO-24B", "carica microbica", 120, 100, "CFU/mL"),
        TestBiologico("QC-04", "BIO-24B", "endotossine", 1.0, 1.0, "EU/mL"),
        TestBiologico("QC-05", "BIO-24C", "DNA residuo", 12.0, 10.0, "ng/mL"),
    ]

    print("=== REGISTRAZIONE DEI TEST ===")
    for test in test_esempio:
        laboratorio.registra_test(test)

    print("\n=== RIEPILOGO GENERALE ===")
    laboratorio.riepilogo()

    print("\n=== RICERCA PER CAMPIONE (BIO-24A) ===")
    campione_da_cercare = "BIO-24A"
    risultati = laboratorio.cerca_per_campione(campione_da_cercare)
    if risultati:
        print(f"Test trovati per il campione {campione_da_cercare}:")
        for test in risultati:
            print(f"- {test.codice} | {test.parametro}: {test.valore} {test.unita} -> {laboratorio.esiti[test.codice]}")
    else:
        print(f"Nessun test trovato per il campione {campione_da_cercare}")

    print("\n=== PROVA GESTIONE DUPLICATO ===")
    try:
        laboratorio.registra_test(test_esempio[0])
    except ValueError as errore:
        print(f"Errore previsto gestito correttamente: {errore}")

    print("\n=== PROVA RICERCA CAMPIONE INESISTENTE ===")
    campione_inesistente = "BIO-99Z"
    risultati_inesistenti = laboratorio.cerca_per_campione(campione_inesistente)
    if not risultati_inesistenti:
        print(f"Nessun test trovato per il campione {campione_inesistente} (ricerca vuota gestita correttamente)")


if __name__ == "__main__":
    main()
