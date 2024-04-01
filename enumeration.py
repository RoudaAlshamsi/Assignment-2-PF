from enum import Enum

class ExhibitionLocation(Enum):
    PERMANENT_GALLERIES = "Permanent Galleries"
    EXHIBITION_HALLS = "Exhibition Halls"
    OUTDOOR_SPACES = "Outdoor Spaces"

class EventPurpose(Enum):
    FUNDRAISING = "Fundraising"
    MUSICAL_CONCERT = "Musical Concert"
    LIGHT_SHOW = "Light Show"

class VisitorCategory(Enum):
    ADULTS = "Adults between 18-60"
    CHILDREN = "Children below 18"
    TEACHER = "Teacher"
    STUDENT = "Student"
    SENIOR = "Senior above 60"