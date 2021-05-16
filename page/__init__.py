from selenium.webdriver.common.by import By

"""以下数据为自媒体登录页面、后台管理页面的URL"""
# 自媒体
url_mp = "http://ttmp.research.itcast.cn/#/login"
# 后台管理
url_mis = "http://ttmis.research.itcast.cn/#/"

"""以下数据为自媒体模块配置"""
# 用户名
mp_username = (By.CSS_SELECTOR, "[placeholder='请输入手机号']")
# 验证码
mp_code = (By.CSS_SELECTOR, "[placeholder='验证码']")
# 登录按钮
mp_login_btn = (By.CSS_SELECTOR, '.el-button--primary')
# 昵称
mp_nickname = (By.CSS_SELECTOR, '.user-name')
