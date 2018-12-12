from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook
# ______________________________________________________
class STU:
    def __init__(self):
        self.target_url = "https://movie.naver.com/"
        #-------------------------------------
        self.options = Options()# 객체 생성
        self.options.add_argument("--headless")
        # self.options.binary_location = "C:\\Users\\sleep\\Desktop\\chrom_driver\\chromedriver.exe"
        # -------------------------------------
        self.driver = webdriver.Chrome \
            (executable_path="C:\\Users\\sleep\\Desktop\\chrom_driver\\chromedriver.exe",
             chrome_options=self.options)

        self.currentMov = {
            "reservMovi":{},   # 현재 상영영화 - 예매순 : reservMovi
            "releaseMovi":{},  # 현재 상영영화 - 개봉순 : releaseMovi
            "gradeMovi":{},    # 현재 상영영화 - 평점순 : gradeMovi
            "likeMovi":{},     # 현재 상영영화 - 좋아요순 : gradeMovi
        }
    # Instance method (1)
    def urlRequests(self):
        self.driver.get(self.target_url)
        assert "네이버 영화" in self.driver.title
        print (self.driver.title)
        time.sleep(2)
        # 상영작 예정작
        # menu02_on
        self.driver.find_element_by_xpath(
            '//*[@id="scrollbar"]/div[1]/div/div/ul/li[2]/a/strong').click()
        assert "현재 상영영화 : 네이버 영화" in self.driver.title
        print (self.driver.title)

    def requestReserve(self):
        # 예매순
        # //*[@id="content"]/div[1]/div[1]/div[2]/ul[2]/li[1]/a
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div[1]/div[1]/div[2]/ul[2]/li[1]/a').click();time.sleep(2)

        bsObject = BeautifulSoup(self.driver.page_source, "html.parser")
        mvList   = bsObject.select('dt.tit > a')

        for n, i in enumerate(mvList):
            self.currentMov["reservMovi"][n+1] = i.string
            print (i.string)

    def requestRelease(self):
        # 개봉순
        # //*[@id="content"]/div[1]/div[1]/div[2]/ul[2]/li[2]/a
        self.driver.find_element_by_xpath(
            '//*[@id="content"]/div[1]/div[1]/div[2]/ul[2]/li[2]/a').click();time.sleep(2)
        # #content > div.article > div:nth-child(1) > div.lst_wrap > ul > li:nth-child(1) > dl > dt > a
        bsObject = BeautifulSoup(self.driver.page_source, "html.parser")
        mvList = bsObject.select('dt.tit > a')
        for n, i in enumerate(mvList):
            self.currentMov["releaseMovi"][n+1] = i.string
            print (i.string)

def main():
    sNode = STU()
    sNode.urlRequests()
    # 개봉순
    sNode.requestRelease()
if __name__ == "__main__":
    main()