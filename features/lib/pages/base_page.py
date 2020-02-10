from selenium.webdriver.common.by import By
class BsePage:
    def __init__(self,driver):
        self.driver=driver
    def get_url(self,url):
        self.driver.get(url)
    def get_title(self):
        return self.driver.title
    def find_element(self,*loc):
        return self.driver.find_element(*loc)

