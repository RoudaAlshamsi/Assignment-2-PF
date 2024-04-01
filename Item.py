from enum import Enum

class ExhibitionLocation(Enum):
    PERMANENT_GALLERIES = "Permanent Galleries"
    EXHIBITION_HALLS = "Exhibition Halls"
    OUTDOOR_SPACES = "Outdoor Spaces"

class Item:
    """Class to represent an item"""
    #constructor to initialize attributes
    def __init__(self, title, artist, dateOfCreation, historicalSignificance):
        self.title = title
        self.artist = artist
        self.dateOfCreation = dateOfCreation
        self.historicalSignificance = historicalSignificance

    #setter and getter for title
    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    # setter and getter for artist
    def setArtist(self, artist):
        self.artist = artist

    def getArtist(self):
        return self.artist

    # setter and getter for dateOfCreation
    def setDateOfCreation(self, dateOfCreation):
        self.dateOfCreation = dateOfCreation

    def getDateOfCreation(self):
        return self.dateOfCreation

    # setter and getter for historicalSignificance
    def setHistoricalSignificance(self, historicalSignificance):
        self.historicalSignificance = historicalSignificance

    def getHistoricalSignificance(self):
        return self.historicalSignificance

    #method to print the details of the item
    def printDetails(self):
        print(f"Title: {self.title}")
        print(f"Artist: {self.artist}")
        print(f"Date of Creation: {self.dateOfCreation}")
        print(f"Historical Significance: {self.historicalSignificance}")