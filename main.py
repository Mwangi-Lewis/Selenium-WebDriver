from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# #keep browser open after program finishes
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
#
#
# driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/ASUS-GeForce-Graphics-Exclusive-Motherboards/dp/B0DB67PPCM/ref=sr_1_2?crid=14UOJPWF5U3ZQ&dib=eyJ2IjoiMSJ9.JP4e44x75k4A4IxdLPK_oDnoUuHCoMh0MVO0I9ssshW8MWjtBBLt4QxlRG5Fjkt_iqDTfO1JAkT-UmoSNy-EhMiM7hNtK4dZilPWzwfIHYufU_TSkE1sWs_tMxdmJjQGuayeYxkP8LsxBhOGG0BPGOGvcBjMljvBw80aAgzoFvnlmE0DL9vrKIid4HeNktak3jdKwmbIftluEClz0hJ7VKebCxfDafrR8yYXIOtXMy4.KDtQuA2tG-9mTFXn089BYqeZyrri3YaDRw7eLbwT9MI&dib_tag=se&keywords=rtx+4090&qid=1733472904&sprefix=rtx+4090%2Caps%2C348&sr=8-2")
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents= driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")
#
# driver.find_element(By.Name, value="q")
# driver.quit()

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Python.org
driver.get("https://www.python.org/")

# Amazon's Instant Pot
# driver.get("https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/?th=1")

# By.CLASS_NAME (uses amazon.com website)
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# Locating strategies for a single element
# By.NAME
search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# By.ID
button = driver.find_element(By.ID, value="submit")
# print(button.size)

# By.CSS_SELECTOR
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# By.XPath
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Finding multiple elements
tier_1 = driver.find_elements(By.CLASS_NAME, value="tier-1")

# Challenge: Print the event dates from python.org
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

# driver.close()
driver.quit()