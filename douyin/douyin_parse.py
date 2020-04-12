import re
import requests
from lxml import etree
from save_to_mongo import get_id
from save_to_mongo import save_user_info

def handle_request(url):
    headers={
        "Referer": "https://www.iesdouyin.com/share/user/88445518961",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80' Safari/537.36"
    }

    resp = requests.get(url,headers=headers)
    return resp.text

def parse_html(html):
    font_list=[
        {'name': ['0xe602', '0xe60e', '0xe618'], 'value': '1'},
        {'name': ['0xe603', '0xe60d', '0xe616'], 'value': '0'},
        {'name': ['0xe604', '0xe611', '0xe61a'], 'value': '3'},
        {'name': ['0xe605', '0xe610', '0xe617'], 'value': '2'},
        {'name': ['0xe606', '0xe60c', '0xe619'], 'value': '4'},
        {'name': ['0xe607', '0xe60f', '0xe61b'], 'value': '5'},
        {'name': ['0xe608', '0xe612', '0xe61f'], 'value': '6'},
        {'name': ['0xe609', '0xe615', '0xe61e'], 'value': '9'},
        {'name': ['0xe60a', '0xe613', '0xe61c'], 'value': '7'},
        {'name': ['0xe60b', '0xe614', '0xe61d'], 'value': '8'}
    ]
    html = html.replace(' &#','0').replace('; ','')

    #替换加密字体
    for font in font_list:
        for name in font['name']:
            if name in html:
                html = re.sub(name,font['value'],html)

    return html
def get_data(parsed_html):
    douyin_data={}
    e = etree.HTML(parsed_html)
    #用xpath获取用户数据
    douyin_data['nickname'] = e.xpath('//p[@class="nickname"]/text()')[0]
    douyin_data['douyin_ID'] = ''.join(e.xpath('//p[@class="shortid"]/i/text()'))
    douyin_data['signature'] = e.xpath('//p[@class="signature"]/text()')[0]
    douyin_data['follow_num'] = e.xpath('//span[@class="focus block"]/span[@class="num"]/i/text()')[0]
    douyin_data['fans_num'] = e.xpath('string(//span[@class="follower block"])').strip()
    douyin_data['liked_num'] = e.xpath('string(//span[@class="liked-num block"])').strip()

    return douyin_data

if __name__ == '__main__':
    share_id = get_id()['share_id']

    url = 'https://www.iesdouyin.com/share/user/{}'.format(share_id)
    html = handle_request(url)
    parsed_html = parse_html(html)
    data = get_data(parsed_html)
    save_user_info(data)


