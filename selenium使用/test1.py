from selenium import webdriver


driver_path = "D:\MyDownloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")
