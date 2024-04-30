class Address:
    def __init__(self, city, street, apartment):
        self.city = city
        self.street = street
        self.apartment = apartment

    def get_full_information(self):
        return f"{self.city}{self.street}{self.apartment}"

