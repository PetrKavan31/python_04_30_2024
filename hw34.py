import pickle

# There is a dictionary that stores country names and their capitals. A country name is
# used as a key, a capital as a value. Implement the following: adding data, deleting data,
# finding data, editing data, saving and loading data (using packing and unpacking).


class CountryCapitalDict:
    def __init__(self):
        self.data = {}

    def add_data(self, country, capital):
        self.data[country] = capital
        print("Country added successfully.")

    def delete_data(self, country):
        if country in self.data:
            del self.data[country]
            print("Country deleted successfully.")
        else:
            print("Country not found")

    def find_data(self, country):
        return self.data.get(country, "Not found")

    def edit_data(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital

    def save_data(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self.data, file)

    def load_data(self, filename):
        with open(filename, "rb") as file:
            self.data = pickle.load(file)

def main():
    ccd = CountryCapitalDict()
    ccd.add_data('Czechia', 'Prague')
    ccd.add_data('Poland', 'Warsaw')


if __name__ == "__main__":
    main()





countries_capitals = {
    'Czechia': 'Prague',
    'Poland': 'Warsaw',
    'Ukraine': 'Kyiv'
}
