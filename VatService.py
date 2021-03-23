from VatProvider import VatProvider


class VatService:

    def __init__(self, vat_provider):
        self.vat_provider = vat_provider

    def get_gross_price_for_default_vat(self, product):
        return self.calculate_gross_price(product.get_net_price(), self.vat_provider.get_default_vat())

    def get_gross_price(self, product):
        vat_value = self.vat_provider.get_vat_for_type(product.get_product_type())
        return self.calculate_gross_price(product.get_net_price(), vat_value)

    @staticmethod
    def calculate_gross_price(net_price, vat_value):
        if vat_value > 1:
            raise Exception("VAT should be lower")
        return round(net_price * (1 + vat_value), 2)

