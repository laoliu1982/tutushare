from selenium import webdriver
import time
from datetime import datetime
import json
import requests
from selenium.webdriver.chrome.options import Options

options = Options()
#options.binary_location='/usr/bin/chromium-browser'

options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.binary_location='/usr/bin/chromium-browser'
print (options)
headers={'userkey':'4f17f9f7a7'}
#browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=options)

browser = webdriver.Chrome()
css_selector='#content>div>ul>li.item.recommend-item>div.cell-star.dl-cell.room--space>div.cell-end.room-column.js_bookroom>p>span>span'
ctrip_url='http://m.ctrip.com/webapp/hotel/hoteldetail/429200.html?days=1&atime=20180127&contrl=0&num=undefined&biz=undefined'
url='http://www.lewei50.com/api/V1/gateway/UpdateSensors/01'
#browser=webdriver.PhantomJS()

#browser.set_page_load_timeout(30)
while(1):
    #browser.get('http://hotels.ctrip.com/hotel/429200.html?isFull=F#ctm_ref=hod_sr_lst_dl_n_1_3')
    try:
        browser.get(ctrip_url)
        print(time.strftime("%H-%M-%S",time.localtime(time.time())))
        #print (browser.title)
        page_info = browser.find_element_by_css_selector(css_selector)
        print(page_info.text)
        print (type(page_info.text))
        payload=[{'Name':'TLGX','Value':page_info.text}]
        r=requests.post(url,json.dumps(payload),headers=headers)
        print(r.text)
        time.sleep(120)
    except Exception as e:
        print (e)
        browser = webdriver.Chrome()

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
