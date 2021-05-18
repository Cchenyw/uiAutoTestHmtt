from page.page_mp_login import PageMpLogin
from page.page_xlw_login import PageXlwLogin


class PageIn:

    def __init__(self, driver):
        self.driver = driver

    # PageMpLogin
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)

    def page_get_PageXlwLogin(self):
        return PageXlwLogin(self.driver)
