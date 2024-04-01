from Item import Item

class Artwork(Item):
    """Class to represent an artwork"""
    def __init__(self, title, artist, dateOfCreation, historicalSignificance, exhibitionLocation, dimensions, colors, material):
        super().__init__(title, artist, dateOfCreation, historicalSignificance)
        self.exhibitionLocation = exhibitionLocation
        self.dimensions = dimensions
        self.colors = colors
        self.material = material


    #setter and getter for dimensions
    def setDimensions(self, dimensions):
        self.dimensions = dimensions

    def getDimensions(self):
        return self.dimensions

    #setter and getter for colors
    def setColors(self, colors):
        self.colors = colors

    def getColors(self):
        return self.colors

    #setter and getter for material
    def setMaterial(self, material):
        self.material = material

    def getMaterial(self):
        return self.material