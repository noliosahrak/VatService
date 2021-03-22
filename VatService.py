class VatService:

    def __init__(self):
        self.vatValue = 0.23

    def get_gross_price_for_default_vat(self, product):
        return self.get_gross_price(product.getNetPrice(), self.vatValue)

    @staticmethod
    def get_gross_price(net_price, vat_value):
        if vat_value > 1:
            raise Exception("VAT should be lower")

        return net_price * (1 + vat_value)
