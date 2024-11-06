from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import sys
import time

if len(sys.argv) < 3:
    print('Usage: python linkedin_employee_scraper.py "https://www.linkedin.com/COMPANY/people/" "path/to/chromedriver"')
    sys.exit(1)

service = Service(sys.argv[2])

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
            link_element = profile.find_element(By.CSS_SELECTOR, "a.app-aware-link")
            
            profile_link = link_element.get_attribute("href").split('?')[0]
            name = profile.find_element(By.CLASS_NAME, 'org-people-profile-card__profile-title').text
            description = profile.find_element(By.CLASS_NAME, 'artdeco-entity-lockup__subtitle').text
            
            file.write(f"{profile_link};{name};{description}\n")
        
        except Exception:
            error_count += 1

if error_count > 0:
    print(f"Total profiles with errors: {error_count}")
else:
    print("All profiles processed successfully.")

driver.quit()