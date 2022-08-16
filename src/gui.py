from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QCheckBox, QPushButton, QAction, QFileDialog, QLineEdit, QLabel, QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from plotfigure import PlotFigure
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar

class GUI(QMainWindow):
    '''
    The class GUI handles the drawing of a PlotFigure and allows user to
    interact with it.
    '''
    def __init__(self):
        super().__init__()
        self.init_window() 
       
        self.init_menubar()        # File-Open
                
        self.canvas = PlotFigure()
        self.hbox3.addWidget(self.canvas)  
            
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.hbox2.addWidget(self.toolbar)
        
        self.init_checkbox_peaks() 
        self.hbox4.addStretch(1)
        self.init_textline_peak_width()
    
    def init_textline_peak_width(self):
        '''
        Textline for changing the peak width
        '''
        self.title = QLabel(self)
        self.title.setText('Peak Width:')
        self.hbox4.addWidget(self.title)
        self.tline = QLineEdit(self)
        self.tline.setMaxLength(3)
        self.hbox4.addWidget(self.tline)       
        self.tline.returnPressed.connect(self.onPressed)
        
    def onPressed(self): 
        '''
        Draws a new figure to canvas according to the given FWHM
        '''
        self.canvas.set_fwhm(float(self.tline.text())) 
        if self.canvas.file_loaded:    # Only if a text file has been loaded even once, try could be better 
            self.canvas.clear_axes() 
            if self.canvas.peaks_checked:
                self.canvas.draw_stem_plot()
            self.canvas.draw_simulated_plot()
            self.canvas.draw()    
     
    def init_menubar(self):
        '''
        For opening the text file. 
        '''
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog_load)

        menubar = self.menuBar() 
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)   
        
    def showDialog_load(self):     
        '''
        Opens the file as string and conveys it to the canvas for drawing the plots.
        '''
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home') 
        
        if fname[0]:
            try:
                f = open(fname[0], 'r')
                with f:       # with takes care of closing the file too
                    data = f.read()  
                    self.canvas.load_file(data)  
                    self.canvas.draw()
            except OSError:
                print("Could not open the file") # Does not print this
     
    def init_checkbox_peaks(self):  
        '''
        Peaks on/off selection
        '''     
        self.checkBox = QCheckBox('Peaks', self)
        self.checkBox.toggle()                                    
        self.checkBox.stateChanged.connect(self.peaks_on_off)
        
        self.hbox4.addWidget(self.checkBox)
        
    def peaks_on_off(self, state): 
        if state == Qt.Checked:
            self.canvas.set_peaks_on()
            if self.canvas.file_loaded:    # Only if a text file has been loaded even once, try better?
                self.canvas.draw_stem_plot()
                self.canvas.draw()
        else:
            self.canvas.set_peaks_off()
            if self.canvas.file_loaded:
                self.canvas.clear_axes() 
                self.canvas.draw_simulated_plot()
                self.canvas.draw()
         
    def init_window(self):
        #Sets up the window.
        title = "Spectrum Simulation"
        top = 400
        left = 400
        width = 900
        height = 600
        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        
        self.setCentralWidget(QtWidgets.QWidget()) # QMainWindown must have a centralWidget to be able to add layouts
        self.vbox = QtWidgets.QVBoxLayout() # Vertical main layout   
        self.centralWidget().setLayout(self.vbox) 
        self.hbox1 = QtWidgets.QHBoxLayout()  
        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox3 = QtWidgets.QHBoxLayout()
        self.hbox4 = QtWidgets.QHBoxLayout()
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        