import yfinance as yf
import pandas as pd
import numpy as np
#dobis podatke za kriptovlute. Pazit moraš, da imena pišeš kot "BTC-USD"

def pridobi_podatke(imena_kriptovalut, z ="2015-09-17", k="2023-08-01"):
    podatki = {}
    for ime in imena_kriptovalut:
        podatki_o_kriptovaluti = yf.download(ime, z, k)
        podatki[ime] = podatki_o_kriptovaluti
    
    
    return podatki
podatki_o_kriptovalutah = pridobi_podatke(["BTC-USD"])

def dodaj_dnevna_rast(podatki_o_kriptovalutah):
    for kriptovaluta, podatki in podatki_o_kriptovalutah.items():
        podatki["Dnevna rast"] = (podatki["Close"] - podatki["Open"])
        podatki_o_kriptovalutah[kriptovaluta]  = podatki
    return podatki_o_kriptovalutah
    

    
    
    
    
    
def povprecje(podatki_o_kriptovalutah):
    for kriptuvaluta, podatki in podatki_o_kriptovalutah.items():
        podatki["Povprečje"] = ((podatki["Close"] + podatki["Open"]) /2).round(4)
        podatki_o_kriptovalutah[kriptuvaluta] = podatki
    return podatki_o_kriptovalutah

    
    
    
    
    
    
def rast_v_procentih(podatki_o_kriptovalutah):
    for kriptuvaluta, podatki in podatki_o_kriptovalutah.items():
        podatki["Rast v %"] = ((podatki["Close"]/podatki["Open"]) - 1).round(4)
        podatki_o_kriptovalutah[kriptuvaluta] = podatki
    return podatki_o_kriptovalutah

def rast_glede_na_x(podatki_o_kriptovalutah, x = None):
    for kriptuvaluta, podatki in podatki_o_kriptovalutah.items():
        if x is None:
            return podatki_o_kriptovalutah
        else:
            return podatki_o_kriptovalutah  
    
    
    
    
    
def uredi_podatke(podatki_o_kriptovalutah):
    for kriptuvaluta, podatki in podatki_o_kriptovalutah.items():
        podatki["Close"] = podatki["Close"].round(4)
        podatki["Open"] = podatki["Open"].round(4)
        podatki["High"] = podatki["High"].round(4)
        podatki["Low"] = podatki["Low"].round(4)
        podatki["Adj Close"] = podatki["Adj Close"].round(4)
        podatki_o_kriptovalutah[kriptuvaluta] = podatki.ffill()   #to dopolni prazna mesta z zadnjimi znanimi vrednostmi
    return podatki_o_kriptovalutah


def shrani(podatki_o_kriptovalutah):
    