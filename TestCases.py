from Artwork import Artwork
from Exhibition import Exhibition
from Ticket import Ticket
from Visitor import Visitor
from enumeration import VisitorCategory

#Test case for adding new art to the museum
def addNewArt():
    artwork = Artwork("Mona Lisa", "Leonardo da Vinci", "1503", "Famous Portrait", "Permanent Gallery", "30x20 inches", "Various", "Oil on wood")
    assert artwork.title == "Mona Lisa"
    assert artwork.exhibitionLocation == "Permanent Gallery"
    return "Test case for adding new art passed."


#Test case for opening a new exhibition

def openExhibition():
    exhibition = Exhibition("3 hours", "Exhibition Hall 1")
    assert exhibition.durationOfTime == "3 hours"
    assert exhibition.location == "Exhibition Hall 1"
    return "Test case for opening a new exhibition passed."


#Test case fro purchasing ticket
def purchaseTicket():
    visitor = Visitor("John Doe", 30, VisitorCategory.ADULTS)
    ticket = Ticket("30-3-2024", "Renaissance Art Exhibition", "3 hours","Exhibition Hall 1", "John Doe", VisitorCategory.ADULTS, 63)
    assert ticket.date == "30-3-2024"
    assert ticket.exhibition == "Renaissance Art Exhibition"
    assert ticket.visitorCategory.ADULTS
    return "Test case for purchasing ticket passed."


#Test case for displaying payment receipt
def paymentReceipt():
    visitor = Visitor("John Doe", 30, VisitorCategory.ADULTS)
    ticket1 = Ticket("30-3-2024", "Renaissance Art Exhibition", "3 hours","Exhibition Hall 1", "John Doe", VisitorCategory.ADULTS, 66.15)
    ticket2 = Ticket("31-3-2024", "Modern Art Exhibition", "2 hours","Exhibition Hall 2", "John Doe", VisitorCategory.STUDENT, 0)

    total_cost = ticket1.ticketPrice + ticket2.ticketPrice
    assert total_cost == 66.15
    return "Test case for displaying payment receipt passed."


#Run all the test cases
if __name__ == "__main__":
    # Store the results of each test case
    results = []

    # Execute each test case and store the result
    results.append(addNewArt())
    results.append(openExhibition())
    results.append(purchaseTicket())
    results.append(paymentReceipt())

    #Print the results
    for result in results:
        print(result)