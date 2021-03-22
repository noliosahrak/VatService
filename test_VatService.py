from unittest import mock
from unittest.mock import patch, Mock

from Product import Product
from VatService import VatService


class TestVatService:
    def test_should_calculate_gross_price_for_default_vat(self):
        # given
        vat_service = VatService()
        mock_product = mock.Mock(name="product mock")
        mock_product.get_net_price.return_value = 100

        # when
        result = vat_service.get_gross_price_for_default_vat(mock_product)

        # then
        assert result == 123

    def test_should_calculate_gross_price_for_other_vat_value(self):
        # given
        vat_service = VatService()

        # when
        result = vat_service.get_gross_price(100, 0.08)

        # then
        assert result == 108
