import requests
from lxml import etree
import time

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

items = []
def handle_request(url,page):
    url = url.format(str(page))
    #发送请求
    r = requests.get(url, headers=headers)
    # 解析内容
    tree = etree.HTML(r.text)
    ip_list = tree.xpath('//table/tbody/tr')
    for oip in ip_list:
        # IP地址：
        ip = tree.xpath('.//td[1]/text()')[0]
        # 位置
        weizhi = tree.xpath('.//td[5]/text()')[0]
        # 响应速度
        sudu = tree.xpath('.//td[6]/text()')[0]
        # 验证时间
        yzsj = tree.xpath('.//td[7]/text()')[0]

        item = {'ip': ip,
                '位置': weizhi,
                '响应速度': sudu,
                '验证时间': yzsj,    

        }
        items.append(item)

        with open('代理.txt', 'w', encoding='utf8') as fp:
            fp.write(str(items))






def main():
    url = 'https://www.kuaidaili.com/free/inha/{}/'
    start_page = int(input('请输入开始页码：'))
    end_page = int(input('请输入结束页码：'))
    for page in range(start_page, end_page+1):
        handle_request(url, page)




if __name__ == '__main__':
    main()