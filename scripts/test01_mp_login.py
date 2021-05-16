import allure
import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.read_yaml import read_yaml


class TestMpLogin:
    """
        自媒体登录测试-业务层结构搭建
    """

    # 初始化
    def setup_class(self):
        # 1.获取driver
        driver = GetDriver.get_web_driver(page.url_mp)
        # 2.通过统一入口类PageIn获取PageMpLogin对象
        self.mp = PageIn(driver).page_get_PageMpLogin()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    """
        注意：
        1.同名函数的引用 tools.read_yaml.read_yaml(),单纯引入real_yaml包会报错
    """

    @pytest.mark.parametrize("username,code,expect", read_yaml("mp_login.yaml"))
    @allure.step("第一步:登录测试")
    def test_mp_login(self, username, code, expect):
        # 1.调用登录业务方法
        self.mp.page_mp_login(username, code)
        # 2.断言(assert就是普通声明)
        try:
            assert expect == self.mp.page_get_nickname()
        except Exception as e:
            # 輸出错误信息
            print("错误原因为:", e)
            # 截图
            self.mp.base_get_img()
            # 抛出异常
            raise
            # 3.调用关闭
        self.teardown_class()
        pass
