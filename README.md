# PREDSTAVITEV GIBANJA CEN KRIPTOVALUT IN NJIHOVA ANALIZA
AVTOR: Žan Luka Kolarič

Pri predmetu Uvod v programiranje sem pripravil tole projektno nalogo. Podatke za cene teh kriptovalut, ki se vse primerjajo glede na ceno ameriškega dolarja, sem prenesel iz spletne strani [Yahoo](https://finance.yahoo.com/) in nato rezultate predstavil s pomočjo Yupiter Notebook.

Za kriptovalute Bitcoin, Ethereum in Binance coin sem sestavil tabele v katerih sem zajel:
- datum
- odpiralno ceno (Open)
- zapiralno ceno (Close)
- najvišjo ceno (High)
- najnižjo ceno (Low)
- volumen (Volume)
- dnevni profit
- interval gibanja
- rast (v procentih)

Nato sem pa skiciral grafe za povprecno ceno kriptovalut, volumna in rasti v procentih.

## PRIPRAVA PODATKOV
V datoteki funkcija.py sem zapisal program, kateri zajame podatke za BTC-USD, ETH-USD in BNB-USD. Te podatke sem lepo uredil s pomočjo funkcije uredi_podatke in jim dodal podatke o dnevnem donosu, povprečni ceni in rasti v %. Podatke sem shranil v mapo datoteke, kjer sem shranil tabelo za vsako izmed kriptovalut posebaj. Podatke in ugotovitve sem zapisal v datoteko glavna_datoteka.ipynb.
Uporabil sem pakete: `yfinance`, `pandas`, `matplotlib.pyplot` in `os`.
