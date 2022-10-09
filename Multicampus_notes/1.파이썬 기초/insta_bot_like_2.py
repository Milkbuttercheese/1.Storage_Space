from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

class LikeBot:
    def __init__(self):
        self.querry = "https://www.instagram.com/explore/tags/"
        
        self.options = Options()
        
        self.options.add_argument("--window-size=1920, 1080")

        self.driver = webdriver.Chrome(executable_path="chromedriver.exe",
                                       chrome_options=self.options)

    def kill(self):
        self.driver.quit()
    
    def login(self, id, ps):
        self.driver.get("https://www.instagram.com/accounts/login/")
        
        time.sleep(5)
        
        input_field = self.driver.find_elements_by_tag_name("input")
        
        input_field[0].send_keys(id)
        
        input_field[1].send_keys(ps)

        input_field[1].send_keys(Keys.RETURN)
        
        time.sleep(5)
        
    def search_tag(self, tag):
        self.driver.get(self.querry + tag)
        
        time.sleep(5)

    # 최근 게시물 클릭 메서드
    def select_picture(self):
        recent_picture_xpath = "/html/body/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a/div"
        
        recent_picture = self.driver.find_element_by_xpath(recent_picture_xpath)
        
        recent_picture.click()
        
        time.sleep(5)
        
    def Like_pictures(self, num):
        count = num
        
        while count != 0:
            # count = count - 1
            count -= 1
            
            article = self.driver.find_elements_by_tag_name("svg")
            
            list_like = []
            
            for like_button in article:
                if like_button.get_attribute("aria-label") == "좋아요":
                    list_like.append(like_button)
            
            list_like[1].click()
            
            time.sleep(5)
            
            next_butten = "/html/body/div[6]/div[2]/div/div[2]/button/div"
            
            next_butten_element = self.driver.find_element_by_xpath(next_butten)
            
            next_butten_element.click()
            
            time.sleep(5)

    def insta_like_auto(self, tag, num):
        self.search_tag(tag)
        
        self.select_picture()
        
        self.Like_pictures(num)