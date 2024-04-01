from enum import Enum
class VisitorCategory(Enum):
    ADULTS = "Adults between 18-60"
    CHILDREN = "Children below 18"
    TEACHER = "Teacher"
    STUDENT = "Student"
    SENIOR = "Senior above 60"

from Visitor import Visitor

class Ticket:
    """Class to represent a ticket"""
    #constructor to initialize attributes
    def __init__(self, date, exhibition, durationOfTime, location, guide, visitorCategory, ticketPrice):
        self.date = date
        self.exhibition = exhibition
        self.durationOfTime = durationOfTime
        self.location = location
        self.guide = guide
        self.visitorCategory = visitorCategory
        self.ticketPrice = ticketPrice

    #setter and getter for date
    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    #setter and getter for exhibition
    def setExhibition(self, exhibition):
        self.exhibition = exhibition

    def getExhibition(self):
        return self.exhibition

    #setter and getter for durationOfTime
    def setDurationOfTime(self, durationOfTime):
        self.durationOfTime = durationOfTime

    def getDurationOfTime(self):
        return self.durationOfTime

    #setter and getter for location
    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    #setter and getter for guide
    def setGuide(self, guide):
        self.guide = guide

    def getGuide(self):
        return self.guide

    #setter and getter for visitorCategory
    def setVisitorCategory(self, visitorCategory):
        self.visitorCategory = visitorCategory

    def getVisitorCategory(self):
        return self.visitorCategory

    #setter and getter for ticketPrice
    def setTicketPrice(self, ticketPrice):
        self.ticketPrice = ticketPrice

    def getTicketPrice(self):
        return self.ticketPrice