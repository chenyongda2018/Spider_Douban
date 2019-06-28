import requests
from bs4 import BeautifulSoup

'''
爬取豆瓣TOP250电影信息,图片
'''

urls = [' https://movie.douban.com/top250?start=' + str(n) + "&filter=" for n in range(0, 250, 25)]
i = 0
for url in urls:
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml');
    # 电影名称
    titles = soup.select("div.hd > a")
    # 电影评分
    ratings = soup.select("span.rating_num")
    # 图片
    imgs = soup.select('img[width="100"]')

    for title, rate, img in zip(titles, ratings, imgs):
        data = {
            'title': list(title.stripped_strings),
            'rate': rate.get_text(),
            'img': img.get('src')
        }
        '''
        将图片下载下来保存在本地
        文件名格式: 1,肖申克的救赎 9.6分.jpg
        '''
        i += 1
        fileName = str(i) + "," + data['title'][0] + " " + data['rate'] + "分.jpg"
        pic = requests.get(data['img'])
        with open('imgs/' + fileName, "wb") as photo:
            photo.write(pic.content)
        print(fileName)
