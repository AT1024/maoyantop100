import requests
import re,json
from multiprocessing import Pool
from requests.exceptions import RequestException
def get_one_page(url):
    try:
        # 常见的反爬虫策略，用于模拟浏览器
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e:
        return None

def parse_one_page(html):
    # 根据我们需要的信息，生产正则表达式对象
    patern = re.compile('<dd>.*?name">.*?>(.*?)</a></p>'
                        +'.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S
    )
    items = re.findall(patern,html)
    for item in items:
        yield {
            'name': item[0],
            'actor':item[1].strip()[3:],
            'time':item[2][5:],
            'score': item[3]+item[4]
        }

def write_to_file(content):
    with open('result.txt','a',encoding='UTF-8') as f:
        # 字符编码没有弄清楚
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main(offset):
    url = "http://maoyan.com/board/4?offset="+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

'''-----简单抓取----------
if __name__=='__main__':
    for i in range(10):
        main(i*10)
'''

# ------多进程抓取------
if __name__=='__main__':
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])