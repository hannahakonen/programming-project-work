from matplotlib import pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from io import StringIO
from corrupted_data_file_error import *

class PlotFigure(FigureCanvas):
    '''
    Canvas for plotting
    '''
    def __init__ (self, parent = None):
        fig = plt.figure()
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)   
        
        self.title = "Spectrum Simulation"
        self.x_title = "Frequency (1/cm)"
        self.y_title = "Intensity"
        self.axes.set_title(self.title)
        plt.xlabel(self.x_title)
        plt.ylabel(self.y_title)
        self.x_start = 0
        self.x_stop = 0  
        self.y_start = 0 
        self.y_stop = 0  
           
        self.frequencies = []
        self.intensities = []
        self.scaled_intensities = []                          
        self.fwhm_calc = 2 * (np.sqrt(np.log(2))) / (np.sqrt(np.pi))  # x=X, ymax=Y, fx=1, ca. 0.939
        self.fwhm = self.fwhm_calc  # changed by user
        self.sigma_calc = self.fwhm_calc / (2 * np.sqrt(2 * np.log(2)))
        self.sigma = self.sigma_calc
        self.scaled_y = 0.0            
        
        self.peaks_checked = True
        self.file_loaded = False
            
    def clear_axes(self):
        plt.cla()
        
    def draw_stem_plot(self): 
        frequence_array = np.array(self.frequencies)
        intensity_array = np.array(self.intensities)
        self.axes.set_title(self.title)
        plt.xlabel(self.x_title)
        plt.ylabel(self.y_title)
        self.y_stop = max(self.intensities) + 50
        plt.ylim(self.y_start, self.y_stop)
        self.axes.stem(frequence_array, intensity_array, linefmt='black', markerfmt=" ", basefmt=" ", use_line_collection=True)
        
    def draw_simulated_plot(self):  
        self.set_sigma() # takes into account the change in fwhm
        self.scale_y()
        self.x_stop = self.frequencies[-1] + 50
        self.x_start = self.frequencies[0] - 50
        x = np.linspace(self.x_start, int(self.x_stop), 10000)
        sum_y = 0
        number_peaks = len(self.frequencies)
        scaled_y = 0
        sum_y = 0
        fx = 0
        for i in range(number_peaks):
            scaled_y = self.scaled_intensities[i]
            fx = 1 / (self.sigma * np.sqrt(2 * np.pi)) * np.exp(- (x - self.frequencies[i])**2 / (2 * self.sigma**2))
            sum_y += scaled_y * fx
        self.axes.set_xlim(self.x_start, self.x_stop)
        self.axes.set_title(self.title)
        plt.xlabel(self.x_title)
        plt.ylabel(self.y_title)
        self.y_stop = max(self.intensities) + 50
        plt.ylim(self.y_start, self.y_stop)
        self.axes.plot(x, sum_y, color='#ba2a2a')
             
    def scale_y(self):
        '''
        Used for scaling the function of a peak when changing the FWHM so that the peak maximum does not change.
        '''
        self.scaled_intensities = []
        for i in self.intensities:
            self.scaled_intensities.append(i * self.fwhm / self.fwhm_calc)
    
    def read_file(self, input):
        '''
        Creates the lists of frequencies and intensities from the text file opened in the GUI.
        '''
        text = StringIO()
        text.write(input) 
        text.seek(0, 0)
        current_line = ""
        frequency = 0
        intensity = 0
        
        try:
            current_line = text.readline()                     
            while current_line != "":
                if current_line.strip() != "":  
                    line_parts = current_line.split()
                    if len(line_parts) == 2: 
                        try:
                            frequency = float(line_parts[0])    
                            intensity = float(line_parts[1])
                            self.frequencies.append(frequency)
                            self.intensities.append(intensity)
                            current_line = text.readline()
                        except ValueError:
                            current_line = text.readline()
                    else:
                        current_line = text.readline()
                else:
                    current_line = text.readline()
                    
        except OSError:
            raise CorruptedDataFileError("Reading the file failed.")
        
    def load_file(self, input):  
        self.reset_initial_values()
        self.clear_axes()
        self.read_file(input)
        if len(self.frequencies) != 0:
            self.draw_simulated_plot()
            if self.peaks_checked:     
                self.draw_stem_plot() 
            self.set_file_loaded()
 
    def set_file_loaded(self):
        self.file_loaded = True
    
    def set_peaks_on(self): 
        self.peaks_checked = True  
    
    def set_peaks_off(self):         
        self.peaks_checked = False  

    def set_sigma(self):
        self.sigma = self.fwhm / (2 * np.sqrt(2 * np.log(2)))
    
    def set_fwhm(self, new):
        self.fwhm = new
        
    def get_fwhm(self):
        return self.fwhm
 
    def reset_initial_values(self):
        self.frequencies = []  # X   
        self.intensities = []  # Y
        self.scaled_intensities = []        
        #self.fwhm = self.fwhm_calc    # If this is on, the width changes with every load
        self.sigma = self.sigma_calc
        self.scaled_y = 0.0             
        self.x_start = 0 
        self.x_stop = 0  
        self.y_start = 0 
        self.y_stop = 0
