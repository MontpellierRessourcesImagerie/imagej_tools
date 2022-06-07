import sys
import webbrowser
from ij import IJ
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
        self.setOperation(ScratchAssayAnalyzer())
        
    def runTool(self):
        inputImage = IJ.getImage()
        analyzer = self.operation
        analyzer.setInputImage(inputImage)
        analyzer.addPropertyChangeListener(self)
        analyzer.start()    
   
     
main()
