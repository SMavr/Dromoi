class Scale:
    def __init__(self, id, name):
        self.id = id
        self.name = name

collection = [
    Scale (1, 'Φυσικό Μινόρε'), 
    Scale (2, 'Αρμονικό Μινόρε'), 
    Scale (3, 'Νιαβέντι'), 
    Scale(4,'Νιγρίς ή Ποιμενικός'), 
    Scale(5,'Χιτζάζ'),
    Scale(6,'Χιτζασκιάρ'), 
    Scale(7,'Πειραιώτικος'), 
    Scale(8,'Φυσικό Ματζόρε'), 
    Scale(9,'Σεγκιάχ'), 
    Scale(10,'Χουζάμ'),
    Scale(11,'Ουσάκ')]

class ScaleCoordinates:
    def __init__(self, id, coordinates):
        self.id = id
        self.coordinates = coordinates

class Coordinate:
    def __init__(self, chord, tab, finger):
        self.chord = chord
        self.tab = tab
        self.finger = finger

coordinates = [
    ScaleCoordinates (1, [Coordinate(3, 12, 1), Coordinate(3, 11, 1)]), 
    ScaleCoordinates (2, [Coordinate(3, 11, 3), Coordinate(3, 11, 1)])]