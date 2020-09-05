import unittest
from io import StringIO
from gui import GUI
from plotfigure import PlotFigure

class Test(unittest.TestCase):
    
    def set_up(self):  
        self.canvas = PlotFigure()
        
    def test_read_file(self):
        data = "# SrU2F12 Raman spectrum\n# X = Freq (cm^-1); Y = Polycrystalline Raman intensity (arb. units)\n486.40      211.39\n494.64      78.15\n504.37      181.35\n513.02      68.03\n534.32      30.33\n646.23      1000\n653.24      13.5"        
        
        x = [486.40, 494.64, 504.37, 513.02, 534.32, 646.23, 653.24]          
        y = [211.39, 78.15, 181.35, 68.03, 30.33, 1000, 13.5]
        
        self.canvas = PlotFigure()
        self.canvas.read_file(data)
        
        self.assertEqual(x, self.canvas.frequencies, "Wrong frequencies")
        self.assertEqual(y, self.canvas.intensities, "Wrong intensities")
        
    def test_read_file_some_wrong(self):
        data = "# SrU2F12 Raman spectrum\n# X = Freq (cm^-1); Y = Polycrystalline Raman intensity (arb. units)\n50     plop\nplip        100\n         100         100\n\n\n200 jhhhh hkhh\n    300      300 \n400        500                600 \n"
        
        x = [100, 300]          
        y = [100, 300]
        
        self.canvas = PlotFigure()
        self.canvas.read_file(data)
        
        self.assertEqual(x, self.canvas.frequencies, "Wrong frequencies")
        self.assertEqual(y, self.canvas.intensities, "Wrong intensities")
        
    def test_read_file_all_wrong(self):
        data = "# SrU2F12 Raman spectrum\n# X = Freq (cm^-1); Y = Polycrystalline Raman intensity (arb. units)\n50     plop\nplip        100\n         plop         100\n\n\n200 jhhhh hkhh\n    plop     300 \n400        500                600 \n"
        
        x = []          
        y = []
        
        self.canvas = PlotFigure()
        self.canvas.read_file(data)
        
        self.assertEqual(x, self.canvas.frequencies, "Wrong frequencies")
        self.assertEqual(y, self.canvas.intensities, "Wrong intensities")

if __name__ == '__main__':
    unittest.main()