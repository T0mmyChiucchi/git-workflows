# Laboratorio 2 bis - Pascal avionics: branch e stash

## Scenario

Realizzate una piccola applicazione Python da terminale per consultare lo stato di alcuni aeromobili di una flotta. Per ogni aereo registrate codice identificativo, modello, ore di volo e stato dei controlli. L'applicazione segnala quali aeromobili richiedono un'ispezione.

## Obiettivi Python

- Rappresentare ogni aeromobile con un dizionario, per esempio `{"codice": "I-ABC", "modello": "A320", "ore_volo": 1240, "controlli_ok": True}`.
- Conservare gli aeromobili in una lista di dizionari.
- Usare list comprehension per ottenere l'elenco degli aeromobili con controlli non validi e quello di quelli oltre la soglia di ore indicata dal gruppo.
- Stampare i risultati in modo leggibile e gestire il caso in cui non ci siano segnalazioni.
- Inserire almeno quattro aeromobili di esempio, con dati fittizi.


## Ruoli (o solo) e branch

- **Studente A - dati e riepilogo:** lavora su `features/dati-flotta`. Completa la lista `aeromobili` fino ad almeno quattro dizionari e implementa `stampa_riepilogo(aeromobili)`. Aggiunge prima i dati, poi il riepilogo, con almeno due commit.
- **Studente B - segnalazioni:** lavora su `features/segnalazioni`. Implementa `filtra_controlli_non_validi(aeromobili)` e `filtra_oltre_soglia(aeromobili, soglia)` usando una list comprehension per ciascun filtro. Fa almeno due commit.
- **Studente C - integrazione e test:** prepara il branch principale (`main`) con `SOGLIA_ORE` e due dizionari iniziali, concorda chiavi e interfacce con A e B, integra le feature, aggiunge un punto di ingresso per stampare riepilogo e segnalazioni e prova i casi manuali. Per una correzione emersa durante la prova usa `fix/gestione-lista-vuota`.

Il branch principale è la base condivisa: A e B partono dallo stesso commit iniziale e non modificano direttamente `main`. Prima di iniziare, concordate l'interfaccia: nome del file (`monitoraggio.py`), lista `aeromobili`, chiavi dei dizionari (`codice`, `modello`, `ore_volo`, `controlli_ok`), costante `SOGLIA_ORE` e nomi/parametri delle funzioni assegnate.

## Procedura

### 1. Preparare il repository condiviso

Lo Studente C crea un repository remoto vuoto (per esempio su GitHub), lo clona e prepara `monitoraggio.py` con `SOGLIA_ORE` e due dizionari fittizi nella lista `aeromobili`. Pubblica il commit iniziale su `main`:

```bash
git clone <URL-del-repository>
cd <cartella-del-repository>
git add monitoraggio.py
git commit -m "chore: prepara monitoraggio flotta"
git push -u origin main
```

Gli Studenti A e B clonano lo stesso repository. Prima di creare il proprio branch, ciascuno aggiorna i riferimenti remoti e porta in locale l'ultimo `main`:

```bash
git fetch origin
git switch main
git pull origin main
```

`fetch` scarica gli aggiornamenti e aggiorna i riferimenti remoti senza integrare modifiche nel branch corrente; `pull` scarica e integra gli aggiornamenti nel branch corrente. In questo passaggio si usa prima `fetch` per controllare gli aggiornamenti disponibili e poi `pull` su `main` per allineare la copia locale.

### 2. Sviluppare le feature in parallelo

Lo Studente A crea il proprio branch partendo da `main` aggiornato:

```bash
git switch -c features/dati-flotta
```

Inserisce almeno quattro dizionari nella lista concordata e implementa il riepilogo. Verifica il programma, crea almeno due commit con messaggi descrittivi e pubblica il branch:

```bash
python monitoraggio.py
git add monitoraggio.py
git commit -m "feat: aggiunge i dati della flotta"
git add monitoraggio.py
git commit -m "feat: stampa il riepilogo degli aeromobili"
git push -u origin features/dati-flotta
```

Lo Studente B, in parallelo, crea `features/segnalazioni` da `main` aggiornato. Implementa due list comprehension: una per `controlli_ok` uguale a `False`, una per `ore_volo` superiori alla soglia. Le funzioni restituiscono liste e ricevono i dati come parametri; C le chiamerà durante l'integrazione. Prova i filtri sui due dizionari iniziali e pubblica il branch con almeno due commit:

