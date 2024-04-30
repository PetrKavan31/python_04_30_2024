import pickle
# 1.priklad
# list1 = [1,2,3,4,5]
# pickle_list = pickle.dumps(list1)
# load_list = pickle.loads(pickle_list)
# print(pickle_list)
# print(load_list)

# 2.priklad
#  nefunguje to - v prezentaci - pickle skrz funkce
# def save(filename):
#     a = pickle.dumps(filename)
#     return a
#
# def load(filename):
#     b = pickle.loads(filename)
#     return b
#
# list1 = [1,2,3,4,5]
# def main():
#     save(list1)
#     load()
#     print(list1)
#
# if __name__ == "__main__":
#     main()


# 3.prilad z prezentace - piklit přes třídy a pouzit matgicky operator (str?)
# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#
#     def get_full_name(self):
#         return f"{self.name}{self.last_name}"
#
# try:
#     p = Person("Bill", "Gates")
#     print(f"Original person:\n{p.get_full_name()}\n")
#     file_name = "person.dat"


