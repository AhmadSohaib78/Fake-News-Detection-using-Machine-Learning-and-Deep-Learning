import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Function to check if the "Next" button is present
def is_next_button_present():
    try:
        driver.find_element(By.CLASS_NAME, 'Pagination-nextPage')
        return True
    except:
        return False

# Function to click the "Next" button
def click_next_button():
    next_button = driver.find_element(By.CLASS_NAME, 'Pagination-nextPage')
    next_button.click()

# Navigate to the initial webpage
url = "https://apnews.com/search?q=fake#nt=navsearch"
driver.get(url)

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Pagination-pageCounts')))

# List to store news names
news_names = []

# Extract and print the text content of all news articles on the first page
promo_elements = driver.find_elements(By.CLASS_NAME, 'PagePromo-title')
for promo_element in promo_elements:
    a_element = promo_element.find_element(By.TAG_NAME, 'a')
    news_name = a_element.text
    print("Fake Name:", news_name)
    news_names.append(news_name)

# Iterate through the next pages until reaching page 10
current_page = 1
while current_page < 20 and is_next_button_present():
    click_next_button()

    # Wait for the new page to load
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Pagination-pageCounts')))

    # Extract and print the text content of all news articles on the current page
    promo_elements = driver.find_elements(By.CLASS_NAME, 'PagePromo-title')
    for promo_element in promo_elements:
        a_element = promo_element.find_element(By.TAG_NAME, 'a')
        news_name = a_element.text
        print("Fake Name:", news_name)
        news_names.append(news_name)

    current_page += 1

# Close the webdriver
driver.quit()

# Write the news names to a CSV file
csv_file_path = 'News_names.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Fake Name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for news_name in news_names:
        writer.writerow({'Fake Name': news_name})

print(f'CSV file "{csv_file_path}" has been created.')
