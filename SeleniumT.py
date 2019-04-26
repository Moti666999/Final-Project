# Import tools.
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:/Devops/chromedriver.exe")
driver.implicitly_wait(10)
driver.get("http://192.168.99.100:5000")
text = driver.find_element_by_xpath("//html/body")
print(text.text)
driver.quit()
