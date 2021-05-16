from selenium import webdriver


class GetDriver:
    # 1.声明变量
    __web_driver = None

    # 2.获取driver方法
    """
        关于类方法@classmethod: 不需要进行实例化
    """
    @classmethod
    def get_web_driver(cls, url):
        # 判断是为空
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome('E:/PycharmProjects/uiAutoTestHmtt/tools/chromedriver.exe')
            # 浏览器最大化
            # cls.__web_driver.maximize_window()
            # 打开URL
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver

    # 3.退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断不为空
        if cls.__web_driver:
            # 退出浏览器
            cls.__web_driver.quit()
            # 置空
            """
                注意：对象地址还不为空，
                    所以需要置空
            """
            cls.__web_driver = None

# 没问题
# if __name__ == '__main__':
#     driver = GetDriver.get_web_driver('http://ttmp.research.itcast.cn/#/login')
#     GetDriver.quit_web_driver()