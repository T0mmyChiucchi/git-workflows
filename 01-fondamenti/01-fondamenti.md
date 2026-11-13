# Laboratorio 1 - Dal file al commit

## Scenario

Realizzazione di un piccolo registro di voti in Python per comprendere e distinguere i tre stati fondamentali di Git: **working tree**, **staging area** e **repository**.

## Procedura Git eseguita

1. **Inizializzazione e primo commit:**
   ```bash
   git init
   git status
   git add registro_voti.py
   git diff --staged
   git commit -m "feat: crea registro voti"
   ```

2. **Aggiunta del calcolo della media ed esito:**
   ```bash
   git diff
   git add registro_voti.py
   git commit -m "feat: calcola media ed esito voti"
   git log --graph --oneline
   git show HEAD
   ```

3. **Simulazione errore e ripristino con reset/reflog:**
   ```bash
   # Modifica non voluta o commit errato
   git reflog
   git reset --hard HEAD@{1}
   ```

---

## Consegna Teorica e Tecnica

### 1. Differenza tra Working Tree, Staging Area e Repository

- **Working Tree (Area di lavoro):**
  È la cartella visibile sul filesystem del computer contenente i file fisici su cui lo sviluppatore sta lavorando. Qui i file possono essere modificati, creati o eliminati. Git rileva queste modifiche contrassegnandole come *Untracked* (non tracciate) o *Modified* (modificate ma non ancora pronte per il commit).

- **Staging Area (Index / Area di preparazione):**
  È un'area intermedia trasparente in cui vengono registrate le modifiche tramite `git add`. Rappresenta un'istantanea (snapshot) precisa di ciò che farà parte del *prossimo* commit. Permette di comporre commit logici, selezionando solo alcuni file o porzioni di codice.

- **Repository (.git):**
  È il database permanente di Git in cui sono memorizzati tutti i commit, la cronologia completa del progetto, i rami (branch) e i tag. Una volta eseguito `git commit`, le modifiche registrate nello staging vengono salvate in modo immutabile e tracciabile con un hash univoco (SHA-1/SHA-256).

### 2. Output tipici dei comandi Git

- `git status`: Mostra lo stato dei file nel working tree rispetto alla staging area (file modificati, da aggiungere, untracked).
- `git diff`: Mostra le modifiche tra il working tree attuale e la staging area (differenze non ancora aggiunte con `add`).
- `git diff --staged` (o `--cached`): Mostra le differenze tra la staging area e l'ultimo commit (ciò che verrà inserito nel prossimo commit).
- `git log --graph --oneline`: Mostra la storia lineare dei commit in formato compatto con visualizzazione ad albero dei branch.
