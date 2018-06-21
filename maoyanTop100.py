#!/usr/bin/env python3
# -*-coding:UTF-8-*-
import requests
import re

# 获取网页
def get_html(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36"
  }
    response = requests.get(url,headers=headers)
    return response.text


# 解析网页
def resolveHtml(html):
    # 自己写的正则表达式，我自己都怕
    #stringRe = "<dd>.*?<i.*?>(.*?)</i>.*?<p.*?>(.*?)</a></p><p>(.*?)</p>.*?<p.*?>(.*?)</p>.*?<p class='score'>.*?>(.*?)</i><i.*?>(.*?)</i.*?</dd>"
    stringRe = "<dd>.*?>(.*?)</a></p>.*?</dd>"
    patern = re.compile(stringRe,re.S)
    text = re.findall(patern, html)
    print(text)

def main():
    url = "http://maoyan.com/board/4"
    html = get_html(url)
    txt = resolveHtml(html)
    print(type(txt))
if __name__ == "__main__":
    main()