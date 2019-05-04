# Import tools.
from selenium import webdriver
import time


def test():
    # Get Chrome Driver.
    driver = webdriver.Chrome(executable_path="C:/Devops/chromedriver.exe")
    # Time to get the tools.
    driver.implicitly_wait(10)
    # Open the Site.
    driver.get("http://192.168.99.100:5000")
    # Find the element.
    text = driver.find_element_by_xpath("//html/body")
    new_text = str(text.text).replace(" World", " ")
    print(new_text)
    # Print the txt.
    time.sleep(3)
    # Close the Site.
    driver.quit()


if __name__ == '__main__':
    test()
