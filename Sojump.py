import random
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# # 选项的xpath
# base_xpaths = '//*[@id="divquestion{}"]/ul/li'
# # 选项的css_selector
# base_css_selectors = '#divquestion{} > ul > li:nth-child({})'
# # 允许填空选项的css_selector
# input_css_selectors = '#divquestion{} > ul > li:nth-child({}) > input.underline'
# //*[@id="drv14_1"]/td[2]/a //*[@id="drv14_7"]/td[3]/a
# '''适用的可能是除了上面的情况的问卷星'''
# 选项的xpath
base_xpaths = '//*[@id="div{}"]/div/div/div'
# 选项的css_selector
# 横着的选项
base_css_selectors = '#div{} >div.ui-controlgroup.two_column>div:nth-child({})>div'
# 竖着的选项
base_css_selectors2 = '#div{} >div.ui-controlgroup.column1>div:nth-child({})>div'
# 允许填空选项的css_selector
input_css_selectors = 'tqq{}_{}'
text_library = ['全日制学生', '生产人员', '销售人员', '市场/公关人员', '客服人员', '行政/后勤人员', '人力资源',
                '财务/审计人员', '文职/办事人员', '技术/研发人员', '管理人员', '教师', '顾问/咨询',
                '专业人士(如会计师、律师、建筑师、医护人员、记者等)', '其他']
