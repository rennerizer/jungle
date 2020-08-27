class Restaurant:
    """ This place is 'da bomb """

    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine

    def open_restaurant(self):
        print("The restaurant is now open")

place = Restaurant('Willies', 'swamp')
place.open_restaurant()