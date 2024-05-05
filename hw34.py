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
            print("Data saved successfully.")

    def load_data(self, filename):
        with open(filename, "rb") as file:
            self.data = pickle.load(file)
            print("Data loaded successfully.")

    def __str__(self):
        return f"{self.data}"


def main():
    ccd = CountryCapitalDict()
    ccd.add_data('Czechia', 'Prague')
    ccd.add_data('Poland', 'Warsaw')
    print(ccd.find_data("Czechia"))
    ccd.edit_data('Czechia', 'Ostrava')
    print(ccd.find_data("Czechia"))
    ccd.delete_data("Czechia")
    print(ccd.find_data("Czechia"))
    ccd.save_data("data.pkl")
    ccd.load_data("data.pkl")
    # loaded_data = ccd.load_data("data.pkl")
    # print(f"Loaded data from file: {loaded_data}")


if __name__ == "__main__":
    main()

