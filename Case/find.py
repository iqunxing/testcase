#coding=utf-8
from unittest.test import test_suite

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import  time
import unittest
import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')
"""
在报错的页面添加代码： import sys
 reload(sys)
 sys.setdefaultencoding('utf8')

执行 Python ez_setup.py，报错：

UnicodeDecodeError: 'utf8' codec can't decode byte 0xb0 in position 35: invalid
  start byte

解决办法：

在报错的页面添加代码： import sys
 reload(sys)
 sys.setdefaultencoding('gb18030')

"""

class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_01(self):
        driver=self.driver
        driver.get("http://www.iqunxing.com/")#搜索百度
        try:
            lear_more=driver.find_element_by_link_text("关于群星")
            lear_more.click()
            time.sleep(3)
            assert "群星金融 - 让企业平等获得金融服务" in driver.title
        except NoSuchElementException:
            print"No such"
    time.sleep(9)
    def test_02(self):
        driver=self.driver
        try:
            log_In=driver.find_element_by_id("btnToLogin")
            log_In.click()
            time.sleep(3)

            username=driver.find_element_by_id("corpName")
            username.send_keys("zhoudaqiang")
            time.sleep(3)
        except NoSuchElementException:
            self.assertTrue(False, "找不到")
            print"no such element"
    def test_03(self):
        self.assertTrue(False,"测试失败")
if __name__ == "__main__":
    testsuite=unittest.TestSuite()
    testsuite.addTest(mytest("test_01"))
    testsuite.addTest(mytest("test_02"))
    testsuite.addTest(mytest("test_03"))
    filename = "d:\\result.html"
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Result', description='Test_Report')
    runner.run(testsuite)

