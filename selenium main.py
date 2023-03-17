from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                          options=options)

driver.get("http://www.python.org")
event_element = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget div ul li a')
time_element = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget div ul li time')

result = [{time_element[i].text: event_element[i].text} for i in range(len(time_element))]

dictionary = {i: result[i] for i in range(len(time_element))}

print(dictionary)


driver.quit()
