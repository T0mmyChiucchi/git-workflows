# Laboratorio 3 - GitHub: remote, Issues e Pull Request

## Scenario

Il gruppo pubblica un piccolo calcolatore su GitHub. Il lavoro viene organizzato con Issues e ogni modifica arriva in `master` tramite Pull Request.

## Preparazione GitHub

1. Un componente crea una repository pubblica vuota, senza inizializzarla con README.
2. Gli altri componenti vengono aggiunti come collaboratori.
3. Dal repository locale:

   ```bash
   git remote add origin https://github.com/ACCOUNT/calcolatore.git
   git branch -M master
   git push -u origin master
   ```

4. Un componente esegue `git clone URL` in una nuova cartella. Tutti controllano `git remote -v`.

## Workflow Issue -> branch -> PR

1. Aprite Issue `#1` per la somma e assegnatela a uno studente. Create `features/somma`:

   ```bash
   git checkout master
   git pull origin master
   git checkout -b features/somma
   ```

2. Implementate la funzione, eseguite il programma, poi usate `git diff`, `git add`, `git diff --staged` e commit. Collegate il commit con `#1` nel messaggio.
3. Pubblicate il branch con `git push -u origin features/somma` e aprite una Pull Request verso `master`.
4. Un compagno fa code review, lascia un commento e approva. Dopo il merge, tutti aggiornano:

   ```bash
   git checkout master
   git pull origin master
   git fetch
   ```

5. Aprite una Issue per una divisione per zero, sviluppate `fixes/divisione-zero` e ripetete il workflow. La PR deve contenere `Closes #2`.
6. Esercitate `git show <commit>` per illustrare nella PR quale commit ha risolto il problema.

## Consegna

- URL della repository;
- due Issues chiuse e due PR completate;
- almeno una review significativa;
- output di `git fetch`, `git pull origin master` e `git log --graph --oneline`;
- screenshot della repository e delle impostazioni di collaborazione, senza pubblicare token o credenziali magari.
