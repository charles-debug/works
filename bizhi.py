import requests
import parsel
import os

for page in range(1,6):
    print(f'正在打印{page}页数据')
    #1. 分析目标网页，确定爬取网页url 和headers
    base_url = 'http://www.win4000.com/mobile_2340_0_0_{}.html'.format(page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }

    # 2.发送请求，模拟浏览器发送请求，获取响应数据
    response = requests.get(base_url, headers=headers)
    data = response.text
    # print(data)

    # 3.解析数据 parsel 模块
    # 转化成selector对象，该对象可以使用xpath方法

    html_data = parsel.Selector(data)
    data_list = html_data.xpath('//div[@class="Left_bar"]//ul[@class="clearfix"]/li/a/@href|//div[@class="Left_bar"]//ul[@class="clearfix"]/li/a/@title').extract()
    # data_name = html_data.xpath('//div[@class="Left_bar"]//ul[@class="clearfix"]/li/a[@title]/@title').extract()
    # print(data_list, data_name)
    # 使用列表推导式对列表进行分组
    data_list = [data_list[i:i+2]for i in range(0, len(data_list), 2)]
    # print(data_list)

    for alist in data_list:
        html_url = alist[0]
        file_name = alist[1]
        # print(html_url, file_name)

        # 创建文件文件夹
        if not os.path.exists('img\\' + file_name):
            os.makedirs('img\\' + file_name)
            print('文件正在下载', file_name)


        response_2 = requests.get(html_url, headers=headers).text
        html_2 = parsel.Selector(response_2)
        page_num = html_2.xpath('//div[@class = "ptitle"]//em/text()').extract_first()

        for url in range(1,int(page_num)+1):
            url_list = html_url.split('.')
            # print(url_list)
            all_url = url_list[0]+'.'+url_list[1]+'.'+url_list[2]+'_'+str(url)+'.'+url_list[3]
            # print(all_url)

            response_3 = requests.get(all_url, headers=headers).text
            html_3 = parsel.Selector(response_3)
            img_url = html_3.xpath('//div[@class="pic-meinv"]//img/@src').extract_first()
            print(img_url)
            img_data = requests.get(img_url, headers=headers).content

            img_name= str(url) + '.jpg'


            with open('img\\{}\\'.format(file_name)+img_name,'wb') as f:
                f.write(img_data)
                print(file_name)


