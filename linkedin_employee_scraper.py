from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import sys
import time

if len(sys.argv) < 2:
    print('Usage: python linkedin_employee_scraper.py "https://www.linkedin.com/COMPANY/people/"')
    sys.exit(1)

home_dir = os.path.expanduser("~")

if os.name == 'nt': 
    user_data_dir = os.path.join(home_dir, r"AppData\Local\Google\Chrome\User Data")
    profile_dir = "Default"
else: 
    user_data_dir = os.path.join(home_dir, ".config/google-chrome")
    profile_dir = "Default"

option = webdriver.ChromeOptions()
option.add_argument("--headless") 
option.add_argument("--no-sandbox")  
option.add_argument("--disable-dev-shm-usage")
option.add_argument("--log-level=3")
option.add_argument(f"--user-data-dir={user_data_dir}")
option.add_argument(f"--profile-directory={profile_dir}")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=option)
driver.get(sys.argv[1])

print("Please close all Chrome windows before running this script.")

time.sleep(5)

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

profiles = driver.find_elements(By.CLASS_NAME, 'org-people-profile-card__profile-info')

error_count = 0
with open('linkedin_profiles.csv', 'w', encoding='utf-8') as file:
    for profile in profiles:
        try:
            link_element = profile.find_element(By.CSS_SELECTOR, "a[data-test-app-aware-link]") 
            
            profile_link = link_element.get_attribute("href").split('?')[0]
            name = profile.find_element(By.CSS_SELECTOR, 'div.lt-line-clamp.lt-line-clamp--single-line').text 
            description = profile.find_element(By.CSS_SELECTOR, 'div.lt-line-clamp.lt-line-clamp--multi-line').text
            
            file.write(f"{profile_link};{name};{description}\n")
        
        except Exception:
            error_count += 1

if error_count > 0:
    print(f"Total profiles with errors: {error_count}.")
    print("If other profiles were processed without issues, the ones with errors are most likely private.")
else:
    print("All profiles processed successfully.")

driver.quit()