```bash
git switch main
git pull origin main
git switch -c features/segnalazioni
git add monitoraggio.py
git commit -m "feat: filtra i controlli non validi"
git add monitoraggio.py
git commit -m "feat: segnala il superamento della soglia ore"
git push -u origin features/segnalazioni
```

### 3. Usare `stash` per una modifica fuori contesto

Durante il lavoro su `features/segnalazioni`, lo Studente B inizia una modifica non pronta alla documentazione, ma deve passare temporaneamente a `main` per controllare il lavoro integrato. Prima controlla le modifiche e le mette da parte localmente:

```bash
git status
git stash push -m "WIP: istruzioni di avvio"
git switch main
git fetch origin
git pull origin main
```

Dopo aver terminato il controllo, torna sul branch corretto e recupera la modifica:

```bash
git switch features/segnalazioni
git stash list
git stash pop
git status
```

`git stash` conserva temporaneamente modifiche locali non committate; non le pubblica sul server. `git stash pop` le riapplica e rimuove la voce recuperata dallo stash. Se si vuole riapplicare la modifica conservando la voce, si può usare `git stash apply`.

### 4. Integrare e aggiornare con `fetch` e `pull`

Lo Studente C controlla i branch pubblicati e integra prima i dati, poi le segnalazioni. Per simulare una collaborazione reale, prima di ogni merge aggiorna i riferimenti remoti con `fetch`; gli altri studenti aggiornano `main` con `pull` dopo ogni integrazione.

```bash
git switch main
git fetch origin
git log --oneline --graph --all
git merge origin/features/dati-flotta
git push origin main
```

Prima di integrare la seconda feature, C controlla i nuovi riferimenti e unisce il branch delle segnalazioni:

```bash
git fetch origin
git merge origin/features/segnalazioni
git push origin main
```

A e B aggiornano poi la propria copia locale del branch principale:

```bash
git switch main
git fetch origin
git pull origin main
```

Se il merge segnala conflitti nello stesso file, gli studenti coinvolti li risolvono mantenendo dati, riepilogo e filtri funzionanti insieme. Dopo aver verificato il file:

```bash
git add monitoraggio.py
git commit -m "merge: integra monitoraggio e segnalazioni"
git push origin main
```

### 5. Aprire e integrare un branch `fix`

Durante la prova, il gruppo verifica che la lista delle segnalazioni non causi errori quando non ci sono aeromobili da segnalare. Se trova un difetto, lo Studente C crea da `main` aggiornato un branch dedicato:

```bash
git switch main
git pull origin main
git switch -c fix/gestione-lista-vuota
```

Corregge il caso, prova sia una lista con segnalazioni sia una senza, quindi committa e pubblica:

```bash
python monitoraggio.py
git add monitoraggio.py
git commit -m "fix: gestisce liste senza segnalazioni"
git push -u origin fix/gestione-lista-vuota
```

C integra il fix in `main` e lo pubblica:

```bash
git switch main
git fetch origin
git merge --no-ff origin/fix/gestione-lista-vuota
git push origin main
```

### 6. Esercitare la risoluzione o l'annullamento di un merge

Per una prova controllata, A e B modificano la stessa riga di riepilogo in due branch distinti, committano e pubblicano le modifiche. C tenta di integrare entrambi i branch. Osserva i marcatori di conflitto (`<<<<<<<`, `=======`, `>>>>>>>`), concorda una versione che conservi le informazioni utili e completa il merge:

```bash
git add monitoraggio.py
git commit -m "merge: risolve conflitto nel riepilogo"
```

Se il merge è stato avviato per errore e non è ancora stato completato, `git merge --abort` interrompe il merge e riporta il branch allo stato precedente all'operazione. Non usarlo dopo aver completato il merge con un commit.

## Consegna

- `monitoraggio.py` eseguibile con almeno quattro aeromobili fittizi, dizionari e list comprehension.
- Branch `features/dati-flotta`, `features/segnalazioni` e `fix/gestione-lista-vuota` integrati in `main`.
- Cronologia visibile con `git log --oneline --graph --all`.
- Evidenza della prova di `git stash` (`git stash list` e cronologia o screenshot).
- Breve spiegazione della differenza tra `fetch` e `pull`, del recupero con `stash pop` e di `git merge --abort`.
