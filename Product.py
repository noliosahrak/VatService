class Product:

    def __init__(self, product_id, net_price, product_type):
        self.product_type = product_type
        self.product_id = product_id
        self.net_price = net_price

    def get_net_price(self):
        return self.net_price

    def get_product_type(self):
        return self.product_type
