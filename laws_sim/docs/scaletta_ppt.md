# Esposizione — dieci minuti

Difesa in presenza, proiettore, commissione mista. Nessun correlatore presente.
Poche domande attese.

---

# 0. Sei regole di consegna

1. **Punta a 9:20, non a 10:00.** Chi cronometra dieci minuti secchi taglia a
   dieci. Novanta secondi in coda sono la differenza fra chiudere e essere
   chiuso. Il testo qui sotto sta in 9:20 letto a voce normale.
2. **Dici sei numeri in tutta l'esposizione.** $0.73$, $0.00$, $+0.250$,
   $+0.280$, $60$ px, dieci minuti di calcolo. Tutto il resto sta sulle slide e
   non va pronunciato. Ogni numero detto a voce è tempo che togli a una frase.
3. **Le slide non sono il testo.** Se una slide contiene una frase che stai per
   dire, togli la frase dalla slide o togli la slide.
4. **Sul prima/dopo, taci per tre secondi.** Fai apparire l'immagine, non parlare,
   lascia guardare. È l'unico momento in cui il silenzio lavora per te.
5. **I limiti li dici tu, al minuto 8:30.** Non è una concessione: chi dichiara
   per primo i limiti del proprio lavoro decide come vengono letti.
6. **Non dire mai «purtroppo», «solo», «non sono riuscito».** I limiti sono
   proprietà del disegno, non fallimenti. Si dicono in indicativo presente.

---

# 1. Scaletta a colpo d'occhio

| Tempo | Slide | Contenuto | Numeri a voce |
|---|---|---|---|
| 0:00–0:15 | 1 | Titolo | — |
| 0:15–1:40 | 2 | Il problema e la domanda | — |
| 1:40–3:05 | 3 | Tre livelli, statuto diverso | — |
| 3:05–5:00 | 4 | Come funziona l'attacco | 60 px, 10 min |
| 5:00–6:35 | 5 | Prima e dopo | 0.73, 0.00 |
| 6:35–8:30 | 6 | I risultati | +0.250, +0.280 |
| 8:30–9:20 | 7 | Limiti e sviluppi | — |
| 9:20 | 8 | Chiusura | — |

Slide di riserva **dopo** la chiusura, per le domande: prima/dopo su VisDrone,
stratificazione per taglia, tabella completa delle metriche, schema del
simulatore.

---

# 2. Slide per slide

## Slide 1 — Titolo · 0:00–0:15

**Sopra:** titolo, nome, relatore, correlatore, anno accademico. Nient'altro.

> Buongiorno. Vi presento il lavoro «Sistemi d'Arma Autonomi Letali: criticità
> nel trattamento dei dati sensibili e analisi sperimentale tra vulnerabilità
> algoritmiche e giuridiche», relatore il professor Buffa, correlatore il
> professor Rivolta.

---

## Slide 2 — Il problema · 0:15–1:40

**Sopra:** una riga sola, grande. *Chi decide che quella figura è un bersaglio?*
Sotto, molto più piccolo, tre parole in fila: `sensore → classificatore →
decisione`. Nessun altro testo.

> Il diritto internazionale umanitario impone il principio di distinzione: chi
> usa la forza deve distinguere un combattente da un civile.
>
> In un sistema d'arma autonomo quella distinzione non la fa una persona. La fa
> una catena tecnica. Un sensore acquisisce, un classificatore attribuisce una
> categoria, una logica decide. Il dibattito giuridico su questi sistemi discute
> a lungo di chi risponda della decisione. Discute molto meno del presupposto su
> cui la decisione si regge, cioè che il riconoscimento sia affidabile.
>
> Il mio lavoro parte da lì. Non chiede se sia legittimo delegare. Chiede quanto
> sia solido l'anello su cui la delega poggia. E lo chiede in modo verificabile:
> costruendo un attacco al canale visivo, e misurando quanto degrada il
> rilevamento di persone da piattaforma aerea.
>
> Un attacco che, va detto subito, è anche una contromisura. Lo stesso artefatto
> che fa fallire il riconoscimento è, dal punto di vista di chi lo indossa, una
> forma di protezione passiva.

---

## Slide 3 — Tre livelli · 1:40–3:05

**Sopra:** lo schema a tre livelli, semplificato al massimo. A destra di ogni
livello una sola parola in grigio: `sperimentale`, `proof-of-concept`,
`proof-of-concept`.

> Il framework ha tre livelli, e hanno statuto diverso. Lo dico subito perché è
> la cosa più importante di questa slide.
>
> Il primo livello è sperimentale. Un rilevatore di persone reale, YOLO nella
> sua versione più leggera, quella che sta a bordo di un drone. Due insiemi di
> dati veri, ripresi da aereo. Statistica inferenziale. Qui i numeri hanno peso.
>
> Il secondo e il terzo livello simulano cosa succede a valle: un ambiente
> multi-agente e una fusione di più fonti informative. Servono a mostrare che
> il degrado percettivo non si ferma al sensore, ma si propaga fino alla
> decisione. Sono prototipi, con quattro difetti che ho accertato leggendo il
> mio stesso codice e che sono dichiarati nella tesi. Non producono risultati
> quantitativi e non li presento come tali.
>
> Fra il primo livello e gli altri due non c'è una condotta continua. C'è un
> file, con dentro due numeri: quanto spesso il rilevatore vede una persona
> prima dell'attacco, e quanto spesso la vede dopo. Il simulatore non contiene
> la rete neurale. Contiene una moneta, il cui sbilanciamento l'ho misurato
> altrove.

