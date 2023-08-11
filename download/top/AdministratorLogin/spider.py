import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# 模拟键盘输入和按键
from selenium.webdriver.common.keys import Keys
# 进程
import multiprocessing
# 线程
import threading

from top.AdministratorLogin.temp2 import crawl
from top.AdministratorLogin.temp2 import getChromewithNohead

from top.allMenue.menueofcomicspider import comicmenue



# 函数调用顺序 getHTML(self, webPath)->def getFirstpage(self)->def get_page(self, selection, number,choose)
class steal_spider():

    def releaseResources(self, chrome):
        chrome.close()

    def __init__(self):
        self.base_url = "https://www.kuaikanmanhua.com"

    # 获取快看漫画网站首页的全部源代码(用于解析,主要是为了拿到分类地址,然后再跳转到分类界面)
    def getHTML(self, webPath):
        res = requests.get(webPath)
        res.encoding = 'utf-8'
        return res.text

    # 拿到每一个分类的地址(在这个网页中上面是列举了漫画的所有分类,下面是列举了一些具体的这个类型的小说)
    def getFirstpage(self):
        # 调用getHTML()函数,获取到首页的源代码,进行解析再获得到 分类 这个栏目的跳转地址
        res = self.getHTML(self.base_url)
        bs = BeautifulSoup(res, 'lxml')
        a_tag = bs.select('#HomeHeader > div.headerContent > div > ul > li:nth-child(2) > div > a:nth-child(1)')[0]
        new_url = self.base_url + a_tag.get("href")
        return new_url  # https://www.kuaikanmanhua.com/tag/0

    # 现在我们已经跳转到了分类这个栏目,进入网页后可以看到很多的分类,这个函数就是为了解析得到
    # 每一个类型页面的跳转地址,从进入到每一个类型页面,再进行后续跳转
    def get_page(self, selection, number,choose):
        # self.driver = webdriver.Chrome()
        # o=Options()
        # o.add_argument('--headless')
        # driver=webdriver.Chrome(options=o)
        driver = getChromewithNohead()
        # self.driver.get(self.getFirstpage())
        driver.get(self.getFirstpage())

        tag = None
        type = None
        if selection == '1':
            # 恋爱类型的tag
            lover_tag = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[2]/a[2]')
            tag = lover_tag
            type = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[2]/a[2]').text
        elif selection == '2':
            # 古风类型的tag
            ancient_tag = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[2]/a[3]')
            tag = ancient_tag
            type = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[2]/a[3]').text
        elif selection == '3':
            # 穿越类型的tag
            passThrough_tag = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[2]/a[4]')
            tag = passThrough_tag
            type = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[2]/a[4]').text
        elif selection == '4':
            # 大女主类型的tag
            youth_tag = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[2]/a[5]')
            tag = youth_tag
            type = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[2]/a[5]').text
        elif selection == '5':
            # 青春类型的tag
            fantasy_tag = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[2]/a[6]')
            tag = fantasy_tag
            type = driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[2]/div[2]/div[2]/a[6]').text

        # 点击恋爱标签进行跳转
        tag.click()

        # 爬取点击恋爱类型后的界面
        # 1.操作浏览器下拉至浏览器底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        # 2.获取恋爱风格中所有的div包括的图片封面
        div_list = driver.find_elements(By.XPATH, '//*[@id="__layout"]/div/div[1]/div[3]/div')

        urlList = []
        for div in div_list:
            a_src = div.find_element(By.XPATH, "./a").get_attribute("href")
            urlList.append(a_src)

        threads = []
        i = 1
        for url in urlList:
            if i <= int(number):
                # from top.AdministratorLogin.temp2 import crawl
                # 调用crawl
                t = threading.Thread(target=crawl, args=(url,type,choose))
                threads.append(t)
                t.start()
                i += 1
            else:
                break

        for t in threads:
            t.join()

        # print(list)
        # 关闭打开的页面
        self.releaseResources(driver)
        print("=" * 115)

    # def menueShow(self):
    #     print("1.开启恋爱类型漫画的爬取")
    #     print("2.开启古风类型漫画的爬取")
    #     print("3.开启穿越类型漫画的爬取")
    #     print("4.开启青春类型漫画的爬取")
    #     print("5.开启奇幻类型漫画的爬取")
    #     print("6.开启古风和奇幻类型漫画的爬取")
    #     print("7.开启穿越和青春类型漫画的爬取")
    #     print("8.同时开启上述类型漫画的爬取")

    def main_loop(self):
        comicmenue().menueShow()
        selection = input("请输入的你选择:")
        number = input("请输入你要爬取多少本此类型的小说:")
        choose=input("1-只启动插入功能;2-同时启动插入和爬取每章节图片功能")
        # 创建进程并传递参数
        p1 = multiprocessing.Process(target=self.get_page, args=('1', number,choose))
        p2 = multiprocessing.Process(target=self.get_page, args=('2', number,choose))
        p3 = multiprocessing.Process(target=self.get_page, args=('3', number,choose))
        p4 = multiprocessing.Process(target=self.get_page, args=('4', number,choose))
        p5 = multiprocessing.Process(target=self.get_page, args=('5', number,choose))

        if selection == "1":
            p1.start()
            p1.join()
        elif selection == "2":
            p2.start()
            p2.join()
        elif selection == "3":
            p3.start()
            p3.join()
        elif selection == "4":
            p4.start()
            p4.join()
        elif selection == "5":
            p5.start()
            p5.join()
        elif selection == "6":
            p2.start()
            p5.start()
            p2.join()
            p5.join()
        elif selection == "7":
            p3.start()
            p4.start()
            p3.join()
            p4.join()
        elif selection == "8":
            # 启动进程
            p1.start()
            p2.start()
            p3.start()
            p4.start()
            p5.start()

            # 等待进程结束
            p1.join()
            p2.join()
            p3.join()
            p4.join()
            p5.join()
        elif selection == "0":
            print("终止选择,退出爬虫系统!")
        else:
            print("输入不合法,请重新输入!")


if __name__ == '__main__':
    spider = steal_spider()
    spider.main_loop()
