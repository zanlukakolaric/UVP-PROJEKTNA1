import yfinance as yf
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
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
        podatki["Dnevna rast"] = (podatki["Close"] - podatki["Open"]).round(4)
        podatki_o_kriptovalutah[kriptovaluta]  = podatki
    return podatki_o_kriptovalutah
    
    
    

    
    
    
    
    
def povprecje(podatki_o_kriptovalutah):
    for kriptuvaluta, podatki in podatki_o_kriptovalutah.items():
        podatki["Povprečje"] = ((podatki["Close"] + podatki["Open"]) /2).round(4)
        podatki_o_kriptovalutah[kriptuvaluta] = podatki
    return podatki_o_kriptovalutah

    
    
    
    
    
    
def rast_v_procentih(podatki_o_kriptovalutah):
    for kriptuvaluta, podatki in podatki_o_kriptovalutah.items():
        podatki["Rast v %"] = (((podatki["Close"]/podatki["Open"]) - 1)*100).round(4)
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
        podatki["Volume"] = podatki["Volume"].round(4)
        podatki_o_kriptovalutah[kriptuvaluta] = podatki.ffill()   #to dopolni prazna mesta z zadnjimi znanimi vrednostmi
    return podatki_o_kriptovalutah



def shrani(podatki_o_kriptovalutah):
    os.makedirs("datoteke", exist_ok=True)
    for ime, podatki in podatki_o_kriptovalutah.items():
        file_name = f"{ime}.csv"
        podatki.to_csv("datoteke/" + file_name)
    
    
def graf_povprecnih_cen(podatki_o_kriptovalutah):
    fig, axs = plt.subplots(1, 2, figsize=(12, 5))

    for kriptovaluta, podatki in podatki_o_kriptovalutah.items(): 
        # navadna skala
        axs[0].plot(podatki.index, podatki["Povprečje"], label=kriptovaluta)
        axs[0].set_title('Graf povprečnih cen')
        axs[0].set_xlabel('datum')
        axs[0].set_ylabel('cena v USD')
        axs[0].grid(True)
        axs[0].legend()


        # logaritemska skala
        axs[1].semilogy(podatki.index, podatki["Povprečje"], label=kriptovaluta)
        axs[1].set_title('Graf povprečnih cen, logaritemska skala')
        axs[1].set_xlabel('datum')
        axs[1].set_ylabel('y (Log Scale)')
        axs[1].grid(True)
        axs[1].legend()



    plt.tight_layout()

    plt.show()

def graf_odpiralnih_cen(podatki_o_kriptovalutah):
    plt.figure(figsize=(12, 6))
    for kriptovaluta, podatki in podatki_o_kriptovalutah.items(): 
        podatki["Open"].plot(label=f"{kriptovaluta}")
    
    plt.title("Gibanje odpiralnih cen")
    plt.xlabel("Datum")
    plt.ylabel("Cena v USD")
    plt.grid(True)
    plt.legend()
    plt.show()
    
def graf_odpiralnih_cen_BNB(podatki_o_kriptovalutah):
    plt.figure(figsize=(12, 6))
    for kriptovaluta, podatki in podatki_o_kriptovalutah.items(): 
        if kriptovaluta == "BNB-USD":
            podatki["Open"].plot(label=f"{kriptovaluta}")
    
    plt.title("Gibanje odpiralnih cen BNB-USD")
    plt.xlabel("Datum")
    plt.ylabel("Cena v USD")
    plt.grid(True)
    plt.legend()
    plt.show()


def graf_odpiralnih_cen_BTC(podatki_o_kriptovalutah):
    plt.figure(figsize=(12, 6))
    for kriptovaluta, podatki in podatki_o_kriptovalutah.items(): 
        if kriptovaluta == "BTC-USD":
            podatki["Open"].plot(label=f"{kriptovaluta}")
    
    plt.title("Gibanje odpiralnih cen BTC-USD")
    plt.xlabel("Datum")
    plt.ylabel("Cena v USD")
    plt.grid(True)
    plt.legend()
    plt.show()

def graf_odpiralnih_cen_ETH(podatki_o_kriptovalutah):
    plt.figure(figsize=(12, 6))
    for kriptovaluta, podatki in podatki_o_kriptovalutah.items(): 
        if kriptovaluta == "ETH-USD":
            podatki["Open"].plot(label=f"{kriptovaluta}")
    
    plt.title("Gibanje odpiralnih cen ETH-USD")
    plt.xlabel("Datum")
    plt.ylabel("Cena v USD")
    plt.grid(True)
    plt.legend()
    plt.show()



def graf_rasti_v_procentih(podatki_o_kriptovalutah):
    plt.figure(figsize=(12, 6))
    for kriptovaluta, podatki in podatki_o_kriptovalutah.items(): 
        podatki["Rast v %"].plot(label=f"{kriptovaluta}")
    
    plt.title("Rast kriptovalut v %")
    plt.xlabel("Datum")
    plt.ylabel("Rast v %")
    plt.grid(True)
    plt.legend()
    plt.show()
    
    
def graf_volumna(podatki_o_kriptovalutah):
    plt.figure(figsize=(12, 6))
    for kriptovaluta, podatki in podatki_o_kriptovalutah.items(): 
        podatki["Volume"].plot(label=f"{kriptovaluta}")
    
    plt.title("Volumen")
    plt.xlabel("Datum")
    plt.ylabel("Volumen")
    plt.grid(True)
    plt.legend()
    plt.show()
    



print(graf_volumna((uredi_podatke(dodaj_dnevna_rast(povprecje(rast_v_procentih(podatki_o_kriptovalutah)))))))


