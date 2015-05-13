#-*-coding=utf-8
from selenium import webdriver
import unittest,time,re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

class Dingjia(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.base_url = "http://cp.360.cn"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_dingjia(self):
        driver = self.driver
        driver.get(self.base_url+"/sscjx")

        i=1
        while(i<100):
            # print driver.find_element_by_xpath(u'//b[1]').text
            #print driver.find_element_by_xpath(u'//span[1]').text
            ss="v countdown"
            print ss
            print driver.find_element_by_xpath("//span[@class='v countdown']").text

            time.sleep(2)

if __name__ == "__main__":
    unittest.main()

#     def test_dingjia(self):
#         driver = self.driver
#         driver.get(self.base_url + "/dbackup")
#         time.sleep(3)
#         handle = driver.window_handles
#         driver.switch_to_frame(0)
#         driver.find_element_by_id("serialRadio").click()
#         driver.find_element_by_id("trialRadio").click()
#         driver.find_element_by_xpath("//div[3]/label").click()
#         driver.find_element_by_id("continue").click()
#         driver.switch_to_window(handle)
#         driver.find_element_by_id("UserNameID").send_keys("admin")
#         driver.find_element_by_id("PWID").send_keys("admin")
#         driver.find_element_by_id("LoginButton").click()
#         alert = self.driver.switch_to_alert()
#         addFTP(driver,"ftp1831","192.168.88.183","irene","dingjia","183FTP/complicate")
# #        alert.accept()
# #------------------------------登录进来了-------------------------------------
#         def addFTP(driver,name,ip,lname,lpasswd,dir):
#             action_chains = ActionChains(driver)
#             time.sleep(3)
#             action_chains.move_to_element(driver.find_element_by_link_text("存储服务器")).perform()
#             action_chains.click(driver.find_element_by_link_text("添加存储服务器")).perform()
#             time.sleep(3)
#             driver.find_element_by_id("strFTPNameID").send_keys(name)
#             se = driver.find_element_by_id("protocalSelect")
#             se.find_element_by_xpath("//option[@value='ftp']").click()
#             time.sleep(3)
#             driver.find_element_by_css_selector("input.input").send_keys(ip)
#             driver.find_element_by_id("strFTPLoginNameID").send_keys(lname)
#             driver.find_element_by_id("strFTPLoginPWID").send_keys(lpasswd)
#             driver.find_element_by_id("nPathID").send_keys(dir)
#             driver.find_element_by_id("nRemanentDateNumID").send_keys("1")
#             driver.find_element_by_id("Submit").click()
#             alert = self.driver.switch_to_alert()
#             alert.accept()
# #------------------------------添加存储服务器成功--------------------------------
#         time.sleep(5)
# #------------------------------注册用户------------------------------------------
#         def addUser(name,passwd,confirmpasswd,email,telephone):
#             action_chains.move_to_element(driver.find_element_by_link_text("用户管理")).perform()
#             action_chains.click(driver.find_element_by_link_text("注册用户")).perform()
#             driver.find_element_by_id("username").send_keys(name)
#             driver.find_element_by_id("password").send_keys(passwd)
#             driver.find_element_by_id("confirmpassword").send_keys(confirmpasswd)
#             driver.find_element_by_id("email").send_keys(email)
#             driver.find_element_by_id("telephone").send_keys(telephone)
#         driver.switch_to_frame(0)
#         time.sleep(5)
#         driver.find_element_by_link_text("监控管理").click()
#         driver.switch_to_frame(0)
#         time.sleep(5)
#         driver.find_element_by_link_text("退出").click()
#         time.sleep(5)

