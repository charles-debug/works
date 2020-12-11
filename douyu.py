from selenium import webdriver
import time

# 程序入口
def get_layout_Cover_list():
    # 睡眠10秒
    time.sleep(10)
    list_contents = driver.find_elements_by_xpath('//ul[@class="layout-Cover-list]/li')

    for item in list_contents:
        # print(item)
        img=item.find_element_by_xpath('//img[@class="DyImg-content is-normal "]').get_attribute('src')

        title=item.find_element_by_xpath('//h3[@class="DyListCover-intro"]').text
        print(img, title)

if __name__ == "__main__":
    url='https://www.douyu.com/directory/all'

    driver = webdriver.Chrome()
    # 发送请求，获取服务器响应
    driver.get(url)
    get_layout_Cover_list(driver)
    