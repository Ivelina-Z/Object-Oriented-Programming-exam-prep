from unittest import TestCase, main
from unit_testing_class_shopping_cart.shopping_cart import ShoppingCart


class ShoppingCartTests(TestCase):
    def setUp(self):
        self.shop = ShoppingCart('Restation', 150.5)

    def test_init(self):
        self.assertEqual(self.shop.shop_name, 'Restation')
        self.assertEqual(self.shop.budget, 150.5)
        self.assertEqual(self.shop.products, {})

    def test_shop_name_validation(self):
        with self.assertRaises(ValueError) as ve:
            self.shop = ShoppingCart('restation1', 150.5)
        self.assertEqual(str(ve.exception), "Shop must contain only letters and must start with capital letter!")

    def test_exception_add_to_cart_expensive_product(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_to_cart('coffee maker', 100.0)
        self.assertEqual(str(ve.exception), 'Product coffee maker cost too much!')

    def test_successful_add_to_cart(self):
        result = self.shop.add_to_cart('chocolate', 3.50)
        self.assertEqual(self.shop.products, {'chocolate': 3.50})
        self.assertEqual(result, 'chocolate product was successfully added to the cart!')

    def test_exception_remove_from_cart_product_not_in_cart(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.remove_from_cart('coffee maker')
        self.assertEqual(str(ve.exception), 'No product with name coffee maker in the cart!')

    def test_remove_from_cart_successful(self):
        self.shop.products['coffee'] = 5.00
        self.shop.products['chocolate'] = 3.50
        result = self.shop.remove_from_cart('chocolate')
        self.assertEqual({'coffee': 5.00}, self.shop.products)
        self.assertEqual('Product chocolate was successfully removed from the cart!', result)

    def test_add(self):
        self.other_shop = ShoppingCart('Someshop', 200.0)
        self.other_shop.add_to_cart('coffee', 3.50)
        self.shop.add_to_cart('chocolate', 5)

        result = self.shop.__add__(self.other_shop)
        self.assertEqual(result.shop_name, 'RestationSomeshop')
        self.assertEqual(result.budget, 350.5)
        self.assertEqual(result.products, {'coffee': 3.50, 'chocolate': 5})

    def test_buy_products_successfully(self):
        self.shop.add_to_cart('chocolate', 5)
        self.shop.add_to_cart('coffee', 3.50)
        result = self.shop.buy_products()
        self.assertEqual(result, 'Products were successfully bought! Total cost: 8.50lv.')

    def test_exception_buy_products(self):
        self.shop.add_to_cart('coffee maker', 99.9)
        self.shop.add_to_cart('microwave', 80)
        with self.assertRaises(ValueError) as ve:
            self.shop.buy_products()
        self.assertEqual(str(ve.exception), 'Not enough money to buy the products! Over budget with 29.40lv!')


if __name__ == '__main__':
    main()
