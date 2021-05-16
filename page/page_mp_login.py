from time import sleep

from base.base import Base
import page


class PageMpLogin(Base):
    # 1.输入用户名
    def page_input_username(self, username):
        # 调用父类函数 输入用户名
        self.base_input(page.mp_username, username)

    # 2.输入验证码
    def page_input_code(self, code):
        # 调用父类函数 输入验证码
        self.base_input(page.mp_code, code)

    # 3.点击登录按钮
    def page_click_login_btn(self):
        # 调用父类函数 点击登录
        """解决电脑运行速度比网速要快的方法，防止按钮还没加载出来"""
        sleep(3)
        self.base_click(page.mp_login_btn)
        self.base_click(page.mp_login_btn)

    # 4.获取昵称方法 -> 测试脚本层断言调用（是否成功）
    def page_get_nickname(self):
        # 调用父类函数 获取昵称文本
        return self.base_get_text(page.mp_nickname)

    # 组合业务方法 -> 测试脚本层调用
    def page_mp_login(self, username, code):
        """
            提示：调用相同页面操作步骤，跨页面不考虑
        """
        # 1.
        self.page_input_username(username)
        # 2.
        self.page_input_code(code)
        # 3.
        self.page_click_login_btn()
