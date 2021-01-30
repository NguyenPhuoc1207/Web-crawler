#Các thư viện cần thiết
import requests
from bs4 import BeautifulSoup
import re

#Các hàm cần thiết
#Hàm đọc nội dung của trang web theo url chỉ định
#Kết quả trả về là 1 văn bản dạng chuỗi
def doc_noi_dung(url):
    # Gửi yêu cầu truy cập url
    raw_page = requests.get(url)
    content = BeautifulSoup(raw_page.text, "html.parser")
    # Lấy code html của trang web được trả về theo url
    return content




def quet_url_va_sua_html(domain,data):
    url_list = []
    a_tag = data.find_all("a")
    pattern1 = '^(http://|https://)'
    pattern2 = '^/.*'
    for item in a_tag:
        link = item.get('href')
        link = str(link)
        checkhttp = re.match(pattern1, link) is not None
        checkurl = re.match(pattern2, link) is not None
        if checkhttp:
            url_list.append(link)
        elif checkurl:
            url_list.append(domain + link)
    return url_list
