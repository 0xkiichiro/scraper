from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Define the URL of the website to be scraped
url = "https://www.trendyol.com/sr?wg=1%2C2&cid=604351%2C617606&pi=2"

# Initialize a webdriver object to control a web browser
options = Options()

options.add_argument("--disable-extensions")
# options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--disable-setuid-sandbox")
options.add_experimental_option("prefs", {
  "profile.default_content_setting_values.notifications": 2
})
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-accelerated-2d-canvas")
# options.add_argument("--disable-gpu-sandbox")
# options.add_argument("--no-first-run")
# options.add_argument("--no-zygote")
# options.add_argument("--single-process")
driver = webdriver.Chrome(options=options)

# Navigate to the website
driver.get(url)

# Wait for the pop-up to appear for 10 seconds
wait = WebDriverWait(driver, 10)

list = []

while True:
    # Extract the HTML of the website
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    # print(soup)
    try:
        pop_up = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "popup")))
        if pop_up:
            overlay = item.find("div", class_="overlay")
        # Click on the pop-up
            driver.execute_script("arguments[0].click();", pop_up)
    except:
        pass
    # Locate the HTML elements containing the item's name, price, and picture link
    items = soup.find_all("div", class_="p-card-chldrn-cntnr card-border")
    # print(items)
    for item in items:
        if list.count(item) < 1:
            list.append(f"{item}")
            # print(item)
            try:
                # name = item.find("span", class_="prdct-desc-cntnr-name hasRatings").text
                # price = item.find("div", class_="prc-box-orgnl").text
                # picture_link = item.find("img", class_="p-card-img")["src"]

                # item.name = name
                # item.price = price
                # item.picture_link = picture_link
                
                # print("Name: ", name)
                # print("Price: ", price)
                # print("Picture Link: ", picture_link)
                print(len(list))
                if len(list) > 100:
                    with open("./list.txt", "w") as outfile:
                        listinstring=""
                        for item in list:
                            listinstring+=str(item)+"\n"
                        outfile.write(listinstring)
                    break
            except Exception as ex:
                print("----")
                print(ex)
    # Scroll to the end of the web page
    driver.execute_script("window.scrollTo(10, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo(15, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo(10, document.body.scrollHeight);")
    
    # Repeat the process until all items have been scraped
    # if not soup.find("a", class_="next-page"):
    #     break

# End the scraping process
driver.quit()