---

## Slide 4 — L'attacco · 3:05–5:00

**Sopra:** cinque righe brevissime, numerate, che compaiono una alla volta se
puoi permettertelo. `1. superficie sul corpo` · `2. proporzionale, non fissa` ·
`3. sedici deformazioni` · `4. minimizza la fiducia` · `5. una sola patch, tutti
i fotogrammi`. In basso a destra la patch nuda, piccola.

> L'avversario che ho modellato è debole. Non entra nei sistemi del velivolo,
> non conosce i pesi della rete, non tocca i dati di addestramento. Ha una cosa
> sola: una superficie stampata da indossare. È il caso peggiore per lui, ed è
> anche il più realistico.
>
> Cinque scelte.
>
> Primo, la perturbazione sta sul torace, perché è l'unica parte di scena che
> chi la indossa controlla davvero.
>
> Secondo, occupa una frazione fissa del corpo e non un numero fisso di pixel.
> Un indumento scala con la persona. Su un bersaglio ripreso dall'alto, alto
> sessanta pixel, questo significa che la superficie ottimizzata arriva al
> rilevatore come poche centinaia di pixel. Tenete a mente questo numero:
> spiega quasi tutto quello che viene dopo.
>
> Terzo, ogni immagine viene mostrata sedici volte, ruotata, riscalata,
> alterata nei colori. Si ottimizza la media su tutte e sedici, non il caso
> fortunato. Serve perché una perturbazione che funziona solo in condizioni
> ideali non sopravvive alla stampa su tessuto.
>
> Quarto, l'obiettivo non è ingannare la rete facendole vedere altro. È
> abbassare la fiducia con cui riconosce la persona, fino a portarla sotto la
> soglia oltre la quale il sistema dichiara di aver visto qualcuno.
>
> Quinto, la patch è una sola. Non è ricalcolata per ogni immagine: è la stessa
> per tutte. È la differenza fra un esperimento di laboratorio e qualcosa che si
> potrebbe stampare una volta e indossare.
>
> Il tutto gira su un portatile. Dodici ore di calcolo, che diventano tre o
> quattro sfruttando l'acceleratore grafico.

---

## Slide 5 — Prima e dopo · 5:00–6:35

**Sopra:** solo `idx5525`, a piena larghezza. Didascalia in corpo minimo con
l'attribuzione: *Okutama-Action (Barekatain et al., 2017), CC BY-NC-SA 3.0.*
Nessun'altra scritta.

