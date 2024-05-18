from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

INSTAGRAM = "https://www.instagram.com/"
USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"
ACCOUNT = "python.hub"

class InstagramFollowers:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chrome_options)


    def open_instagram(self):
        self.driver.get(url= INSTAGRAM)
        time.sleep(3)
        button = self.driver.find_element(By.XPATH, value='/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]').click()
        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        time.sleep(3)
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        time.sleep(5)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        time.sleep(4)
        save_info = self.driver.find_element(By.XPATH,
                                             value='//div[contains(text(), "Not now")]')
        if save_info:
            save_info.click()
        time.sleep(6)
        notification = self.driver.find_element(By.XPATH,
                                                value='//button[contains(text(), "Not Now")]')
        if notification:
            notification.click()
        else:
            notification = self.driver.find_element(By.XPATH, value='/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()

        time.sleep(5)

    def open_followers(self):
        time.sleep(5)
        self.driver.get(f"{INSTAGRAM}/{ACCOUNT}/followers")
        time.sleep(5)
        followers = self.driver.find_element(By.XPATH, value='//a[contains(text(), " followers")]')
        followers.click()
        time.sleep(5)
        scroll = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
        time.sleep(2)
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            time.sleep(2)

    def follow(self):
        scroll = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        all_buttons = scroll.find_elements(By.TAG_NAME, value='button')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(3)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()
                time.sleep(2)



