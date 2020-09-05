# Spectrum Simulation Program by Python

Project work for the python programming basic course 2 (CS-A1121, Aalto University) spring 2020

## Introduction

This spectrum simulation program reads molecule’s ideal vibration spectrum (frequency X, intensity Y) from a text file such as:

![Text file](https://github.com/Katijoz/spectrum-simulation-python/blob/master/images/text%20file%20example.png)

and draws the original peaks (black) and the spectrum simulating an experimental spectrum (red):

![Spectrum simulation GUI](https://github.com/Katijoz/spectrum-simulation-python/blob/master/images/spectrum%20simulation%20program.png)

The user loads a text file through the GUI and can adjust the figure settings and the peak width and visibility. It is also possible to save the figure as a png file. 

The peaks of the simulated spectrum are widened using the probability density function of the normal distribution

![fx](https://github.com/Katijoz/spectrum-simulation-python/blob/master/images/fx.png)

where x0 is the frequency X from the input file and the standard deviation is calculated from the full width at half maximum (FWHM) value (given by the user in the Peak width text field)

![ro](https://github.com/Katijoz/spectrum-simulation-python/blob/master/images/ro.png)

Single ideal peak (X, Y) is widened by

![y](https://github.com/Katijoz/spectrum-simulation-python/blob/master/images/y.png)

However, if the user now changes the peak width (FWHM), f(x) changes and the simulated peak height y is not equal to given peak height Y anymore. In order to fix the value of f(x) to 1, when x=X=x0, it should be scaled. For that the real FWHM, FWHM0, is calculated from the equation

![fx1](https://github.com/Katijoz/spectrum-simulation-python/blob/master/images/fx1.png)

and we get FWHM0≈0,94. If the user changes peak width, f(x) should be scaled by FWHM/FWHM0. 

The equation for the simulated spectrum is the sum of all the simulated peaks ysim

![ysim](https://github.com/Katijoz/spectrum-simulation-python/blob/master/images/ysim.png)

Numpy is used to create the array for plotting the figure, Matplotlib to draw the figure and PyQt5 to create the GUI. 

The structure of the code: 

![Code structure](https://github.com/Katijoz/spectrum-simulation-python/blob/master/images/code%20structure.png)

## Files

### doc
- SrU2F12_Raman.txt: model for the input text file containing the molecule’s ideal vibration spectrum
- Spektrisimulaatio Yleissuunnitelma.pdf: general plan in Finnish
- Spektrisimulaatio Tekninen suunnitelma: technical plan in Finnish
- Spektrisimulaatio Raportti: project report in Finnish

### src
- main.py
- gui.py: user interface
- plotfigure.py: draws the figure
- corrupted_data_file_error.py
- test.py

## Instructions
- program is started by running main.py
- input spectrum is opened as a text file from the File menu: Open
- only the correct rows having two numbers are read by the program: frequency (cm^-1) and peak intensity 
- figure can be adjusted by the navigation toolbar
- visibility of the computational peaks is selected with the Peaks checkbox 
- the width of the peaks in the simulated spectrum can be changed with the Peak Width text field

## Installation
- NumPy: "pip install numpy"
- Matplotlib: "pip install matplotlib"
- PyQt5: "pip install PyQt5"
