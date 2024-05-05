
# nefunguje to

# import json
# class FootballClub:
#     # Initialize an instance of the class
#     def __init__(self, name, city, country):
#         # Define the name, city, and country attributes of the class instance
#         self.name = name
#         self.city = city
#         self.country = country
#
#     # Define a method that returns a formatted string with full club information
#     def get_full_information(self):
#         return f"{self.name}{self.city}{self.country}"
#
#     def to_json(self):
#         return json.dumps(self.__dict__)
#
#
# club1 = FootballClub["SFC", "Opava", "Czech"]
# print(club1.get_full_information())
#
# serializace = club1.to_json()
# print(serializace)


import json
class FootballClub:
    def __init__(self, name, city, country):
        # Define the name, city, and country attributes of the class instance
        self.name = name
        self.city = city
        self.country = country

    def get_full_information(self):
        return f"{self.name}{self.city}{self.country}"

    def to_json(self):
        return json.dumps(self.__dict__)

obj = FootballClub('SFC ', 'Opava ', 'Czech ' )
print(obj.get_full_information())

serializace = obj.to_json()
print(serializace)
