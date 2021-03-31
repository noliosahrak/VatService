from random import randint
from unittest import mock

import pytest
from assertpy import assert_that

from Product import Product
from VatService import VatService


class TestVatService:
    @pytest.fixture
    def vat(self):
        self.vat_provider = mock.Mock()
        self.vat_service = VatService(self.vat_provider)

    def test_should_calculate_gross_price_for_default_vat(self, vat):
        # given
        product = self.generate_product(100, "clothes")
        self.vat_provider.get_default_vat.return_value = 0.23

        # when
        result = self.vat_service.get_gross_price_for_default_vat(product)

        # then
        assert_that(result).is_equal_to(123)

    def test_should_calculate_gross_price_for_other_vat_value(self, vat):
        # given
        product = self.generate_product(4, "bread")
        self.vat_provider.get_vat_for_type.return_value = 0.05

        # when
        result = self.vat_service.get_gross_price(product.get_net_price(), product.get_product_type())

        # then
        assert_that(result).is_equal_to(4.2)

    def test_should_raise_exception_when_vat_is_not_number(self, vat):
        # then
        assert_that(self.vat_service.calculate_gross_price).raises(Exception).when_called_with(1, "a4g5") \
            .is_equal_to("VAT should be numeric value")

    def test_should_raise_exception_when_vat_is_to_high(self, vat):
        # then
        assert_that(self.vat_service.calculate_gross_price).raises(Exception).when_called_with(1, 10) \
            .is_equal_to("VAT should be lower than 1")

    def test_should_raise_exception_when_vat_is_negative(self, vat):
        # then
        assert_that(self.vat_service.calculate_gross_price).raises(Exception).when_called_with(1, -1) \
            .is_equal_to("VAT should have positive value")

    @staticmethod
    def generate_product(net_price, product_type):
        return Product(str(randint(10000000, 99999999)), net_price, product_type)