count = 0
answer_14 = [6, 6, 4, 5, 6, 4, 2, 2]
class Wenjuanxing(object):
    # 初始化
    def __init__(self, url):
        self.url = url

    # 计数器
    def counter(self):
        global count
        count += 1
        w = print("第{}次运行".format(count))
        return w

    # 伪装selenium
    def weizhuang_selenium(self):
        # 躲避智能检测
        self.option = webdriver.ChromeOptions()
        self.option.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.option.add_experimental_option('useAutomationExtension', False)
        self.driver = webdriver.Chrome(options=self.option)
        self.driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                                    {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
        self.driver.get(self.url)

    # 01 单选题（随机选择）
    def danxuan(self, i, flag=1):
        global base_xpaths
        base_xpath = base_xpaths.format(i)
        a = self.driver.find_elements(by=By.XPATH, value=base_xpath)
        b = random.randint(1, len(a))
        if flag == 1:
            self.driver.find_element(by=By.CSS_SELECTOR,
                                    value=base_css_selectors.format(i, b)).click()
        else:
            self.driver.find_element(by=By.CSS_SELECTOR,
                                     value=base_css_selectors2.format(i, b)).click()
        return b

    # 02 单选题（只选择某个选项）
    def fixed_danxuan(self, i, b, flag=1):
        if flag == 1:
            self.driver.find_element(by=By.CSS_SELECTOR,
                                     value=base_css_selectors.format(i, b)).click()
        else:
            self.driver.find_element(by=By.CSS_SELECTOR,
                                     value=base_css_selectors2.format(i, b)).click()
        return b

    # 03 单选题（排除一个或一些选项）
    def excluded_danxuan(self, i, *args, flag=1):
        global base_xpaths
        base_xpath = base_xpaths.format(i)
        a = self.driver.find_elements(by=By.XPATH, value=base_xpath)
        c = []
        # y是计算arg的个数，方便计算还剩几个选项
        y = 0
        for x in range(1, len(a) + 1):
            c.append(x)
        for arg in args:
            y += 1
            c.remove(arg)
        b = random.choice(c)
        if flag == 1:
            self.driver.find_element(by=By.CSS_SELECTOR,
                                     value=base_css_selectors.format(i, b)).click()
        else:
            self.driver.find_element(by=By.CSS_SELECTOR,
                                     value=base_css_selectors2.format(i, b)).click()
        return b

    # 04 单选题（在m到n范围内单选）
    # def range_danxuan(self, i, m, n):
    #     x = random.randint(m, n)
    #     self.driver.find_element(by=By.CSS_SELECTOR,
    #                              value=base_css_selectors.format(i, x)).click()

    # 05 单选题（在某些选项中选择）如6个选项，在1235中单选
    def restrictive_danxuan(self, i, *args, flag=1):
        m = []
        for arg in args:
            m.append(arg)
        n = random.choice(m)
        if flag == 1:
            self.driver.find_element(by=By.CSS_SELECTOR,
                                     value=base_css_selectors.format(i, n)).click()
        else:
            self.driver.find_element(by=By.CSS_SELECTOR,
                                     value=base_css_selectors2.format(i, n)).click()
        return n

    # 06 单选题（选项中允许填空）
    # def textinput_danxuan(self, i, c, wenzi):
    #     global base_xpaths
    #     base_xpath = base_xpaths.format(i)
    #     a = self.driver.find_elements(by=By.XPATH, value=base_xpath)
    #     b = random.randint(1, len(a))
    #     self.driver.find_element(by=By.CSS_SELECTOR,
    #                              value=base_css_selectors.format(i, b)).click()
    #     if c == b:
    #         time.sleep(0.2)
    #         self.driver.find_element(by=By.CSS_SELECTOR,
    #                                  value=input_css_selectors.format(i, c)).send_keys(wenzi)

    # 07 多选题（随机选择）
    def duoxuan(self, i, flag=1):
        global base_xpaths
        base_xpath = base_xpaths.format(i)
        a = self.driver.find_elements(by=By.XPATH, value=base_xpath)
        b = len(a)
        # m中存放选项
        m = []
        for x in range(1, b + 1):
            m.append(x)
        c = random.randint(1, b)
        n = random.sample(m, c)
        for o in n:
            if flag == 1:
                self.driver.find_element(by=By.CSS_SELECTOR,
                                         value=base_css_selectors.format(i, o)).click()
            else:
                self.driver.find_element(by=By.CSS_SELECTOR,
                                         value=base_css_selectors2.format(i, o)).click()

    # 08 多选题（只选择某些选项）
    def fixed_duoxuan(self, i, *args, flag=1):
        for arg in args:
            if flag == 1:
                self.driver.find_element(by=By.CSS_SELECTOR,
                                         value=base_css_selectors.format(i, arg)).click()
            else:
                self.driver.find_element(by=By.CSS_SELECTOR,
                                         value=base_css_selectors2.format(i, arg)).click()

    # 09 多选题(排除一个或一些的选项)
    def excluded_duoxuan(self, i, *args, flag=1):
        global base_xpaths
        base_xpath = base_xpaths.format(i)
        a = self.driver.find_elements(by=By.XPATH, value=base_xpath)
        # print(len(a))
        c = []
        # y是计算arg的个数，方便计算还剩几个选项
        y = 0
        for x in range(1, len(a) + 1):
            c.append(x)
        for arg in args:
            y += 1
            c.remove(arg)
        # 还剩下几个选项
        z = len(a) - y
        # 多选题选项个数
        b = random.randint(1, z)
        # 多选题用sample（）
        d = random.sample(c, b)
        for r in d:
            if flag == 1:
                self.driver.find_element(by=By.CSS_SELECTOR,
                                         value=base_css_selectors.format(i, r)).click()
            else:
                self.driver.find_element(by=By.CSS_SELECTOR,
                                         value=base_css_selectors2.format(i, r)).click()

    # 10 多选题（在某些选项中多选）
    # def restrictive_duoxuan(self, i, *args):
    #     m = []
    #     for arg in args:
    #         m.append(arg)
    #     n = random.randint(1, len(m))
    #     o = random.sample(m, n)
    #     for q in o:
    #         self.driver.find_element(by=By.CSS_SELECTOR,
    #                                  value=base_css_selectors.format(i, q)).click()
    #
    # # 11 多选题（在m到n范围内的多选）
    # def range_duoxuan(self, i, m, n):
    #     # 列表c为m到n的选项组，如当m=2,n=5时，c=[2,3,4,5]
    #     c = []
    #     for x in range(m, n + 1):
    #         c.append(x)
    #     # 选项个数
    #     o = n - m + 1
    #     # 随机生成要填几个选项
    #     p = random.randint(1, o)
    #     d = random.sample(c, p)
    #     for r in d:
    #         self.driver.find_element(by=By.CSS_SELECTOR,
    #                                  value=base_css_selectors.format(i, r)).click()
    #
    # # 12 多选题（选项中允许填空）
    # def text_input_duoxuan(self, i, c, wenzi):
    #     global base_xpaths
    #     base_xpath = base_xpaths.format(i)
    #     a = self.driver.find_elements(by=By.XPATH, value=base_xpath)
    #     b = len(a)
    #     # m中存放选项
    #     m = []
    #     for x in range(1, b + 1):
    #         m.append(x)
    #     # 随机生成要多选的选项个数
    #     o = random.randint(1, b)
    #     # 在选项中随机选取o个选项
    #     n = random.sample(m, o)
    #     for r in n:
    #         self.driver.find_element(by=By.CSS_SELECTOR,
    #                                  value=base_css_selectors.format(i, r)).click()
    #         if c == r:
    #             time.sleep(0.2)
    #             self.driver.find_element(by=By.CSS_SELECTOR,
    #                                      value=input_css_selectors.format(i, c)).send_keys(wenzi)

    # 13 文本题
    def text(self, i, turn, wenzi):
        self.driver.find_element(by=By.CSS_SELECTOR, value='#div{} > div.field-label > div > div:nth-child(2) > '
                                                           'label:nth-child({}) > span'.format(i, turn)).send_keys(wenzi)

    # 框选题
    def kuangxuan(self, text_library):
        self.driver.find_element(by=By.CSS_SELECTOR, value='#div9 > div.ui-select > div > span > span.selection > '
                                                           'span > span.select2-selection__arrow').click()
        b = random.randint(2, len(text_library))
        self.driver.find_element(by=By.XPATH, value='/ html / body / span / span / span[2] / ul / li[{}]'
                                 .format(b)).click()

    # 自选框选
    # 框选题 /html/body/span/span/span[2]/ul/li[2]
    def fixed_kuangxuan(self, b):
        self.driver.find_element(by=By.CSS_SELECTOR, value='#div9 > div.ui-select > div > span > span.selection > '
                                                           'span > span.select2-selection__arrow').click()
        self.driver.find_element(by=By.XPATH, value='/ html / body / span / span / span[2] / ul / li[{}]'
                                 .format(b)).click()

    # 二维矩阵题 题目，有多少题，有多少项
    def matrix(self, i, m, n):
        for j in range(m):
            k = random.randint(2, n+1)
            self.driver.find_element(by=By.CSS_SELECTOR, value='#drv{}_{} > td:nth-child({}) > a'
                                     .format(i, j+1, k)).click()

    # 自选二维矩阵题 题目，有多少题，答案数组
    def fixed_matrix(self, i, m, answer):
        for j in range(m):
            self.driver.find_element(by=By.CSS_SELECTOR, value='#drv{}_{} > td:nth-child({}) > a'
                                     .format(i, j + 1, answer[j])).click()

    # 一维矩阵题
    def s_matrix(self, i, n):
        k = random.randint(2, n+1)
        self.driver.find_element(by=By.CSS_SELECTOR, value='#drv{}_1 > td:nth-child({}) > a'
                                 .format(i, k)).click()

    # 自选一维矩阵题
    def fixed_s_matrix(self, i, *args):
        k = random.choice(args)
        self.driver.find_element(by=By.CSS_SELECTOR, value='#drv{}_1 > td:nth-child({}) > a'
                                 .format(i, k)).click()

    # 提交按钮
    def submit(self):
        # time.sleep(0.5)
        btn = self.driver.find_element(by=By.CSS_SELECTOR, value='#divSubmit > div > div')
        btn.click()
        # 出现点击验证码验证
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value='//*[@id="layui-layer1"]/div[3]/a[1]').click()
        time.sleep(0.5)
        self.driver.find_element(by=By.XPATH, value='//*[@id="SM_BTN_1"]').click()
        time.sleep(4)
        # 关闭页面
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[0])
        # time.sleep(0.5)
        # # 刷新页面（可能不需要）
        # self.driver.refresh()
        # 关闭当前页面，如果只有一个页面，则也关闭浏览器
        self.driver.close()

    # 点击一下提交按钮
    def click_submit(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value='#divSubmit > div > div')



