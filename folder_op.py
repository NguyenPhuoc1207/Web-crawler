#Các thư viện cần thiết
import os
import codecs

#Các hàm
def tao_thu_muc():
    a=input("Nhập thư mục bạn muốn tạo:")
    os.mkdir(a)
    os.chdir(a)


#Hàm lưu nội dung vào file ở thư mục chỉ định
def luu_noi_dung_xuong_file(data, stt):
    file = codecs.open('file' + str(stt) + '.html', 'w', 'utf8')
    file.write(data.text)
    file.close()
