# Spectrum Simulation Program by Python

Project work for the python programming course 2 (Aalto University): Numpy, Matplotlib, PyQt5 

## Introduction
To be translated:
Projektityössä toteutettiin spektrisimulaatio-ohjelma. Ohjelma lukee käyttöliittymässä avatusta tekstitiedostosta molekyylin kvanttikemiallisesti lasketun spektrin ja piirtää sen sekä piikkeinä että kokeellista mittausta simuloivana spektrinä, jossa piikit on levennetty normaalijakauman tiheysfunktion avulla. Kokeellisesti mitatut piikit ovat leveämpiä johtuen mittalaitteen tarkkuudesta ja näytteestä, jolloin vierekkäiset piikit eivät erotu toisistaan. Käyttäjä voi säätää käyttöliittymässä kuvaajan asetuksia, kuten otsikoita, akseleiden välejä, piikkien leveyttä ja sitä, näkyykö piikit. Spektrin voi myös tallentaa kuvatiedostona. Projektissa myös testattiin ohjelman toimivuutta.

## Installation
To be translated:
Ohjelma tarvitsee NumPy-, Matplotlib- ja Pyqt5-kirjastoja
Kirjastojen asennusohje:
NumPy: "pip install numpy"
Matplotlib: "pip install matplotlib"
PyQt5: "pip install PyQt5"

## Files

- spectrum simulation program.png: screenshot of the program
yleissuunnitelma
tekninen suunnitelma
loppuraportti
tekstitiedostomalli SrU2F12_Raman.txt

pääohjelma main.py
käyttöliittymä gui.py
kuvan piirtävä plotfigure.py
virheluokka corrupted_data_file_error.py
testausohjelma test.py
tyhjä gui_malli.py

## Instructions
To be translated:
Ohjelma käynnistetään ajamalla pääohjelma
Spektri avataan tekstitiedostona File-valikosta: Open
Tekstitiedostosta lähtotiedoiksi luetaan vain rivit, joissa on kaksi lukua peräkkäin: ensin spektrin taajuus ja sitten sen intensiteetti.
Työkalupalkilla voi säätää kuvaa.
Peaks-valintaruudulla voi poistaa laskennalliset piikit näkyvistä.
Peak Width -tekstikentällä voi vaihtaa simuloitujen piikkien leveyttä.
