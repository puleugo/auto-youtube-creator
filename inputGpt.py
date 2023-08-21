from xml.dom import DOMException
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.common.by import By
import time
import zipfile
import os
import time
import shutil

load_dotenv()

notion_email = os.getenv('NOTION_EMAIL')
notion_password = os.getenv('NOTION_PASSWORD')
notion_token = os.getenv('NOTION_TOKEN')
download_path = os.getenv('DOWNLOAD_PATH')
gpt_file_path= os.getenv('GPT_FILE_PATH')
input_file_path = os.getenv('INPUT_FILE_PATH')

def notion_login():
    notion_options = Options()
    notion_options.add_experimental_option("detach", True)
    driver = EC.Chrome(options=notion_options)
    
    driver.get('https://www.notion.so/41b2a55d2700425685a794050cbd3989?v=c52bb740e37b4b7f9c3aeae534fecdeb')

    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/main/div/div[3]/div[1]/div[3]/form/div[1]/input').send_keys(notion_email)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/main/div/div[3]/div[1]/div[3]/form/div[3]').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/main/div/div[3]/div[1]/div[3]/form/div[2]/input').send_keys(notion_password)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="notion-app"]/div/div[1]/div/div/main/div/div[3]/div[1]/div[3]/form/div[3]').click()

    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/header/div[1]/div/div[3]/div[2]/div[5]').click()
    driver.find_element(By.XPATH ,'/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[5]/div[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[6]/div[2]').click()

def search_download_file(start_file,end_file):
    current_time = time.time()  
    five_minutes_ago = current_time - 5 * 60  # 5분 전 시간을 계산

    files = os.listdir(start_file)

    moved_files = []

    for file in files:
        full_file_path = os.path.join(start_file, file)
        file_creation_time = os.path.getctime(full_file_path)  

        if file.endswith('.zip') and file_creation_time >= five_minutes_ago:
            target_file_path = os.path.join(end_file, file)
            shutil.move(full_file_path, target_file_path) 
            moved_files.append(file)

    return None  

def decompression(start_file, end_file):
    files = os.listdir(start_file)
    for file in files:
        if file.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(start_file, file)) as existing_zip:
                existing_zip.extractall(end_file)
            os.remove(os.path.join(start_file, file))

    return None


if __name__ == '__main__':
    notion_login()
    time.sleep(10)
    search_download_file(download_path, gpt_file_path)
    time.sleep(10)
    decompression(gpt_file_path, input_file_path)
    


