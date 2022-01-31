class Bike:
    def __init__(self, description, cost, sale_price, condition,sold):
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition
        self.sold = sold
    def sell(self):
        self.sold = self.sold
    def update_sale_price(self,sale_price):
        if self.sold == True:
            print('Action not allowed, Bike has already been sold')
        else:
            self.sale_price = sale_price
bike1 = Bike('Univega Alpina, orange', 100, 500, 0.5,True)
bike1.update_sale_price(350)
bike1.sell()