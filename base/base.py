from time import sleep

import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Base:
    # 初始化
    def __init__(self, driver):
        """实例化传入的driver"""
        self.driver = driver

    # 查找 方法封装
    def base_find(self, *loc, timeout=10, poll=0.5):
        """
        :param loc:格式为列表或元组，内容：定义查找方式，参数
        :param timeout:超时时间，默认30秒
        :param poll:运行频率，默认0.5秒
        :return:元素
        """
        """
            1.设置一个等待，防止测试时有元素未加载完成
            2.设置一个查找元素的底层函数
            3.返回查找到的元素
            note:
                locals():以字典类型，返回当前函数中声明的局部变量（'z':'1','x':'2'）
                    x其实就是driver
                timeout:超时时间（sec）
                poll_frequency:运行频率（sec）
                until：等待返回一个true或者false
        """
        # return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll) \
        #     .until(lambda x: x.find_element(*loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(

            ec.presence_of_element_located(*loc)
        )

    # 输入 方法封装
    def base_input(self, loc, value):
        """
        :param loc: 定位元素
        :param value: 要输入的数据
        """
        # 1.找到该元素
        el = self.base_find(loc)
        # 2.清空输入框
        el.clear()
        # 3.输入数值
        el.send_keys(value)

    # 点击 方法封装
    def base_click(self, loc):
        """
        :param loc:  定位元素
        """
        self.base_find(loc).click()

    # 获取元素文本 方法封装
    def base_get_text(self, loc):
        """
        :param loc: 定位元素
        :return: 返回文本值
        """
        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        # 1. 调用截图方法
        self.driver.get_screenshot_as_file("../image/err.png")
        # 2. 调用截图写入报告方法
        self.__base_write_img()

    # 将图片写入报告方法（私有）
    def __base_write_img(self):
        # 1.获取图片文件流
        with open("../image/err.png", "rb") as f:
            # 2.调用allure.attach附加方法("附件主体","备注","附件类型")
            allure.attach(f.read(), "错误原因:", allure.attachment_type.PNG)
