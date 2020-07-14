# GNSSLiguria_download
 Script to automatically download GNSS observation files from Regione Liguria's GNSS network
 
 Lo script integra una funzione per scaricare in maniera automatica i dati RINEX dalla rete di stazioni permanenti di Regione Liguria.
 
 La funzione richiede in input:
 
 - nome della stazione (può essere una stringa o una lista)
 - data: stringa con formato 'yyyy/mm/dd'
 - rate: è un intero che può valere 1, 5 o 30 (secondi)
 - ore: è una stringa o una lista (contenente le lettere dell'alfabeto dalla a alla x)
 - tipo di osservazioni: può essere una strina o una lista con le tipologie di osservabili desiderate (obs, nav o gnav)
 
 ## Modalità di scaricamento file

Per scaricare il file obs giornaliero di genu a 30 secondi, relativo al 2 Giugno 2020, la funzione deve essere chiamata in questo modo 

```
GNSS_download('genu','2020/06/02',30,'a','obs')
```
nb: in questo caso la 'a' è inutile ma non può essere omessa

Se oltre al file obs si vuole scaricare anche il navigazionale (nav), la funzione deve essere chiamata in questo modo

```
GNSS_download('genu','2020/06/02',30,'a',['obs','nav'])
```

Se oltre a genu si vogliono scaricare gli stessi file anche per chiv (ad esempio), la funzione deve essere chiamata in questo modo

```
GNSS_download(['genu','chiv'],'2020/06/02',30,'a',['obs','nav'])
```
I file orari sono disponibili solo per rate = 1s. Se si volesse scaricare il file orario di genu dalle 00:00 alle 00:59 del 2 Giugno 2020, la funzione deve essere chiamata in questo modo

```
GNSS_download('genu','2020/06/02',30,'a','obs')
```
Se si volessero scaricare ore diverse basta sostituire la 'a' con la lista delle ore desiderate (i nomi delle ore corrispondono alle lettere dell'alfabeto come da convenzione IGS per i nomi dei file RINEX 2.11). Ad esempio:

```
GNSS_download('genu','2020/06/02',30,['a','b','f'],'obs')
```
NB: non è necessario che le lettere siano consecutive.

Se la funzione viene chiamata senza input:

```
GNSS_download()
```
sono settati gli input di default come segue:

```
GNSS_download(station=['baja','loan','camn','genu','chiv','beve'],date='2020/01/01',rate=30,hour=[c for c in ascii_lowercase[:-2]],obs_type=['obs','nav','gnav'])
```
dove la lista hour corrisponde a tutte le lettere dell'alfabeto dalla a alla x.

## Estrazione file compressi

E' stata implementata anche l'estrazione dei file che, di default, vengono scaricati compressi (.Z). Tale funzione però funziona solo sui sistemi UNIX 
In questo modo si hanno a disposizione i file .yyd (file di osservabili hatanakato) .yyn (navigazionale GPS) e .yyg (navigazionale GLONASS)

## Hatanaka

Funzione per estrarre un file di osservabili compresso con Hatanaka: .yyd --> .yyo
Se si esegue la funzione dallo script GNSS_download.py, bisognerà settare i vari input nel main. Lo script scarica quindi i file richiesti nella stessa cartella dove è salvato.

