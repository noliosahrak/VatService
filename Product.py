class Product:

    def __init__(self, product_id, net_price):
        self.product_id = product_id
        self.net_price = net_price

    def get_net_price(self):
        return self.net_price
