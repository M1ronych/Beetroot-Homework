class Product:
    def __init__(self,type_,name,price):
        self.type = type_
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0.0

    def add(self,product,amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        store_price = product.price * 1.3

        if product.name in self.products:
            self.products[product.name]["amount"] += amount
        else:
            self.products[product.name] = {
                "product":product,
                "amount":amount,
                "price":store_price
            }
    def set_discount(self,identifier,percent,identifier_type='name'):
        if percent < 0 or percent > 100:
            raise ValueError("Discount percent must be between 0 and 100")

        found = False

        for item in self.products.values():
            product = item["product"]

            if identifier_type == "name" and product.name == identifier:
                item["price"] = item["price"] * (1 - percent/100)
                found = True

            elif identifier_type == "type" and product.type == identifier:
                item["price"] = item["price"] * (1 - percent/100)
                found = True

        if not found:
            raise ValueError("No products match the given identifier")

    def sell_product(self,product_name,amount):
        if product_name not in self.products:
            raise ValueError("Product not found")

        if amount <= 0:
            raise ValueError("Amount must be positive")

        item = self.products[product_name]

        if item["amount"] < amount:
           raise ValueError("Not enough product in store")

        item["amount"] -= amount
        self.income += item["price"] * amount

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(info["product"].name,info["amount"]) for info in self.products.values()]

    def get_product_info(self,product_name):
        if product_name not in self.products:
            raise ValueError("Product not found")

        return product_name,self.products[product_name]["amount"]

p = Product('Sport','Football T-Shirt',100)
p2 = Product('Food','Ramen',1.5)

s = ProductStore()
s.add(p,10)
s.add(p2,300)
s.sell_product('Ramen',10)

assert s.get_product_info('Ramen') == ('Ramen',290)


