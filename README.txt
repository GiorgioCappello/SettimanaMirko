Project 3: TO-DO LIST

Description: Simulation of a task management system.

MEMBRI DEL TEAM 3:
-Franco Rinaldi - https://github.com/jalt1990
-Carlo Schiano Di Cola - https://github.com/tbnh62
-Monica Parmigiani - https://github.com/monicaparmigiani
-Giorgio Cappello - https://github.com/GiorgioCappello

TEAMWORKING RIFERITO AD ANALISI E SVILUPPO DI APP GESTIONE TASK CON SERVIZI CRUD

REGOLE DI GRUPPO

COORDINAMENTO INTERNO:
requisiti individuale preliminare e brainstorming collettivo;
pianificazione del tempo durante il brainstorming;
pianificazione delle task urgenti;
comunicazioni agili eliminando barriere gerarchiche con il massimo rispetto reciproco;
gestione dello sprint in base alle tempistiche con assegnazione task.
COMMIT ON GITHUB:
pull a inizio lavoro, con file separati;
push dei file personali sulla cartella condivisa ogni aggiornamento importante;
il teamleader, o chi per sua vece, ha l'onere di unire i file compositi;
le cancellazioni solo ed esclusivamente se decise in gruppo.
DOVE E QUANDO INSERIRE I COMMENTI:
uno per definire classe o funzione al di sopra delle stesse;
laterale se corti;
accanto agli script in caso di necessità per spiegare l'algoritmo;
a più righe se il blocco è particolarmente complesso da leggere.
CLEAN CODE:
nomi delle variabili con underscore;
nomi delle Classi e delle funzioni in camelCase;
nomi che abbiano un significato coerente;
raggruppamento del codice in base al tipo (classi, funzioni, test, etc...).
FEATURES DA IMPLEMENTARE:
possibilità di implementare più liste, ognuna con nome di riferimento o di categoria, con relativa data di scadenza e le diverse task all'interno;
inserimento di un alert per i giorni mancanti alla scadenza;
inserimento di un filtro controllo per le task e le liste attive, mostrando anche una deadline;
inserimento di un filtro task scaduta/non scaduta;
inserimento di un sistema di comunicazione con app calendario esterne;
implentazione di funzione di import/export per file di backup;
ordinamento delle liste per priorità, scadenza, o da completare;
visualizzazione del progressivo dell'esecuzione delle liste (in percentuale);
gestione di più profili (nome utente e password).
MANUALE DI ISTRUZIONI - REALEASE 2.0

L'app si avvia dal menu di accesso (1)

MENU DI ACCESSO
Nel menu di Accesso appare il seguente messaggio di Benvenuto che invita a entrare nell'App o a uscire da essa:

Benvenuto nell' App della To Do List

Entra
Esci
1.1 --> Entra

Una volta entrati nell' app appare il menu Principale con le seguenti funzioni:

Benvenuto nell' App della To Do List.

Aggiungi una task
Visualizza tutte le task
Elimina Task
Modifica la Task
Aggiorna Status della Task
Torna indietro
1.1.1 --> Aggiungi una task

Permette di creare una task specificandone il contenuto, la data di scadenza, e la priorità (facoltativa). Torna poi al Menu di Benvenuto (1.1 Entra)

1.1.2 --> Visualizza tutte le task

Permette di visualizzare le singole task finora memorizzate all'interno della Lista Task dell' App. Se la lista è vuota, visualizza un messaggio che dichiara l'assenza di task. Torna poi al Menu di Benvenuto (1.1 Entra)

1.1.3 --> Elimina Task

Se la lista delle task ha almeno un elemento, permette di eliminare una task dalla Lista delle task selezionandola tramite l'indice di riferimento. Se la lista è vuota, riporta un messaggio di avviso. Torna poi al Menu di Benvenuto (1.1 Entra)

1.1.4 --> Modifica la Task

Se la lista delle task ha almeno un elemento, permette di modificare una task dalla Lista delle task selezionandola tramite l'indice di riferimento.

Una volta selezionata la task da modificare, appare il seguente menu di modifica:

Questa è l'area di modifica:

Modifica completa di una task
Modifica solo un elemento di una task
Torna indietro
1.1.4.1 --> Modifica completa di una task

Arriveranno dei messaggi di inserimento input all'utente per indicare il contenuto della task, i dati della scadenza, e la priorità aggiornata, per modificare completamente il task precedentemente selezionato. Torna poi al Menu di Benvenuto (1.1 Entra)

1.1.4.2 --> Modifica solo un elemento di una task

Apparirà all' utente il seguente menu di navigazione:

Questa è l'area di modifica parziale:

Modifica contenuto
Modifica scadenza
Modifica priorita
Torna indietro
L'utente potrà selezionare cosa modificare della task precedentemente indicata. In base alla selezione, avverrà la modifica e il task verrà visualizzato aggiornato. Alla fine di qualsiasi modifica fatta si torna in loop a questo menu (1.1.4.2) finchè l'utente non seleziona 0 che riporta al Menu di Benvenuto (1.1 Entra)

1.1.4.0 --> Torna indietro

riporta al Menu di Benvenuto (1.1 Entra)

1.1.5 --> Aggiorna Status della Task

Se la lista delle task ha almeno un elemento, permette di aggiornare lo status di una task dalla Lista delle task selezionandola tramite l'indice di riferimento. Eseguita l'operazione, viene visualizzata la task aggiornata con lo status, e si torna poi al Menu di Benvenuto (1.1 Entra)