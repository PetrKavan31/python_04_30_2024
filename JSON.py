import json

# capitals = {"Italy": "Rome", "Spain": "Madrid", "Germany":"Berlin"}
#
# json_list = json.dumps(capitals)
# print(json_list)
# load_list = json.loads(json_list)
# print(load_list)



employees_dict = {
    "company": "ABC Corp",
    "employees": [
        {
            "name": "John Doe",
            "age": 30,
            "department": "Sales",
            "skills": ["negotiation", "communication", "CRM"]
        },
        {
             "name": "Jane Smith",
             "age": 35,
             "department": "Marketing",
             "skills": ["SEO", "content creation", "branding"]
        }
    ]
}


def save_data(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)


def load_data(filename):
    with open(filename, "r") as file:
        return json.load(file)


def main():

    # Filename to save data
    filename = "data.json"

    # Save data to file
    save_data(employees_dict, filename)

    # Load data from file
    loaded_list = load_data(filename)

    # Display the loaded data
    print("Data loaded from file:", loaded_list)


if __name__ == "__main__":
    main()