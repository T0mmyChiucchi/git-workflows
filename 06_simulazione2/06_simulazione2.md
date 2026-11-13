# Simulazione 2

## Domande scritte e Risposte

### 1. Repository locale
**Domanda:** descrivi working tree, staging area e repository. In quale area si trovano le modifiche dopo `git add` e dopo `git commit`?

**Risposta:**
- **Working tree:** è lo spazio di lavoro locale effettivo (la cartella di file su disco). Tutte le creazioni, cancellazioni e modifiche al codice avvengono qui e sono inizialmente non tracciate o non salvate in cronologia.
- **Staging area (Index):** è l'area di staging/preparazione in cui si raggruppano le modifiche selezionate per il prossimo commit. Consente di preparare commit logici, mirati e atomici.
- **Repository (.git):** è il database locale permanente contenente tutti i commit storici con i relativi alberi di file, autori, date, hash crittografici, branch e tag.
- **Collocazione delle modifiche:**
  - Dopo `git add <file>`: le modifiche passano dal working tree alla **staging area**.
  - Dopo `git commit -m "..."`: le modifiche passano dalla staging area al **repository locale** sotto forma di un nuovo commit immutabile.

---

### 2. Branch e integrazione
**Domanda:** spiega la differenza tra `git merge` e `git fetch`. Quando si usa `git stash`?

**Risposta:**
- **Differenza tra `git fetch` e `git merge`:**
  - `git fetch`: scarica le novità e i metadati dal server remoto (aggiornando rami remoti come `origin/main`), ma **non modifica i branch locali né il codice nella working tree**. È un controllo informativo sicuro.
  - `git merge`: integra le modifiche di un branch sorgente nel branch di destinazione attualmente attivo. Se vi sono conflitti di modifica sulle stesse righe, richiede l'intervento manuale per risolverli prima di finalizzare il commit di fusione.
- **Quando si usa `git stash`:**
  - Si usa quando si ha del codice parziale o non pronto nel working tree e occorre cambiare contesto/branch (es. per verificare un bug, cambiare branch o sincronizzarsi con `pull`) senza committare lavoro incompleto. `git stash push` archivia le modifiche lasciando la working tree pulita; `git stash pop` le estrae e le riapplica sul branch di lavoro.

---

### 3. GitHub e collaborazione
**Domanda:** descrivi il flusso Issue -> branch -> commit -> push -> Pull Request -> review -> merge.

**Risposta:**
1. **Issue:** traccia l'attività, il requisito o il bug da affrontare.
2. **Branch:** creazione di un ramo dedicato partendo dall'ultimo `main` (`git switch -c features/...`).
3. **Commit:** sviluppo del codice con commit frequenti, atomici e con messaggi chiari.
4. **Push:** caricamento del ramo locale sul repository remoto (`git push -u origin <branch>`).
5. **Pull Request:** proposta formale di integrazione delle modifiche in `main`, collegando la relativa Issue (es. `Closes #1`).
6. **Review:** revisione del codice da parte di un collega/peer (commenti, richieste di modifica o approvazione).
7. **Merge:** integrazione definitiva del ramo nel branch `main`, chiusura automatica dell'Issue e cancellazione del ramo di feature.

---

## Esercizio: Controllo Qualità Laboratorio Biotecnologico

### File implementati
1. `test_biologico.py`: classe `TestBiologico` con attributi tipizzati e metodo `esito()` (`CONFORME` se `valore <= limite_massimo`, altrimenti `FUORI SPECIFICA`).
2. `laboratorio.py`: classe `LaboratorioBiotecnologico` con lista test, dizionario degli esiti, prevenzione codici duplicati (`ValueError`), ricerca per campione case-insensitive e metodo `riepilogo()`.
3. `main.py`: dimostrazione completa con 5 test di esempio, riepilogo con conteggio conformi/fuori specifica, ricerca campione, gestione duplicati e ricerca senza risultati.

### Esecuzione test
```bash
python3 main.py
```
