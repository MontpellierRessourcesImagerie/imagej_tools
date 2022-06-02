import sys
import webbrowser
from ij import IJ
from ij.gui import GenericDialog
from ij.gui import Toolbar
from fr.cnrs.mri.ijso.tools import GenericTool
from fr.cnrs.mri.scratchAssay.analyzer import ScratchAssayAnalyzer
from fr.cnrs.mri.scratchAssay.masks import CreateMaskFromVariance
from fr.cnrs.mri.scratchAssay.masks import CreateMaskFromFindEdges

def main(): 
    toolbar = Toolbar.getInstance()
    toolbar.removeMacroTools()   
    toolbar.addPlugInTool(getHelpTool())
    toolbar.addPlugInTool(getMeasureTool())

def getHelpTool():
    helpTool = WoundHealingHelpTool()
    helpTool.setToolIcon("icon:wound_healing.png")
    helpTool.setToolName('MRI Wound Healing Help Action Tool')
    return helpTool
    
def getMeasureTool():
    measureTool  = MeasureTool()
    measureTool.setToolIcon("C000T4b12m")
    measureTool.setToolName('Measure Wound Healing Action Tool')
    return measureTool
    
class WoundHealingHelpTool(GenericTool):

    def runTool(self):
        webbrowser.open('https://github.com/MontpellierRessourcesImagerie/imagej_macros_and_scripts/wiki/Wound-Healing-Tool', new=2)    


class MeasureTool(GenericTool):
    
    def __init__(self):
        GenericTool.__init__(self)
        self.methodOption = "variance"
        self.varianceFilterRadius = 20
        self.threshold = 1
        self.closeRadius = 4
        self.minArea = 999999
        self.ignoreSpatialCalibration = False
        self.operation = ScratchAssayAnalyzer()
        
    def runTool(self):
        inputImage = IJ.getImage()
        analyzer = self.operation
        analyzer.setInputImage(inputImage)
        analyzer.addPropertyChangeListener(self)
        analyzer.start()    
        
    def showOptionsDialog(self):
        dialog = GenericDialog("Measure Image Options")
        dialog.addChoice("method", ["variance", "find edges"], self.methodOption)
        dialog.addNumericField("variance filter radius", self.varianceFilterRadius)
        dialog.addNumericField("threshold", self.threshold)
        dialog.addNumericField("radius close", self.closeRadius)
        dialog.addNumericField("min. size", self.minArea)
        dialog.addCheckbox("ignore spatial calibration", self.ignoreSpatialCalibration)
        dialog.showDialog()
        if dialog.wasCanceled():
            return
        self.methodOption = dialog.getNextChoice()
        self.varianceFilterRadius = dialog.getNextNumber()
        self.threshold = dialog.getNextNumber()
        self.closeRadius = dialog.getNextNumber()
        self.minArea = dialog.getNextNumber()
        self.ignoreSpatialCalibration = dialog.getNextBoolean()
        
main()
