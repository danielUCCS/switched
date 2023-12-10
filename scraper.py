from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

# URL to scrape
URL = "https://www.nintendo.com/us/store/products/the-legend-of-zelda-breath-of-the-wild-switch/"

# Set up selenium
driver = webdriver.Firefox() # configure firefox webdriver
driver.get(URL)

# Wait for price to show
element = WebDriverWait(driver=driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cgoQnQ")))

# Grab page source and quit
page_source = driver.page_source
driver.quit()

# Moving to beautfiful soup to parse data
soup = BeautifulSoup(page_source, 'html.parser')
results = soup.find(id="main")

title_element = results.find("h1", class_="Headingstyles__StyledH-sc-s17bth-0 eQifGC")
price_element = results.find("p", class_="Textstyles__StyledPara-sc-w55g5t-4 dQCCpW RadioDetailedstyles__Price-sc-d1kg1d-5 cTzeTR")
heading_element = results.find("h2", class_="Headingstyles__StyledH-sc-s17bth-0 vsVuC")
description_element = results.find("div", class_="RichTextstyles__Html-sc-16r5mbt-1 kdsZWM clamp")
image_url_element = results.find("div", class_="MediaGallerystyles__CropFrame-sc-1fakp5g-6 eDOgNa").find("img")

print(title_element.text)
print(price_element.text)
print(heading_element.text)
print(description_element.text)
print(URL)
print(image_url_element.attrs['src'])

list = [title_element.text, price_element.text, heading_element.text, description_element.text, URL, image_url_element.attrs['src']]

df = pd.DataFrame(list).to_csv('Nintendo.csv', index=False)