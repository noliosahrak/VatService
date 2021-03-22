from unittest import mock

import pytest
from assertpy import assert_that

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
        assert_that(result).is_equal_to(123)

    @pytest.mark.parametrize("net_price, vat_value, gross_price", [(20, 0.08, 21.6), (4, 0.05, 4.2)])
    def test_should_calculate_gross_price_for_other_vat_value(self, net_price, vat_value, gross_price):
        # given
        vat_service = VatService()

        # when
        result = vat_service.get_gross_price(net_price, vat_value)

        # then
        assert_that(result).is_equal_to(gross_price)

    def test_should_raise_exception_when_vat_is_to_high(self):
        # given
        vat_service = VatService()

        # then
        assert_that(vat_service.get_gross_price).raises(Exception).when_called_with(1, 10)\
            .is_equal_to("VAT should be lower")
