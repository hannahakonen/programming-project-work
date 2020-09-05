# Spectrum Simulation Program by Python

Project work for the python programming basic course 2 (CS-A1121, Aalto University) spring 2020

## Introduction

This spectrum simulation program reads molecule’s ideal vibration spectrum from a text file and draws the original peaks and the spectrum simulating an experimental spectrum. The peaks of the simulated spectrum are widened using the probability density function of the normal distribution. The user loads a text file through the GUI and can adjust the figure settings and the peak width and visibility. It is also possible to save the figure as a png file. 

Numpy is used to create the array for plotting the figure, Matplotlib to draw the figure and PyQt5 to create the GUI. 

![Spectrum simulation GUI](/doc/spectrum simulation program.png)

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

## Installation
- NumPy: "pip install numpy"
- Matplotlib: "pip install matplotlib"
- PyQt5: "pip install PyQt5"
