import requests
import parsel


def check_ip(proxies_list):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }
    for proxy in proxies_list:
        requests.get('https://www.baidu.com', headers=headers, proxies = proxy, timeout = 0.1)

proxies_list = []
for page in range(1,10):

    base_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
    print('===========正在抓取{page}页============'.format(page))

    

    response = requests.get(base_url, headers = headers)
    data = response.text
# print(data)

    html_data = parsel.Selector(data)
# print(html_data)
    parsel_list = html_data.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
# print(parsel_list)

   
    for tr in parsel_list:
        proxies_dict = {}
        http_type = tr.xpath('./td[4]/text()').extract_first()
        ip_num = tr.xpath('./td[1]/text()').extract_first()
        port_num = tr.xpath('./td[2]/text()').extract_first()
    # print(http_type, ip_num, port_num)

        proxies_dict[http_type] = ip_num + ":" + port_num
    # print(proxies_dict)

        proxies_list.append(proxies_dict)


print(proxies_list)

print(len(proxies_list),'个')

