import logging
from time import sleep
import yaml
import allure
import logging
from selenium import webdriver


class TestSelenium:
    def setup(self):
        logging.info('设置浏览器驱动，窗口最大化，隐形等待设置为5s')
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    # 获取cookies
    @allure.story('获取cookies')
    @allure.title('获取cookies')
    def test_remote(self):
        # 设置复用
        logging.info('设置复用')
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        logging.info('复用设置成功')
        # 拿cookies并写入yaml文件 date.yaml中
        logging.info('将拿到的cookies并写入yaml文件 date.yaml中')
        cookies = self.driver.get_cookies()
        with open("date.yaml", "w", encoding='UTF-8') as f:
            yaml.dump(cookies, f)
        logging.info('写入文件成功')
        sleep(3)

    # 添加成员
    @allure.story('添加成员')
    @allure.title('添加成员')
    def test_selenium(self):
        # 打开扫码登录页面
        logging.info('打开扫码登录页面')
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
        # 调用复用的cookies
        logging.info('调用复用的cookies')
        with open("date.yaml", encoding='UTF-8') as f:
            cookies = yaml.safe_load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        logging.info('调用cookies成功')
        # 进入企业微信主页
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        logging.info('进入企业微信主页成功')
        sleep(1)
        # 点击通讯录
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        logging.info('进入通讯录页面成功')
        sleep(5)
        # 点击添加成员
        self.driver.find_element_by_link_text('添加成员').click()
        logging.info('成功进入添加成员页面')
        sleep(3)
        # 填写姓名
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('小韩1')
        logging.info('成功填写姓名')
        sleep(1)
        # 填写别名
        self.driver.find_element_by_xpath('//*[@id="memberAdd_english_name"]').click()
        self.driver.find_element_by_xpath('//*[@id="memberAdd_english_name"]').send_keys('小小韩1')
        sleep(1)
        logging.info('成功填写别名')
        # 填写账号
        self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').click()
        self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys('775778')
        sleep(1)
        logging.info('成功填写账号')
        # 填写手机号
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').click()
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys('18733506888')
        sleep(1)
        logging.info('成功填写手机号')
        # 其余非必填项未填，点击保存按钮，完成新增
        self.driver.find_element_by_link_text('保存').click()
        logging.info('成功保存')
        sleep(5)
        eles = self.driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")

        for x in eles:
            print(type(x.get_attribute("title")))
            print(x.get_attribute("title"))
            if "小韩" == x.get_attribute("title"):
                print('完成新增')
            else:
                print('失败')
        logging.info('完成新增')
