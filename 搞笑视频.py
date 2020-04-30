import requests
from lxml import etree
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
"""
在提取视频下载源的src时，通过正常途径利用xpath解析不到src，网址应该是用了js反爬，最终用了无头浏览器获取网页源码得到解决。
如遇到js反爬
考虑思路：1 捕获网页链接接口：不能用网页原链接解析。url = '网页的js接口' 就是json的url
 js捕获方式：找到网页js相关文件 进行js格式翻译，解析内容返回的是json格式数据，直接用json解析即可；再通过分析，要json里的相关数据，例如要data里的url; 将json数据转化为pytho对象：obj = json.loads(r.text)；取出所有和视频相关的数据，data = obj['data']; 循环data列表，取出每一个视频信息 
  for vider_data in data:
      title = vider_data['title'] 注意 链接是否需要拼接
2，找不到src时，可用 with open 写下文件，找相关的video；不行就再次进行抓包，找js文件，如还找不到就用无头浏览器进行网页源码抓取，抓去之后再用xpath看是否能够直接提取到src，就先找前一个标签，如果能找到前一个标签，就再次用with open 将源代码写下来，写下之后再找sec具体所在标签。
"""

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'}

def handle_title(url, page):    
    if page == 1:
        url = url.format('')
    else:
        url = url.format('_' + str(page))
    
    r = requests.get(url, headers=headers)
    # 利用xpath解析
    tree = etree.HTML(r.text)
    # 获取所有视频链接
    href_url = tree.xpath('//div[@class="a_itemBox"]/div[2]/a/@href')
    # 获取所有的视频名字

    #print(href_url)
    for s_url in href_url:     
        src_url(s_url)

def src_url(s_url):
    print("lala")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    path = r'/Applications/chromedriver'
    browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)
    browser.get(s_url)
    print('*'*20)
    time.sleep(3)
    #获取源码，生成tree对象，然后查找video里面的src  
    tree = etree.HTML(browser.page_source)
    # 获取所有视频的src
    try:
        v_src = tree.xpath('//video[@id="HTML5Player"]/@src')[0]
    except Exception as e:
        pass   
    v_name = tree.xpath('//div[@class="leftPart"]/h1/text()')[0]
    print('lululu')
    # 下载视频
    dirpath = 'gaoxiaoshipin'
    # 创建文件夹
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
        print('文件夹创建完成')
    
    filepath = 'gaoxiaoshipin/' + v_name + '.mp4'
    print('%s开始下载。。。。。' % v_name)
    request = requests.get(v_src)
    with open(filepath, 'wb') as fp:
        fp.write(request.content)
    print('%s结束下载。。。。。' % v_name)
    

    


def main():
    url = 'http://gaoxiao.52op.net/fangyan/index{}.htm'
    start_page = int(input("请输入下载开始页码："))
    end_page = int(input("请输入下载结束页码："))
    for page in range(start_page, end_page+1):
        # 发送请求 返回所有标题链接
        handle_title(url, page)
        # 向标题链接发送请求获取视频src
        


        



if __name__ == '__main__':
    main()