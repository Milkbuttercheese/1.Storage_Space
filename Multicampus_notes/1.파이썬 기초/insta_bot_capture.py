#웹제어문
from selenium import webdriver
#해상도 조절
from selenium.webdriver.chrome.options import Options 
#키 입력하기
from selenium.webdriver.common.keys import Keys
import time 
import sys
import os

#기본설정 저장하기
class CaptureBot:
    
    #자동으로 기본실행되는 명령어
    def __init__(self):
        #인스타에서 특정 해시태그 검색주소:self.query+'태그이름'
        self.querry = "https://www.instagram.com/explore/tags/"
        #해상도 설정 => 객체에 설정하는 코드
        self.options= Options()
        self.options.add_argument('--window--size==1920, 1080')
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe'
                                       ,chrome_options= self.options)
    
    #프로그램 정지시키는 명령어
    def kill(self):
        self.driver.quit()
    
    #스크린샷 메소드
    def save_screenshot(self,filename):
        self.driver.save_screenshot(filename)
    
    #인스타그램 로그인 메소드
    def login(self,id,pw):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        input_field = self.driver.find_elements_by_tag_name("input")
        #id 입력
        input_field[0].send_keys(id)
        #pw 입력
        input_field[1].send_keys(pw)
        #엔터 입력 (비밀번호 위치)
        input_field[1].send_keys(Keys.RETURN)
        time.sleep(5)
        
    #특정 태그로 검색하기
    def search_tag(self,tag):
        self.driver.get(self.querry+tag)
        time.sleep(5)
        
    #최근 검색물 클릭 메소드
    def select_pic(self):
        recent_pic_xpath= "/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]"
        recent_pic= self.driver.find_element_by_xpath(recent_pic_xpath)
        recent_pic.click()  
        time.sleep(5)
        
    #반복문 메소드 
    def capture_pics(self,directory,num):
        folder= directory
        if folder not in os.listdir():
            os.mkdir(folder)
            
        count= num
        while count !=0:
            count = count - 1
            #사진 저장하기
            
            article_xpath="/html/body/div[6]/div[3]/div/article/div/div[1]/div/div/div[2]"

            article_element=self.driver.find_element_by_xpath(article_xpath)
            article_element.screenshot(directory+"/"+str(time.time())+ ".png" )
            time.sleep(3)
            
            #다음 사진 넘어가기
            next_btn='/html/body/div[6]/div[2]/div/div[2]/button/div/span'
            next_btn_element=self.driver.find_element_by_xpath(next_btn)
            next_btn_element.click()
            time.sleep(5)
            
    #메크로 메소드
    def insta_chapture_macro(self,tag,directory,num):
        self.search_tag(tag)
        self.select_pic()
        self.captrue_pictures(directory,num)
