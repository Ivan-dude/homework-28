class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop():
    __file_name = 'products.txt'
    def get_product(self):
        file = open(self.__file_name, 'r')
        list_of_products = file.read()
        file.close()
        return list_of_products

    def add(self, *products):
        for i in products:
            list_of_products = self.get_product()
            if i.name not in list_of_products:
                file = open(self.__file_name, 'a')
                file.write(f'{i}\n')
                file.close()
            else:
                print(f'Продукт {i.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_product())


