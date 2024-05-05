import pickle
import json

# Supplement the Car class with the ability to pack and unpack data using json and pickle.


class Car:
    type = "Passenger car"

    def __init__(self, model, year, manufacturer, engine, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine = engine
        self.color = color
        self.price = price

    def pack_pickle(self):
        return pickle.dumps(self)

    @classmethod
    def unpack_pickle(cls, pickle_data):
        return pickle.loads(pickle_data)

    def pack_json(self):
        return json.dumps(self.__dict__)

    @classmethod
    def unpack_json(cls, json_data):
        data = json.loads(json_data)
        return cls(**data)


car1 = Car("Civic", 2004, "Honda", 1.6, "grey", 1500)
car2 = Car("Fusion", 2010, "Ford", 1.4, "red", 5000)


def main():
    # pickle packing
    pickle_data = car1.pack_pickle()
    print(f"Saved data to pickle file: \n {pickle_data}")
    from_pickle_car = Car.unpack_pickle(pickle_data)
    print(f"Loaded data from pickle file: \n {from_pickle_car.__dict__}")
    # json packing
    json_data = car2.pack_json()
    print(f"Saved data to json file: \n {json_data}")
    from_json_car = Car.unpack_json(json_data)
    print(f"Loaded data from json file: \n {from_json_car.__dict__}")


if __name__ == "__main__":
    main()
