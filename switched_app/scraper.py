from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def ScrapeURL(URL):

    # Start a new session, open the given URL
    driver = webdriver.Firefox() 
    driver.get(URL)

    # Wait for price element to show
    try:
        element = WebDriverWait(driver=driver, timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.cgoQnQ")))
    except:
        print("Unable to detect price")

    # Grab page source and close session
    page_source = driver.page_source
    driver.quit()

    # Moving to beautfiful soup to parse data
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

    return [title, price, heading, description]
