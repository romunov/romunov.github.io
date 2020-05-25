Title: Odkrivanje elementov delovnega razmerja s strani Inšpektorata RS za delo
Date: 2020-05-23 10:48
Modified: 2020-05-23 10:48
Tags: ijz, Python, OCR, tesseract, pypdfocr
Keywords: informacije javnega značaja, elementi delovnega razmerja, zdr-1, inšpekcijski postopek, Python, OCR
Category: IJZ
slug: inspekcijski-postopki-elementi-delovnega-razmerja

<!-- https://docs.getpelican.com/en/stable/content.html -->

Na Inšpektoratu RS za delo so bili tako prijazni, da so mi poslali stiskano in poskenirano tabelo zaključnenih dokumentov inšpekcijskih nadzorov, ki se tičejo ugotavljanja elementov delovnega razmerja kot jih opredeljuje [ZDR-1](http://pisrs.si/Pis.web/pregledPredpisa?id=ZAKO5944#). Po domače povedano so inšpektorji in inšpektorice pri delodajalcih preverjali, če ima podjetje delavce zaposlene "prek s.p.-ja". 

Z inšpektorata so mi sporočili, da bi ugodenje zahtevi za vse dokumente, ki se tičejo ugotavljanja elementov delovnega razmerja, trajalo dolgo in bi bilo povezano s stroški. Čez to zgodbo že šel z Inšpektoratom RS za notranje zadeve ([kurc enivan?](http://kurc.biolitika.si)), je Urad IP pokazal, da zakon ne predvideva, da se zaračunava stroške, če se zahteva zadevo elektronsko. Ker sem len, sem se odločil, da bom zahteval zadeve _per partes_. Tako so mi poslali lično natiskano in v PDF poskenirano tabelo relevantnih zadev.

Prejet PDF dokument sem spremenil v PDF s pomočjo paketa `pypdfocr` in s `tesseract` prebral številke zadev. Z manjšo skripto sem očistil datoteko. Vse skupaj je trajalo nekaj minut, jaz ne vem kaj si mislijo na Inšpektoratu.

```
import re
import random

with open('./data/seznam_zadev.txt', mode='rt') as rf:
    xy = rf.readlines()

out = []
for line in xy:
    mch = re.search('\d+-\d+', line)
    if mch:
        out.append(mch.group())

xy = []

for line in out:
    if line.startswith('0'):
        xy.append(line)
    else:
        xy.append(line[1:])

with open('./data/spucane_st_zadev.txt', mode='wt') as wf:
    for line in xy:
        wf.writelines(f'{line}\n')

random.seed(357)

random_rows = []
for rng in range(len(xy) - 1):
    random_rows.append(random.randrange(start=0, stop=len(xy)))

[xy[rng] for rng in random_rows]
```

Skripta vrne očiščeno datoteko in seznam zadev. Za te zadeve sem zaprosil in jih tudi dobil po dveh mesecih, verjetno zaradi koronast(r)anja.

```
'010601-201506'
'010606-201812'
'010505-201701'
'010104-201905'
'010611-201605'
'010601-201806'
'011401-201901'
'010506-202001'
'010401-201507'
'011305-201910'
```

# Zadeva 06100-1427/2016
Pri podjetju iz primorske regije, ki se ukvarja s skladiščenjem in pretovarjanjem vozil, je inšpektorat ugotovil, da nima zaposlenih delavcev, na podjetju pa je bilo aktivnih šest delavcev. Ti niso imeli dovolilnice oz. niso zaposleni, imajo pa priglašeno dejavnost samostojnega podjetnika. Delodajalec je inšpektorju pokazal izjave, da delavci ne želijo biti zaposleni pri tem podjetju iz različnih razlogov. Ponudil je tudi dokaz, da jih je želel zaposliti, a te pogodbe delavci niso želeli skleniti. Tale navedba se mi je zdela zanimiva

> ZDR-1 določa, da je potrebno skleniti pogodbo o zaposlitvi, svobodna in vzajemna volja ne more biti v nasprotju z zakonodajo.

# Zadeva 710-2452/2018
Inšpektorica je ugotovila, da med podjetjem in samostojnim podjetnikom obstajajo elementi delovnega razmerja (v nasprotu z drugim odstavkom 13. člena ZDR-1) in izdala plačilni nalog za 1500 EUR globe. Sicer je zagrožena globa je do 8.000,00 EUR.

# Zadeva 06100-1604/2016
Inšpektor z območne enote Celje je javnemu zavodu prepovedal opravljanje dela z delavcem, ki je delal kot samostojni podjetnik. Inšpektor je ugotovil, da obstajajo elementi delovnega razmerja, v ozir pa je vzel tudi pogodbo o izvajanju del.

# Zadeva 710-1032/2019
Podjetje in podjetnik, ki padeta pod pristojnost inšpektorata iz Kranja sta dobila _opomin_, ker je bilo dovoljeno delavcu opravljati delo preko svoje družbe. To naj bi bilo v nasprotju s tretjo točko 217. člena ZDR-1, ki se glasi

> pri njem opravlja delavec delo na podlagi pogodbe civilnega prava v nasprotju z drugim odstavkom 13. člena tega zakona;

Kršitelja morata poravnati stroške postopka v višini 30 EUR.

# Zadeva 06109-7/2015
Murskosoboško-Mariborski inšpektorat je obiskal gostinsko podjetje. Delavka je izjavila, da ni zaposlena, ima s.p. in pogodbo o poslovnem sodelovanju. Inšpektorica je ugotovila, da obstajajo vsi elementi delovnega razmerja po 4. členu ZDR-1 (delavka se je prostovoljno vključena v organiziran delovni proces in s sredstvi delodajalca za plačilo po njegovih navodilih in njegovim nadzorom opravljala delo). Inšpektorica je prepovedala opravljanje dela delavke dokler je ne zaposli skladno s predpisi o zaposlovanju.

# Zadeva 710-1666/2018-3
Kandidat je opravljal delo pooblaščene osebe v imenu za račun v korist in s sredstvi pravne osebe. Inšpektor je presodil, da gre za kršitev 4. člena ZDR-1 in izrekel opomin. Kršiteljici sta morali plačati 30 EUR stroškov postopka.

# Zadeva 710-2628/2017
Podjetje s osebo z s.p.-jem sklenilo pogodbo za opravljanje dela direktorja v imenu in v korist pravne osebe z vsemi elementi delovnega razmerja. Inšpektorica je ugotovila, da gre za kršitev 13. člena ZDR-1. Pravni in odgovorni osebi je izrekla opomin in plačilo 30 EUR stroškov postopka.

# Zadeva 710-3015/2019
Podobno kot za zadevo 710-2628/2017.

# Zadeva 710-917/2019
Podobno kot za zadevo 710-2628/2017, le da je bila izrečena globa 1500 EUR za pravno in 150 EUR za odgovorno osebo. Dodatno so še zaračunali 180 in 70 EUR stroškov postopka za pravno in odgovorno osebo.

# Zadeva 06141-1803/2019-5
Podjetju je inšpektorica prepovedala opravljanje dela na podlagi študentskih napotnic (strežba v lokalu). Inšpektorica je ugotovila, da študentke opravljajo delo v postrežbi v lokalu, ki vsebuje elemente delovnega razmerja. Delodajalcu je bilo naloženo, da v roku treh dni (od prejema odločbe) delavkam izročiti pisno pogodbo o zaposlitvi za delo v strežbi.
