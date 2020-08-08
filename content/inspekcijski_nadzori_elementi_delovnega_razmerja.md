Title: Odkrivanje elementov delovnega razmerja s strani Inšpektorata RS za delo
Date: 2020-05-23 10:48
Modified: 2020-08-08 11:12
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

> Naslednje zadeve sem prejel dne 2020-06-15

# Zadeva PN 710-68/2019-3
Kratko a jedrnato poročilo in plačilni nalog za 1500 EUR oz 750 EUR za polovičko. Oglobljena je bila lastnica lokala, ker je v lokalu delala delavka neskladno z 2. odstavkom 13. člena Zakona o delovnih razmerjih, saj so obstajali elementi delovnega razmerja.

# Zadeva 06100-1464/2018
Koprska inšpektorica je podjetju prepovedala opravljanje delovnega procesa oz. uporabo sredstev za delo s samostojnim podjetnikom do odprave nepravilnosti. Utemeljuje, da delodajalec omogoča opravljanje dela na podlagi pogodbe civilnega prava na način, da delo s.p.-ja vsebuje vse elemente delovnega razmerja. Inšpektorica odredi, da morata stranki skleniti pogodbo o zaposlitvi.

# Zadeva 06100-2793/2019-7
Mariborska inšpektorica je delodajalcu prepovedala opravljati delo dvema osebama do odprave nepravilnosti. Delavca sta namreč opravljali delo na podlagi pogodbe civilnega prava, njuno delo pa vsebuje vse elemente delovnega razmerja. Ne piše (pobrisano), ali je šlo za fizični osebi ali morda za samostojna podjetnika.

Zanimivo mi je to, da je glava odločble na videz podobna tisti, ki jo je spisala koprska inšpektorica (ali pa je obratno, iz zaključnih zadev težko sklepam).

# Zadeva 06141-576/2018
Inšpektor ugotavlja, da je imel delodajalec z dvema delavkama (s.p.?) sklenjeno pogodbo civilnega prava in da obstajajo elementi delovnega razmerja. Nalaga, da delodajalec uredi delovno razmerje skladno s 54. členom ZDR-1A.

# Zadeva 06141/191/2015-1
Inšpektor delodajalcu prepove opravljanje dela oz delovnega procesa z delavko, s katero ima sklenjeno <pobrisano>, dokler bo pri delodajalcu opravljala delo na način, ki vsebuje elemente delovnega razmerja in tako zagotovi spoštovanje določb 2. odstavka 13. člena ZDR-1.

# Zadeva 710-2567/2017-3
Inšpektorica je izdala opomin in 30 EUR stroškov postopka, ker je podjetje dovolilo delavki opravljati delo na podlagi civilne pogodbe v nasprotju s 13. členom Zakona o delovnih razmerjih, ker vsebujejo elemente delovnega razmerja v skladu s 4. točko v povezavi z 22. členom ZDR-1.

# Zadeva 06100-243/2016
Inšpektorica delodajalcu prepove opravljanje dela z osebo. Sicer je veliko pobrisanega, vendar bi lahko sklepal, da gre za delo na podlagi ("civilne") pogodbe, obstajajo pa tudi elementi delovnega razmerja skladno s 4. in v povezavi z 22. oz. 54. členom Zakona o delovnih razmerjih.

# Zadeva 06139-1670/2016
Inšpektorica delodajalcu prepove opravljana dela oz. opravljanje delovnega procesa v katerem je udeležena delavka s katero ima, ker je pobrisano ugibam, sklenjeno pogodbo. Delo, ki ga delavka opravlja vsebuje vse elemente delovnega razmerja, kar je v nasprotju z 2. odstavkom 13. člena Zakona o delovnih razmerjih.

# Zadeva 06100-157/2015-1
Inšpektor delodajalcu prepove opravljanje dela oz. delovnega procesa z delavcem, ki ima priglašeno dejavnost <pobrisano>. Sklepam, da gre za delo preko s.p.-ja. Prepoved velja dokler delavce pri delodajalcu delo opravlja na način, ki vsebuje elemente delovnega razmerja.

# Zadeva 710-332/2017
Inšpektor pravni in odgovorni osebi očita štiri prekrške od a do č. V dokumentu je nepobrisan samo prekršek a. V prekršku a je očitano, da je bilo delavcu omogočeno delo na podlagi pogodbe civilnega prava, kljub obstoju elementov delovnega razmerja, kar je v nasprotju z 2. odstavkom 13. člena ZDR-1. Pravna oseba je za ta prekršek dobila izrečene 4500 EUR globe, odgovorna pa 450 EUR. Poleg globe je še obračunana sodna taksa 1050 EUR za pravno in 160 za odgovorno osebo.

> Naslednje zadeve sem prejel 2020-07-29

# Zadeva 06139-392/2015-3
Inšpektor delodajalcu prepove opravljanje delovnega procesa z delavcem, ker mu omogoča opravljanje dela na podlagi civilnega prava - pogodbe o opravljanju storitev. Pogodba vsebuje elemente delovnega razmerja, v nasprotju z 2. drugim odstavkom 13. člena Zakona o delovnih razmerjih. Verjetno gre za s.p., a zaradi umika osebnih informacij iz tega dokumenta to nedvoumno ne znam razbrati. V primeru, da delodajalec ne bo odpravil nepravilnosti, je zagrožena globa 4500 EUR za pravno osebo in 350 EUR za odgovorno osebo.

