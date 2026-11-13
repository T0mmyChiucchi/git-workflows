# Simulazione 1

## Domande scritte e Risposte

### 1. Repository locale
**Domanda:** descrivi working tree, staging area e repository. In quale area si trovano le modifiche dopo `git add` e dopo `git commit`?

**Risposta:**
- **Working tree (Directory di lavoro):** è la cartella locale visibile sul disco in cui l'utente crea, modifica ed elimina file. Le modifiche qui presenti non sono ancora salvate nella cronologia Git e sono nello stato *Untracked* (nuovi file) o *Modified* (file già tracciati e modificati).
- **Staging area (o Index):** è l'area intermedia di preparazione. Funziona come un'anteprima del prossimo salvataggio: vi vengono registrati i file o le porzioni di file selezionate dallo sviluppatore tramite il comando `git add`.
- **Repository (.git):** è l'archivio permanente e definitivo. Contiene l'intero grafo della cronologia, i commit immutabili (identificati da un hash SHA), i riferimenti ai branch e i tag.
- **Collocazione delle modifiche:**
  - Dopo `git add`: le modifiche passano dal working tree alla **staging area** (diventano *staged* o pronte al commit).
  - Dopo `git commit`: le modifiche presenti nella staging area vengono scritte e memorizzate permanentemente nel **repository locale** come nuovo commit, e la staging area si svuota.

---

### 2. Branch e integrazione
**Domanda:** spiega la differenza tra `git merge` e `git fetch`. Quando si usa `git stash`?

**Risposta:**
- **Differenza tra `git fetch` e `git merge`:**
  - `git fetch`: interroga il repository remoto (es. GitHub) e scarica tutti i nuovi dati (commit, branch remoti come `origin/main`, tag), ma **non tocca né modifica in alcun modo il branch locale corrente né il working tree**. È un'operazione completamente non distruttiva e sicura.
  - `git merge`: unisce la cronologia di un branch sorgente (es. `origin/main` o un feature branch) all'interno del branch locale in cui ci si trova. Se non è possibile una fusione *fast-forward*, crea un commit di merge; in caso di modifiche incompatibili sulle stesse righe, segnala conflitti da risolvere manualmente. *(Nota: il comando `git pull` equivale proprio all'esecuzione in sequenza di `git fetch` seguito da `git merge`).*
- **Quando si usa `git stash`:**
  - Si usa quando si hanno modifiche in corso nel working tree o nella staging area che non si vogliono o non si possono ancora committare (lavoro incompleto / WIP), ma è necessario cambiare temporaneamente branch (ad esempio per risolvere un bug urgente su `main`, testare codice di un collega o scaricare aggiornamenti remoti). `git stash push` archivia temporaneamente le modifiche riportando la working tree a uno stato pulito; successivamente, con `git stash pop` (o `apply`), le modifiche vengono riapplicate.

---

### 3. GitHub e collaborazione
**Domanda:** descrivi il flusso Issue -> branch -> commit -> push -> Pull Request -> review -> merge.

**Risposta:**
È il flusso di lavoro standard (GitHub Flow / Feature Branch Workflow):
1. **Issue:** su GitHub si apre un ticket (Issue) per documentare il requisito, il bug da risolvere o la nuova feature, assegnandola a uno sviluppatore.
2. **Branch:** lo sviluppatore aggiorna il proprio `main` locale (`git pull`) e crea un branch isolato e tematico (es. `git switch -c features/modello-sensore` o `fixes/stato-invalido`).
3. **Commit:** nel branch creato si scrive il codice, si testano i casi d'uso e si registrano uno o più commit atomici e chiari con `git add` e `git commit -m "..."`.
4. **Push:** si pubblica il branch locale sul server remoto con `git push -u origin <nome-branch>`.
5. **Pull Request (PR):** su GitHub lo sviluppatore apre una Pull Request per proporre l'integrazione del branch in `main`. Nel testo della PR si inserisce il riferimento per la chiusura automatica dell'Issue (es. `Closes #1`).
6. **Review:** i compagni di team esaminano il diff del codice, lasciano commenti, verificano eventuali errori e approvano la richiesta.
7. **Merge:** una volta approvata, la PR viene fusa nel branch `main` e il feature branch remoto può essere eliminato. Tutti i collaboratori riallineano il proprio `main` locale con `git checkout main && git pull`.

---

## Esercizio: Telemetria CubeSat

### File implementati
1. `sensore.py`: definizione della classe `Sensore` con `codice`, `grandezza`, `unita`, `soglia_massima`.
2. `satellite.py`: definizione della classe `Satellite` con gestione del dizionario dei sensori, lista delle letture, calcolo allarmi con confronto strettamente maggiore (`valore > soglia_massima`), filtro `letture_in_allarme()` e metodo `riepilogo()`.
3. `main.py`: istanziazione di `CubeSat Aurora`, tre sensori (`TMP-01`, `BAT-01`, `GYR-01`), letture sotto, sopra e uguali alla soglia, test gestione eccezione `KeyError` per sensore non registrato.

### Esecuzione test
```bash
python3 main.py
```
