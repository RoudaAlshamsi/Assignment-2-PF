class Tour:
    """Class to represent a tour"""
    #constructor to initialize attributes
    def __init__(self, date, numberOfVisitors, guide):
        self.date = date
        self.numberOfVisitors = numberOfVisitors
        self.guide = guide

    #setter and getter for date
    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    #setter and getter for numberOfVisitors
    def setNumberOfVisitors(self, numberOfVisitors):
        self.numberOfVisitors = numberOfVisitors

    def getNumberOfVisitors(self):
        return self.numberOfVisitors

    #setter and getter for guide
    def setGuide(self, guide):
        self.guide = guide

    def getGuide(self):
        return self.guide