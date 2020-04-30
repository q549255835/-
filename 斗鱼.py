import requests
import json


s = requests.session()
offset_page = 1

url = 'https://www.douyu.com/gapi/rkc/directory/2_1008/' + str(offset_page)

# 发送请求获取响应
htmltext = s.get(url).text

htmltext = json.loads(htmltext.encode('utf-8'))
print(htmltext)

#解析网页
while True:
	if len(htmltext['data']) != 0:
		for data in htmltext['data']:
			nickname = data['nickname']
			f = open("./Image/" + nickname + ".jpg", "wb")
			imagelink = data["vertical_src"]

			f.write(s.get(imagelink).content)

		offset_page == 20
        url = 'https://www.douyu.com/gapi/rkc/directory/2_1008/' + str(offset_page)
        htmltext = s.get(url).text

        htmltext = json.loads(htmltext.encode("utf-8"))
    else:
    	break











