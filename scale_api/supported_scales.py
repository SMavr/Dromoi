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

class Coord:
    def __init__(self, chord, tab, finger):
        self.chord = chord
        self.tab = tab
        self.finger = finger

scale_coordinates = [
    # Fusiko Minore
    ScaleCoordinates (1, [Coord(2, 7, 1), Coord(2, 5, 1), Coord(2, 4, 2),  
                          Coord(2, 2, 4), Coord(1, 5, 1), Coord(1, 4, 2), 
                          Coord(1, 2, 2), Coord(1, 0, 4)]), 

    # Armoniko Minore
    ScaleCoordinates (2, [Coord(2, 7, 1), Coord(2, 5, 1), Coord(2, 4, 2),  
                          Coord(2, 2, 4), Coord(1, 5, 1), Coord(1, 4, 2), 
                          Coord(1, 1, 2), Coord(1, 0, 3)]),

    # Niaventi
    ScaleCoordinates (3, [Coord(2, 7, 1), Coord(2, 5, 1), Coord(2, 4, 3),  
                          Coord(1, 6, 1), Coord(1, 5, 2), Coord(1, 4, 3), 
                          Coord(1, 1, 2), Coord(1, 0, 3)]),

    # Nigris Poimenikos
    ScaleCoordinates (4, [Coord(2, 7, 1), Coord(2, 5, 1), Coord(2, 4, 3),  
                          Coord(1, 6, 1), Coord(1, 5, 2), Coord(1, 3, 1), 
                          Coord(1, 2, 2), Coord(1, 0, 4)]),

    # Hitzaz                   
    ScaleCoordinates (5, [Coord(2, 7, 2), Coord(2, 6, 3), Coord(1, 8, 1),  
                          Coord(1, 7, 2), Coord(1, 5, 1), Coord(1, 4, 2), 
                          Coord(1, 2, 2), Coord(1, 0, 4)]),

     # Hitzaskiar                   
    ScaleCoordinates (6, [Coord(2, 7, 2), Coord(2, 6, 3), Coord(1, 8, 1),  
                          Coord(1, 7, 2), Coord(1, 5, 1), Coord(1, 4, 2), 
                          Coord(1, 1, 2), Coord(1, 0, 3)]),                         
                          
    # Peiraiotikos                   
    ScaleCoordinates (7, [Coord(2, 7, 1), Coord(2, 6, 2), Coord(1, 8, 1),  
                          Coord(1, 6, 1), Coord(1, 5, 2), Coord(1, 4, 3), 
                          Coord(1, 1, 2), Coord(1, 0, 3)])                         
                        ]