class VatProvider:
    @staticmethod
    def get_default_vat():
        return 0.23

    @staticmethod
    def get_vat_for_type(product_type):
        if product_type == "bread":
            return 0.05
        if product_type == "chocolate":
            return 0.08
        else:
            return 0.23
