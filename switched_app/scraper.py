from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def ScrapeURL(URL):

    # Start new browser session, navigate to URL
    driver = webdriver.Firefox() # configure firefox webdriver
    driver.get(URL)

    # Wait for price element to load
    try:
        element = WebDriverWait(driver=driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cgoQnQ")))
    except:
        print("Unable to detect price")

    # Grab page source and close session
    page_source = driver.page_source
    driver.quit()

    # Create new soup object to parse html
    soup = BeautifulSoup(page_source, 'html.parser')
    results = soup.find(id="main")

    try:
        title = results.find("h1", class_="Headingstyles__StyledH-sc-s17bth-0 eQifGC").text
    except:
        title = "null"
    
    try:
        price = results.find("p", class_="Textstyles__StyledPara-sc-w55g5t-4 dQCCpW RadioDetailedstyles__Price-sc-d1kg1d-5 cTzeTR").text
    except:
        price = "null"
    
    try:
        heading = results.find("h2", class_="Headingstyles__StyledH-sc-s17bth-0 vsVuC").text
    except:
        heading = "null"

    try:
        description = results.find("div", class_="RichTextstyles__Html-sc-16r5mbt-1 kdsZWM clamp").text
    except:
        description = "null"

    try:
        image_url = results.find("div", class_="MediaGallerystyles__CropFrame-sc-1fakp5g-6 eDOgNa").find("img").attrs['src']
    except:
        image_url = "null"

    # Print out scraped data for testing
    print(title)
    print(price)
    print(heading)
    print(description)
    print(image_url)

    list = [title, price, heading, description, image_url]

    return list 