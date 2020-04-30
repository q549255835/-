import requests
from lxml import etree
items = []

def handle_request(url, page):
    url = url.format(str(page))
    #创建请求头
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    r = requests.get(url=url, headers=headers)
   
    tree = etree.HTML(r.text)
    herf_list = tree.xpath('//div/ul[@class="book-list"]/li/a/@href')
    for book in herf_list:
        #print(book)
        url = book
        r = requests.get(url=url, headers=headers)
        parse(r.text)
    

def parse(content):
    tree = etree.HTML(content)
    # 获取书名
    book_name = tree.xpath('//div[@class="book-breintro"]/h3/text()')[0]
    # 获取评分
    book_score = tree.xpath('//div[@class="book-breintro"]/div/@data-douscore')
    # 书本价格
    book_price = tree.xpath('//div[@class="book-breintro"]/div[3]/span/text()')
    # 基本信息
    book_public = tree.xpath('//div[@class="book-breintro"]/div[2]/text()')[0]

    item = {
    '书名': book_name,
    '评分': book_score,
    '价格': book_price,
    '基本信息': book_public,
    }
    items.append(item)
    #print(items)
    
    






def main():
    url = 'https://market.douban.com/book/?utm_campaign=book_freyr_section&utm_source=douban&utm_medium=pc_web&page={}&page_num=18&'
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}
    start_page = int(input("请输入起始页码："))
    end_page = int(input("请输入结束页码："))
    for page in range(start_page, end_page+1):
        #创建请求对象
        request = handle_request(url, page)
        # 解析内容
      
    #写入内容
    with open('豆瓣读书.text', 'w', encoding='utf8') as fp:
        fp.write(str(items) + '\n' + ' ')


    

        





if __name__ == '__main__':
    main()