# Spectrum Simulation Program by Python

Project work for the python programming course 2 (Aalto University): Numpy, Matplotlib, PyQt5 

## Introduction
To be translated:
Projektityössä toteutettiin spektrisimulaatio-ohjelma. Ohjelma lukee käyttöliittymässä avatusta tekstitiedostosta molekyylin kvanttikemiallisesti lasketun spektrin ja piirtää sen sekä piikkeinä että kokeellista mittausta simuloivana spektrinä, jossa piikit on levennetty normaalijakauman tiheysfunktion avulla. Kokeellisesti mitatut piikit ovat leveämpiä johtuen mittalaitteen tarkkuudesta ja näytteestä, jolloin vierekkäiset piikit eivät erotu toisistaan. Käyttäjä voi säätää käyttöliittymässä kuvaajan asetuksia, kuten otsikoita, akseleiden välejä, piikkien leveyttä ja sitä, näkyykö piikit. Spektrin voi myös tallentaa kuvatiedostona. Projektissa myös testattiin ohjelman toimivuutta.

## Installation
NumPy: "pip install numpy"
Matplotlib: "pip install matplotlib"
PyQt5: "pip install PyQt5"

## Files

### doc
- spectrum simulation program.png: screenshot of the program
- Spektrisimulaatio Yleissuunnitelma.pdf: general plan in Finnish
- Spektrisimulaatio Tekninen suunnitelma: technical plan in Finnish
- Spektrisimulaatio Raportti: project report in Finnish
- SrU2F12_Raman.txt: model for the input text file containing the molecule’s ideal vibration spectrum

### src
- main.py
- gui.py: user interface
- plotfigure.py: draws the figure
- corrupted_data_file_error.py
- test.py

## Instructions
- program is started by running main.py
- input spectrum is opened as a text file from the File menu: Open
- only the rows having two numbers are read by the program: frequency (cm^-1) and peak intensity 
- figure can be adjusted by the navigation toolbar
- visibility of the computational peaks is selected with the Peaks checkbox 
- the width of the peaks in the simulated spectrum can be changed with the Peak Width text field
