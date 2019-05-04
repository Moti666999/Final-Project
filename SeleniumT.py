# Import tools.
from selenium import webdriver
import time


def test():
    # Get Chrome Driver.
    driver = webdriver.Chrome(executable_path="C:/Devops/chromedriver.exe")
    driver.implicitly_wait(10)
    # Open the Window.
    driver.get("http://192.168.99.100:5000")
    text = driver.find_element_by_xpath("//html/body")
    print(text.text)
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    test()
