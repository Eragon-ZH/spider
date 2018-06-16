'''
利用Selenium+ChromeDriver+BeautifulSoup爬取自己的所有说说内容并下载
'''
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

# 登录，需要手动滑动验证
def login(uesername, password):
    username = uesername
    password = password

    login_url = "http://qzone.qq.com"
    driver.get(login_url)
    # 需要切换至登录的frame才能找到元素
    driver.switch_to.frame("login_frame")
    driver.find_element_by_id("switcher_plogin").click()
    driver.find_element_by_id("u").send_keys(uesername)
    driver.find_element_by_id("p").send_keys(password)
    driver.find_element_by_id("login_button").click()
    # 手动滑动验证码
    sleep(10)
# 获取页面
def download_page(uesername):
    url = "https://user.qzone.qq.com/" + uesername + "/311"
    driver.get(url)
    # 下滑到页面底部让全部内容加载
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    sleep(3)
    # 切换到说说内容所在的frame才能找到内容
    driver.switch_to.frame("app_canvas_frame")
    get_content(driver.page_source)
    # 找到title为“下一页”的a标签即为下一页的链接，循环点击下一页
    ele = driver.find_element_by_css_selector('a[title="下一页"]')
    while ele:
        ele.click()
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        sleep(3)
        get_content(driver.page_source)
        ele = driver.find_element_by_css_selector('a[title="下一页"]')
# 获取内容
def get_content(html):
    soup = BeautifulSoup(html, "xml")
    # 说说内容和时间都在li标签下class为“box bgr3”的div里
    shuoList = soup.find_all("div", {"class": "box bgr3"})
    # 图片在img-xxx的div中
    imgList = soup.find_all("div", {"class": "img-attachments-inner clearfix"})
    shuoContentList = []
    imgSrcList = []
    for i in shuoList:
        shuoContent = i.find("pre", {"class": "content"}).getText()
        shuoTime = i.find("a", {"class": "c_tx c_tx3 goDetail"}).get("title")
        shuoContentList.append([shuoTime,shuoContent])
    for i in imgList:
        imgSrc = i.find_all("a")
        for j in imgSrc:
            imgSrcAddr = j.get("href")
            imgSrcList.append(imgSrcAddr)
    # 图片地址
    with open("imgAddr.txt","a+") as f:
        for i in imgSrcList:
            f.write(i+"\n")
    # 时间和内容
    with open("shuoshuo.txt","a+", encoding="utf-8") as f:
        for i in shuoContentList:
            f.write(i[0]+"\n")
            f.write(i[1]+"\n")
            f.write("=="*50+"\n")
        f.close()

def main():
    uesername = 你的QQ号
    password = 你的密码
    login(uesername, password)
    download_page(uesername)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    main()
