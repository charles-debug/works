from selenium.webdriver import Chrome
import time

driver = Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get('https://www.baidu.com')
print(driver.title)
time.sleep(5)
driver.quit()