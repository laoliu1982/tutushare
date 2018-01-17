from selenium import webdriver
import time
from datetime import datetime
import json
import requests
headers={'userkey':'4f17f9f7a7'}
browser = webdriver.Chrome()
url='http://www.lewei50.com/api/V1/gateway/UpdateSensors/01'
#browser=webdriver.PhantomJS()

#browser.set_page_load_timeout(30)
while(1):
    browser.get('http://hotels.ctrip.com/hotel/429200.html?isFull=F#ctm_ref=hod_sr_lst_dl_n_1_3')
    print(time.strftime("%H-%M-%S",time.localtime(time.time())))
#print (browser.title)
    page_info = browser.find_element_by_css_selector('p.staring_price>span.price')
    print(page_info.text)
    print (type(page_info.text))
    payload=[{'Name':'TLGX','Value':page_info.text}]
    r=requests.post(url,json.dumps(payload),headers=headers)
    print(r.text)
    time.sleep(300)
'''
pages = int((page_info.text.split('，')[0]).split(' ')[1])
for page in range(pages):
    if page > 2:
        break
    url = 'http://www.17huo.com/?mod=search&sq=2&keyword=%E7%BE%8A%E6%AF%9B&page=' + str(page + 1)
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)   # 不然会load不完整
    goods = browser.find_element_by_css_selector('body > div.wrap > div:nth-child(2) > div.p_main > ul').find_elements_by_tag_name('li')
    print('%d页有%d件商品' % ((page + 1), len(goods)))
    for good in goods:
        try:
            title = good.find_element_by_css_selector('a:nth-child(1) > p:nth-child(2)').text
            price = good.find_element_by_css_selector('div > a > span').text
            print(title, price)
        except:
            print(good.text)

'''
