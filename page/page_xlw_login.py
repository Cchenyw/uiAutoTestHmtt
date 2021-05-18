from base.base import Base
import page


class PageXlwLogin(Base):

    # 1.输入用户名
    def page_input_username(self, username):
        self.base_input(page.xlw_username, username)

    # 2.输入密码
    def page_input_password(self, password):
        self.base_input(page.xlw_password, password)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.xlw_login_btn)

    # 获取登录成功之后的用户名 ->asset
    def page_get_nickname(self):
        return self.base_get_text(page.xlw_success_username)

    # 组合业务方法 -> 测试脚本层调用
    def page_xlw_login(self, username, password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
        self.page_get_nickname()
