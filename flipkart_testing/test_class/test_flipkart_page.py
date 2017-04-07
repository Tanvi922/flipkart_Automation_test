import nose.tools
import nose.plugins.multiprocess

from test_base import BaseTest
from page_class.flipkart_page import FlipkartPage


class TestFlipkartPage(BaseTest):

    _multiprocess_can_split_ = True

    @classmethod
    def setUpClass(self):
        super(TestFlipkartPage, self).setUpClass()
        self.flipkart_page = FlipkartPage(self._browser)
        self.flipkart_page.go_to_page()
        self.flipkart_page.maximize()

    def test_01_check_iphone6_search_working(self):
        nose.tools.assert_true(self.flipkart_page.search_for_iphone6())

    def test_02_click_on_mobile_category(self):
        nose.tools.assert_true(self.flipkart_page.click_on_mobile_category())

    def test_03_check_price_filter_working(self):
        self.flipkart_page.apply_price_filter()

    def test_04_check_brand_filter_working(self):
        nose.tools.assert_true(self.flipkart_page.apply_brand_filter())

    def test_05_check_exclude_out_of_stock_filter_working(self):
        nose.tools.assert_true(self.flipkart_page.apply_exclude_out_of_stock_filter_working())

    def test_06_get_product_details(self):
        self.flipkart_page.product_details()