> *[Fai apparire l'immagine. Conta fino a tre. Non parlare.]*
>
> Stesso fotogramma. A sinistra il sistema senza perturbazione: riconosce la
> persona con fiducia zero virgola settantatré. A destra, con la patch
> applicata: zero.
>
> Guardate però gli altri riquadri. In questa scena ci sono altre cinque
> persone. Nessuna indossa la patch, e tutte e cinque restano riconosciute,
> prima e dopo. L'effetto è locale: agisce sul soggetto che porta la
> perturbazione e non sul resto della scena.
>
> Questo è un caso singolo, e da solo non dimostra niente. Serve a farvi vedere
> che aspetto ha il fenomeno. Quanto sia sistematico lo dice la slide dopo.

---

## Slide 6 — I risultati · 6:35–8:30

**Sopra:** il pannello (b) dei due forest plot affiancati, ridotto a tre righe —
Evasion rate, Sensitività, Specificità. Titoli dei due riquadri: `VisDrone
(immagini statiche)` e `Okutama-Action (video)`. Linea dello zero tratteggiata,
ben visibile.

> Questo grafico va letto una volta sola, e poi si legge da sé.
>
> Ogni rombo nero è il cambiamento prodotto dall'attacco. La barra orizzontale è
> l'incertezza della misura. La linea tratteggiata è lo zero, cioè «nessun
> effetto». Se una barra attraversa la linea, l'effetto misurato potrebbe essere
> dovuto al caso.
>
> Prima riga, la frazione di persone che il sistema non vede. A sinistra, su
> immagini statiche in contesto urbano, l'attacco la aumenta di venticinque punti
> percentuali. A destra, su sequenze video riprese in un contesto tutto diverso,
> di ventotto. Nessuna delle due barre tocca lo zero.
>
> Il punto non è quanto siano grandi quei due numeri. È che siano **due**, e
> vicini. Sono due domini indipendenti, con risoluzioni diverse, altitudini
> diverse, scene diverse. La misura si replica.
>
> Terza riga, la specificità: quanto il sistema evita di vedere persone dove non
> ce ne sono. Non si muove. E non si muove per una ragione strutturale, non
> perché l'attacco sia elegante: quella riga è calcolata sui fotogrammi in cui
> non c'è nessun bersaglio, e su quei fotogrammi la patch non viene mai
> applicata. L'immagine è identica nelle due condizioni. Lo dico perché è la
> lettura sbagliata più facile da fare guardando questo grafico.

---

## Slide 7 — Limiti e sviluppi · 8:30–9:20

**Sopra:** due colonne. A sinistra `Cosa questo lavoro non dice`, quattro righe
telegrafiche. A destra `C.A.R.E. Kit — sviluppo futuro`, una riga.

> Quattro cose che questo lavoro non dice, e voglio dirle io.
>
> L'attacco è stato valutato in digitale. La perturbazione è vincolata a essere
> riproducibile a stampa, ma su tessuto reale non l'ho provata.
>
> L'ottimizzazione conosceva il modello che avrebbe attaccato. I numeri che vi
> ho mostrato sono quindi un limite superiore, non una stima di quanto
> funzionerebbe contro un rilevatore sconosciuto.
>
> L'ottimizzazione non è stata ripetuta con inizializzazioni diverse. Ho
> evidenza indiretta di stabilità — sei configurazioni che convergono, e la
> replica su un secondo dominio — ma non ho la prova diretta.
>
> E il regime dei bersagli molto grandi, quelli che occupano una porzione ampia
> dell'immagine, resta non testato su entrambi i domini.
>
> La direzione futura è il C.A.R.E. Kit: un dispositivo indossabile completo di
> cui la perturbazione caratterizzata qui è la sola componente percettiva.

---

## Slide 8 — Chiusura · 9:20

**Sopra:** una frase sola, in nero su bianco.

> Chiudo con la cosa che mi ha colpito di più, e che non era nel piano iniziale.
>
> Sullo stesso insieme di dati, **senza nessun attacco**, cambiando soltanto la
> soglia di fiducia oltre la quale il sistema dichiara di aver visto una
> persona, la frazione di persone non rilevate passa da meno del quattro
> percento a oltre il settanta.
>
> Un singolo parametro, privo di qualunque significato semantico, deciso da chi
> configura il sistema, ridefinisce interamente chi il sistema considera
> presente nella scena.
>
> Quello che emerge da questo lavoro non è una contromisura pronta all'uso. È
> una misura di quanto sia fragile il presupposto di fatto su cui l'intera
> delega si regge.
>
> Grazie.

---

# 3. Cosa non dire

- **Non dire «l'attacco funziona meglio su Okutama».** Non è vero: cambia la
  linea di base, non l'efficacia. Se ti scappa in esposizione, te lo chiedono.
- **Non dire «la specificità non cambia perché l'attacco è pulito».** È la
  risposta sbagliata e la slide 6 te la mette in bocca. Il testo sopra la
  disinnesca già.
- **Non nominare la metrica dei rilevamenti spuri.** Costa quaranta secondi
  spiegarla, richiede la correzione di Bonferroni, e su un dominio il risultato
  è ritirato. Se la chiedono, la risposta è pronta; in esposizione, no.
- **Non nominare CEAE.** È fra gli sviluppi futuri e non è nei risultati.
- **Non giustificare la visibilità della patch.** Se nessuno chiede, non è un
  problema. Se qualcuno chiede, la risposta è che non è mimetismo percettivo ma
  una perturbazione ottimizzata contro un rilevatore, e la sua visibilità a
  occhio umano è irrilevante rispetto all'obiettivo.

---

# 4. Lista di taglio, in ordine

Se al minuto 7 sei indietro, togli in quest'ordine. Ogni voce è già scritta in
modo da poter sparire senza lasciare buchi.

1. La riga sulle dodici ore di calcolo (slide 4). Vale 8 secondi.
2. Il quinto punto della slide 4, «una sola patch». Vale 20 secondi. Costoso,
   perché è un punto di merito — ma è il primo che puoi sacrificare.
3. Il quarto limite, i bersagli grandi (slide 7). Vale 12 secondi.
4. Il capoverso «questo è un caso singolo» della slide 5. Vale 12 secondi.

Non tagliare mai: il paragrafo sulla specificità (slide 6), i primi due limiti
(slide 7), la chiusura sulla soglia (slide 8).

---

# 5. Le due frasi da sapere a memoria

Solo queste. Il resto può essere detto con parole tue.

**L'apertura del blocco sui livelli:**

> «Il simulatore non contiene la rete neurale. Contiene una moneta, il cui
> sbilanciamento l'ho misurato altrove.»

**La chiusura:**

> «Quello che emerge da questo lavoro non è una contromisura pronta all'uso. È
> una misura di quanto sia fragile il presupposto di fatto su cui l'intera
> delega si regge.»

---

# 6. Da preparare prima

- [ ] Cronometrare a voce alta due volte. La prima esce lunga sempre.
- [ ] Generare il pannello (b) ridotto a tre righe per la slide 6.
- [ ] Preparare le quattro slide di riserva dopo la chiusura.
- [ ] Verificare la resa del prima/dopo proiettato: la patch deve leggersi
      dall'ultima fila.
