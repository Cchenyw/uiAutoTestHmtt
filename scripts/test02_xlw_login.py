from time import sleep

import allure
import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml


class TestXlwLogin:

    # 初始化
    def setup_class(self):
        driver = GetDriver.get_web_driver(page.url_xlw)
        self.xlw = PageIn(driver).page_get_PageXlwLogin()

    def teardown_class(self):
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("username,password,expect", read_yaml("xlw_login.yaml"))
    @allure.step("第一步：登陆测试")
    def test_xlm_login(self, username, password, expect):
        # 调用登录方法
        self.xlw.page_xlw_login(username, password)
        # 断言
        try:
            assert expect == self.xlw.page_get_nickname()
        except Exception as e:
            # 收集测试信息
            print("错误原因：", e)
            self.xlw.base_get_img()
            raise
        # 调用关闭
        sleep(3)
        self.teardown_class()
