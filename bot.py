from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://web.whatsapp.com/')
time.sleep(2)

cellphone = "573006165599"
message = "Hi, this is my first bot"

driver.get("https://wa.me/"+cellphone+"?text="+message)

button = driver.find_element_by_xpath("//*[@id='action-button']")[0]
button.click(0)
time.sleep(2)

button = driver.find_element_by_xpath("//*[@id='fallback_block']/div/div/a")[0]
button.click()
time.sleep(5)

# Send the information (press button):
button = driver.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]")[0]
button.click()
time.sleep(2)

print("The bot is done!")
time.sleep(5)
driver.close()
