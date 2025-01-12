from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    
    def __init__(self) -> None:
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def open_url(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.close()