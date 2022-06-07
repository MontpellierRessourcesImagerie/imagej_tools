from ij import IJ
from fr.cnrs.mri.ijso.utilities import History
from ij.text import TextWindow

def main():
    image = IJ.getImage()
    title = image.getTitle()
    history = History.fromImage(image)
    text = history.asText()
    window = TextWindow("History of {}".format(title), text, 800, 600)    


main()
