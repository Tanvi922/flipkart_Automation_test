# __author__ = 'tanvi'


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from collections import OrderedDict


from .page_base import AbstractBasePage


class FlipkartPage(AbstractBasePage):


    _FLIPKART_SEARCHBAR_LOCATOR = (By.CSS_SELECTOR, '[title*="Search for Products"]')
    _MOBILE_CATEGORY_LOCATOR = (By.CSS_SELECTOR, '._1a8kD8[title = "Mobiles"]')
    _MIN_FILTER_LOCATOR = (By.CSS_SELECTOR, '._1QaKk1 .a_eCSK')
    _APPLE_FILTER_LOCATOR = (By.CSS_SELECTOR, '[title="Apple"] ._1GEhLw')
    _AVALIBILITY_FILTER_LOCATOR = (By.CSS_SELECTOR, ' ._1fWl8W > div:nth-child(8) > section:nth-child(1) > div:nth-child(1)')
    _EXCLUDE_FILTER_LOCATOR = (By.CSS_SELECTOR, '._1fWl8W > div:nth-child(8) > section:nth-child(1) > div:nth-child(1)')
    _PRODUCT_NAME_LIST_LOCATOR = (By.CSS_SELECTOR, '._3wU53n')
    _PRODUCT_PRICE_LIST_LOCATOR = (By.CSS_SELECTOR, '._1vC4OE._2rQ-NK')
    _PRODUCT_CARD_LINK_LIST_LOCATOR = (By.CSS_SELECTOR, '._1UoZlX')

    def search_for_iphone6(self):
        return self.enter_field_input(self._FLIPKART_SEARCHBAR_LOCATOR, 'IPhone6'+Keys.ENTER)

    def click_on_mobile_category(self):
        return self.click_on_element(self._MOBILE_CATEGORY_LOCATOR)

    def apply_price_filter(self):
        res1 = self.get_page_element(self._MIN_FILTER_LOCATOR)
        select = Select(res1)
        select.select_by_value('35000')

    def apply_brand_filter(self):
        self.scroll_into_view(self._APPLE_FILTER_LOCATOR)
        return self.click_on_element(self._APPLE_FILTER_LOCATOR)

    def apply_exclude_out_of_stock_filter_working(self):
        self.scroll_into_view(self._AVALIBILITY_FILTER_LOCATOR)
        res1 = self.click_on_element(self._AVALIBILITY_FILTER_LOCATOR)
        res2 = self.click_on_element(self._EXCLUDE_FILTER_LOCATOR)
        return res1 and res2

    def product_details(self):
        name = self.get_text_of_elements(self._PRODUCT_NAME_LIST_LOCATOR)
        price = self.get_text_of_elements(self._PRODUCT_PRICE_LIST_LOCATOR)
        link = self.get_attribute_of_elements(self._PRODUCT_CARD_LINK_LIST_LOCATOR, 'href')
        price = [int(p.replace('₹','').replace(',','')) for p in price]
        l_dict = {}
        count = 0
        for elem in price:
            l_dict[elem] = (name[count], link[count])
            count += 1
        b = OrderedDict(sorted(l_dict.items()))
        for key, value in b.items():
            print(str(key) + ' | ' + value[0] + ' | ' + value[1])