# 06112-811/2014-1
Delavec s priglašeno dejavnostjo v gostinstvu na podlagi pogodbe o sodelovanju pri delodajalcu opravlja delo. Inšpektor je ugotovil, da obstajajo elementi delovnega razmerja po drugem odstavku 13. člena Zakona o delovnih razmerjih. V kolikor delodajalec ne odpravi nepravilnosti, je zagrožena globa 4500 EUR za pravno in 350 EUR za odgovorno osebo.

# 06141-590/2016
Inšpektorica je dvema delavkama s priglašeno dejavnostjo prepovedala opravljanje dela pri delodajalcu, ker je slednji omogočil opravljanje dela na podlagi pogodb civilnega prava, kar je v nasprotju z drugim odstavkom 13. člena Zakona o delovnih razmerjih, saj vsebuje delo vse elemente delovnega razmerja. Zagrožena globa je 4500 EUR za delodajalca in 350 EUR za odgovorno osebo.

# 06100-583/2016
Inšpektor delodajalcu prepove opravljati dela oz. opravljanje delovnega proces in uporabe sredstev za delo z delavko, ki ima priglašeno dejavnost dokler bo pri delodajalcu opravljala delo na način, ki vsebuje elemente delovnega razmerja, kar je v nasprotju z drugim odstavkom 13. člena Zakona o delovnih razmerjih. Zagrožena je kaze 4500 EUR za delodajalca in 350 EUR za odgovorno osebo.

# 06100-1228/2016
Inšpektor je ob inšpekcijskem pregledu ugotovil, da imajo nekateri delavci status (pobrisano, verjetno s.p.), z družbo sklenjeno pogodbo civilnega prava. Inšpektor je ugotovil, da obstajaji vsi elementi delovnega razmerja, kot jih določa 4. člen Zakona o delovnih razmerjih-1 in ni v skladju z drugim odstavkom 13. člena istega zakona. Delodajalec je obljubil, da bo z navedenimi zaposlenimi sklenil pogodbo o zaposlitvi do 2017-01-01, ker potrebuje nekaj časa za spremembo internega akta. Za delodajalca je tudi zagroženakazen 2000 EUR in 200 EUR za neizpolnjevanje pisnega poročila ter 4500 EUR kazni za neizvrševanje določbe za pravno in 350 EUR za odgovorno osebo.

# 710-603/2019-3
V tej zadevi je veliko informacij umaknjenih in je težko razbrati za kaj gre. Da se razbrati, da je pri pravni osebi nekdo opravljal dleo na podlagi pogodbe civilnega prava s čimer je kršila drugi odstavek 13. člena Zakona o delovnih razmerjih-1. Pravni in odgovorni osebi je bil izrečen opomin in vsaki tudi plačilo sodne takse v višini 30 EUR.

# 710-2691/2017-3
Inšpektorica je ugotovila, da je bila kršiteljica naročnica del z brezposelno osebo. Ugotovljeni so bili elementi delovnega razmerja, kar je v nasprotju z drugim odstavkom 13. člena Zakona o delovnih razmerjih-1 in je tako storila prekršek po tretji točki prvega odstavka v povezavi z drugim odstavkom 217. člena Zakona o delovnih razmerjih [_ja, taka klobasa v odločbi piše_]. Izrečen ji je bil opomin in plačilo stroške postopka odmerjene sodne takse v vrednosti 30 EUR.

# 710-2214/2018
Inšpektor je ugotovil, da je kršiteljica omogočila/dovolila, da je pri njej na podlagi pogodbe civilnega prava opravljala delo oseba (pobrisano), kar je v nasprotju z določbami 2. odstavka 13. člena Zakona o delovnih razmerjih-1. Samostojni podjetnici, ki zaposluje manj kot 10 oseb, se tako izreče globa 1500 EUR in 150 EUR sodne takse.

# 710-1885/2017
Inšpektorica pravni in odgovorni osebi izreče opomin, ker je omogočila opravljane dela prodajalke, verjetno na podlagi pogodbe civilnega prava, na sistematiziranem delovnem mestu prodajalke z vsemi elementi delovnega razmerja. To je v nasprotju z drugim odstavkom 13. člena Zakona o delovnih razmerjih. Pravna in odgovorna oseba morata vsaka plačati 30 EUR stroškov postopka - sodno takso.

# 710-1390/2017
Inšpektor pravni in odgovorni osebi očita odgovornost za prekšek, ker je odgovorna oseba v imenu pravne osebe sklenila pogodbo civilnega prava z osebo, ki ima priglašeno dejavnost, in ji tako omogočila delo, ki je v nasprotju z drugim odstavkom 13. člena Zakona o delovnih razmerjih. Izrečena je globa 3000 EUR za pravno in 450 EUR za odgovorno osebo.
