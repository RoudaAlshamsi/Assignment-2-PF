from enum import Enum

class EventPurpose(Enum):
    FUNDRAISING = "Fundraising"
    MUSICAL_CONCERT = "Musical Concert"
    LIGHT_SHOW = "Light Show"

class SpecialEvent:
    """Class to represent a special event"""
    #constructor to initialize attributes
    def __init__(self, eventName, eventPurpose, eventLocation, eventDuration, ticketPrice):
        self.eventName = eventName
        self.eventPurpose = eventPurpose
        self.eventLocation = eventLocation
        self.eventDuration = eventDuration
        self.ticketPrice = ticketPrice

    #setter and getter for eventName
    def setEventName(self, eventName):
        self.eventName = eventName

    def getEventName(self):
        return self.eventName

    #setter and getter for eventPurpose
    def setEventPurpose(self, eventPurpose):
        self.eventPurpose = eventPurpose

    def getEventPurpose(self):
        return self.eventPurpose

    #setter and getter for eventLocation
    def setEventLocation(self, eventLocation):
        self.eventLocation = eventLocation

    def getEventLocation(self):
        return self.eventLocation

    #setter and getter for eventDuration
    def setEventDuration(self, eventDuration):
        self.eventDuration = eventDuration

    def getEventDuration(self):
        return self.eventDuration

    #setter and getter for ticketPrice
    def setTicketPrice(self, ticketPrice):
        self.ticketPrice = ticketPrice

    def getTicketPrice(self):
        return self.ticketPrice

    #method to calculate the total revenue generated from ticket sales
    def calculateTotalRevenue(self, num_tickets_sold):
        return num_tickets_sold * self.ticketPrice

    #method to check if the event is a fundraiser event
    def isFundraisingEvent(self):
        return self.eventPurpose == EventPurpose.FUNDRAISING

    #method to print event details
    def printEventDetails(self):
        print(f"Event Name: {self.eventName}")
        print(f"Event Purpose: {self.eventPurpose.value}")
        print(f"Event Location: {self.eventLocation}")
        print(f"Event Duration: {self.eventDuration}")
        print(f"Ticket Price: {self.ticketPrice}")