# 通过webdriver操纵进行查找
from selenium import webdriver
import time
# 通过keys模拟键盘
from selenium.webdriver.common.keys import Keys

# 操纵哪个浏览器就对哪个浏览器建一个实例
# 自动按照环境变量查找相对应的浏览器
driver = webdriver.Chrome(executable_path=)
url = "http://www.baidu.com"
driver.get(url)

text = driver.find_element_by_id("wrapper").text
print(text)
print(driver.title)
driver.seve_screentshot("index.png")
driver.find_element_by_id("kw").send_keys(u"大熊猫")
driver.find_element_by_id("su").click()
time.sleep(5)
driver.save_screenshot("daxiongmao.png")
print(driver.get_cookies())
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")
driver.find_element_by_id("kw").send_keys(u"航空母舰")
driver.save_screenshot("hangmu.png")
driver.find_element_by_id("kw").clear()
driver.save_screenshot("clear.png")
driver.quit()
