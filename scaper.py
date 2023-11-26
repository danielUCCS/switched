from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

import pandas as pd

list = []

# Set up selenium
driver = webdriver.Firefox() # configure firefox webdriver
driver.get("https://www.nintendo.com/us/store/products/the-legend-of-zelda-tears-of-the-kingdom-switch/")
#wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
#elem = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Pricestyles__PriceWrapper-sc-1f0n8u6-1 eroAfM")))

element = WebDriverWait(driver=driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cgoQnQ")))

page_source = driver.page_source

# Moving to beautfiful soup to parse data
soup = BeautifulSoup(page_source, 'html.parser')
results = soup.find(id="main")

title_element = results.find("h1", class_="Headingstyles__StyledH-sc-s17bth-0 eQifGC")
price_element = results.find("p", class_="Textstyles__StyledPara-sc-w55g5t-4 dQCCpW RadioDetailedstyles__Price-sc-d1kg1d-5 cTzeTR")
heading_element = results.find("h2", class_="Headingstyles__StyledH-sc-s17bth-0 eQifGC")
description_element = results.find("p", class_="RichTextstyles__Paragraph-sc-16r5mbt-0 NqoHc")
image_url_element = results.find("div", class_="MediaGallerystyles__CropFrame-sc-1fakp5g-6 eDOgNa").find("img")

print(title_element.text)
print(price_element.text)
print(heading_element.text)
print(description_element.text)
print(image_url_element.attrs['src'])

data = {"title": title_element.text,
        "price": price_element.text,
        "heading": heading_element.text,
        "description": description_element.text,
        "img src": image_url_element.attrs['src']
        }

list.append(data)

driver.quit()

df = pd.DataFrame(list)
df.to_csv('Nintendo.csv', index=False)