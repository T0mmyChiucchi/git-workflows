# Laboratorio 2 - Pascal Avionics

## Scenario

Realizzare in Python un registro di apparati avionici. Il programma mostra lo stato dichiarato degli apparati e produce report.

## Modello dati e interfaccia

Nel dizionario (apparati = {}) `APPARATI`, la chiave è il codice univoco e il valore è un altro dizionario:

```python
APPARATI = {
	"NAV-01": {"nome": "Ricevitore navigazione", "bus": "BUS-A", "stato": "OK"},
	"COM-02": {"nome": "Radio comunicazioni", "bus": "BUS-B", "stato": "ATTENZIONE"},
	"SEN-03": {"nome": "Sensore assetto", "bus": "BUS-A", "stato": "OFFLINE"},
}
```

Gli stati ammessi sono `OK`, `ATTENZIONE` e `OFFLINE`.

## Gruppo e relative responsabilità

- **Studente A, registro:** crea `features/registro-apparati`; implementa `apparati.py` con `APPARATI`, `aggiungi_apparato(...)` e `aggiorna_stato(...)`. Rifiuta codici duplicati e stati non ammessi senza modificare il registro.
- **Studente B, report e fix:** crea `features/report-stato`; implementa `report.py` con `filtra_per_stato(...)` e `filtra_per_bus(...)`, usando una list comprehension per ciascun filtro. Gestisce anche il branch `fixes/stato-non-valido` durante la pausa descritta sotto.
- **Studente C, riepilogo e integrazione:** crea `features/riepilogo`; implementa `riepilogo.py` con `crea_riepilogo(...)`, che restituisce un dizionario con il totale e il conteggio per stato. Prepara `main.py`.

## Sequenza di lavoro

### 1. Creare il repository condiviso

Lo Studente C crea su GitHub una repository vuota e aggiunge gli altri due come collaboratori. Create il primo commit con `README.md`. Tutti clonano la repository; verificate il remote:

```bash
git clone URL_DEL_REPOSITORY
cd avionica-simulata
git remote -v
git status
```

Usate `main` come branch principale, in coerenza con i laboratori precedenti. Prima di iniziare, ogni studente porta il branch locale allo stato remoto:

```bash
git checkout main
git fetch origin
git pull origin main
```

`git fetch` aggiorna i riferimenti remoti senza integrare modifiche nel branch locale; `git pull origin main` scarica e integra gli aggiornamenti in `main`.

### 2. Prima feature: registro (Studente A)

Aprire una Issue per il registro e assegnarla allo Studente A. Dal `main` aggiornato:

```bash
git checkout -b features/registro-apparati
```

Implementare `apparati.py` con almeno i tre apparati di esempio, inserimento e aggiornamento stato. Provare il codice, poi controllare `git status` e `git diff`; fare commit e pubblicare il branch:

```bash
git add apparati.py
git commit -m "feat: aggiunge il registro degli apparati"
git push -u origin features/registro-apparati
```

### 3. Seconda feature e pausa con stash (Studente B)

Lo Studente B crea il branch dal `main` aggiornato:

```bash
git checkout main
git pull origin main
git checkout -b features/report-stato
```

Iniziare `report.py`, implementando e provando almeno `filtra_per_stato(...)`. Prima di aver concluso la feature, simulare l'arrivo della segnalazione urgente descritta al punto 4. La modifica non ancora pronta deve risultare visibile in `git status`.

### 4. Fix urgente: correggere uno stato non valido (Studente B)

La segnalazione dice che `aggiorna_stato(...)` può lasciare dati incoerenti quando riceve uno stato sconosciuto o scritto in minuscolo. Salvare il lavoro non committato del report, senza inserirlo nel branch del fix:

```bash
git status
git stash push -m "WIP report-stato"
git checkout main
git pull origin main
git checkout -b fixes/stato-non-valido
```

In `apparati.py`, normalizzare lo stato ignorando maiuscole/minuscole; se non è ammesso, rifiutare l'aggiornamento e lasciare invariati i dati. Aggiungere una prova per entrambi i casi, poi fare commit, `git push -u origin fixes/stato-non-valido` e aprire una PR. Lo Studente C la revisiona; dopo il merge, lo Studente B aggiorna `main`.

Riprendere il branch del report e recuperare la modifica salvata:

```bash
git checkout features/report-stato
git merge main
git stash list
git stash pop
```

Verificare il codice recuperato con `git status` e completare `filtra_per_bus(...)`. `git stash` conserva modifiche locali non committate: non le pubblica su GitHub e non sostituisce un commit. Se `stash pop` segnala un conflitto, risolverlo, verificare il risultato e poi fare commit.

Completato il report, committare e pubblicare `features/report-stato`; Dopo la review e il merge, tutti eseguono `git fetch origin` e `git pull origin main`.

### 5. Terza feature: riepilogo e integrazione (Studente C)

Lo Studente C crea `features/riepilogo` partendo dal `main` aggiornato. In `riepilogo.py`, implementa `crea_riepilogo(...)`: il risultato deve contenere il totale degli apparati e quanti sono `OK`, `ATTENZIONE` e `OFFLINE`. Completa `main.py` mostrando registro, report per stato o bus e riepilogo, senza duplicare la logica dei moduli.

Provare il programma con i dati iniziali e con un aggiornamento di stato. Fare commit, push del branch; gli Studenti A e B fanno la review. Dopo il merge, tutti aggiornano `main` e verificano che il programma funzioni dalla versione clonata.

## Consegna

- repository GitHub con tre branch `features/...` e una branch `fixes/stato-non-valido`, collegate alle rispettive Issue;
- `apparati.py`, `report.py`, `riepilogo.py` e `main.py` funzionanti;
- uso verificabile di dizionari annidati e list comprehension nei filtri;
- test/prove per inserimento, filtri, riepilogo e fix degli stati;
- cronologia `git log --graph --oneline --all` e prova della sequenza `fetch`/`pull`;
- prova di `git stash list` e descrizione di cosa è stato salvato e ripristinato;
- tabella con studente, Issue, branch, commit e PR.
