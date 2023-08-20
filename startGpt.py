from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

google_email = os.getenv('GOOGLE_EMAIL')
google_password = os.getenv('GOOGLE_PASSWORD')


def set_chatgpt():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = EC.Chrome(options=chrome_options)
    driver.get('https://chat.openai.com/auth/login')
    driver.implicitly_wait(5) 

    try:
        driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[4]/button[1]').click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div/button[1]').click()


    driver.find_element(By.XPATH, '/html/body/div/main/section/div/div/div/div[1]/div/form/div[1]/div/div/div/input').send_keys(google_email)
    driver.find_element(By.XPATH, '/html/body/div/main/section/div/div/div/div[1]/div/form/div[2]/button').click()
 

    driver.find_element(By.XPATH, '/html/body/div/main/section/div/div/div/form/div[2]/div/div[2]/div/input').send_keys(google_password)
    driver.find_element(By.XPATH, '/html/body/div/main/section/div/div/div/form/div[3]/button').click()
    
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="radix-:ri:"]/div[2]/div/div[4]/button').click()

if __name__ == '__main__':
    set_chatgpt()

