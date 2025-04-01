# Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


import time
import os

# User-defined inputs
from_dest = "Bengaluru"
to_dest = "New Delhi"
from_date = "29/03/2025"
return_date = "30/03/2025"

# Chrome options
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# Path to ChromeDriver (Update this path as needed)
driver_path = "C:\\chromedriver-win64\\chromedriver.exe"
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Opening Google Flights
driver.get("https://www.google.com/travel/flights")
time.sleep(2)
print("Opened Google Flights page")

# Entering destination
driver.switch_to.active_element.send_keys(to_dest)
time.sleep(1)

# Pressing tab twice to move to departure date field
actions = ActionChains(driver)
actions.send_keys(Keys.TAB).pause(0.5).send_keys(Keys.TAB).perform()
time.sleep(1)
print("Moved to departure date field")

# Enter departure date
driver.switch_to.active_element.send_keys(from_date)
time.sleep(1)
print(f"Entered Departure Date: {from_date}")

# Move to return date
actions.send_keys(Keys.TAB).perform()
time.sleep(1)
print("Moved to Return date field")

driver.switch_to.active_element.send_keys(return_date)
time.sleep(1)
print(f"Entered Return Date: {return_date}")

# Confirm selection
driver.switch_to.active_element.send_keys(Keys.ENTER)
actions.send_keys(Keys.TAB).pause(0.5).send_keys(Keys.TAB).perform()
time.sleep(1)

driver.switch_to.active_element.send_keys(Keys.ENTER)
print("Search initiated!")

# Ensure flight results load
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Scroll multiple times to load all flights
last_height = driver.execute_script("return document.body.scrollHeight")
for _ in range(5):  # Adjust number of scrolls if needed
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Increase wait time for better loading
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Wait for flights to load
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[2]/div[1]')))

# Extract flight details
divs = driver.find_elements(By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[2]/div[2]/div/div[2]/div[1]')
filtered_labels = [div.text for div in divs if div.text.strip() != ""]  # Extracting visible text

# Debugging: Print extracted data
print("Extracted flight data:", filtered_labels)

# Save extracted data
output_file = os.path.join(os.getcwd(), "flight_data.txt")
with open(output_file, "w", encoding="utf-8") as file:
    for label in filtered_labels:
        file.write(label + "\n")

print(f"Flight data saved to: {output_file}")

driver.quit()
print("Browser closed")
