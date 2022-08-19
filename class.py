#Animal Class
class Animal:
    type = 'Land Animal'

    def __init__(self, name, color, type):
        self.name = name
        self.color = color
        self.type = type
    
    def show_details(self):
        print("{} is a {} and is of {} color".format(self.name, self.type, self.color))