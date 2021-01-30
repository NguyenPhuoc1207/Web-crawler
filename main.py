
# Các thư viện cần thiết
import folder_op, web_op #sử dụng thư viện mình đa tạo

def start():
    #Nhóm các biến toàn cục cung cấp thông số cho chương trình
    domain = input("nhap link trang web:")  #trang chủ để chứa các đường link
    url_list = history = []  #Chứa các đường link đã duyệt
    max_page =int(input("nhập số trang bạn muốn tải:"))  #Nhập số lượng trang web mà bạn muốn tải
    count = 0 #Đếm số lượng trang web đã tải về
    folder_op.tao_thu_muc() # sử dụng thư viện để tạo thư mục
    url_list.append(domain) #thêm đường link mình nhập từ domain vào list url_list
    #Kịch bản tải các trang web
    while (count < max_page) and (len(url_list) > 0): #sử dụng vòng lặp while với điều kiện biến đếm phải nhỏ hơn số lượng của page và độ dài của link phải lớn hơn 0
        url = url_list.pop(0) # lấy phần tử đầu tiên từ urlist
        history.append(url)  #thêm phần tử vào history
        count += 1 #tăng biến đếm lên 1
        data = web_op.doc_noi_dung(url) # gọi thư viện web_op và gọi hàm doc_noi_dung
        list_links = web_op.quet_url_va_sua_html(domain,data)
        for item in list_links: #Duyệt từng đường link thu được để kiểm tra tính hợp lệ
            if (item not in url_list) and ( item not in history):  #Nếu đường link chưa hề được duyệt và chưa có trong hàng đợi
                url_list.append(item) #Thêm đường link mới vào danh sách chờ duyệt
        folder_op.luu_noi_dung_xuong_file(data, count)

        print(count, url)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/